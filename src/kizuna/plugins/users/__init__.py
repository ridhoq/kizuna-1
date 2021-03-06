from kizuna.adapters.slack import SlackCommand, SlackMessage, SlackAdapter
from kizuna.skills.db import DB
from .models.user import User
from config import KIZUNA_WEB_URL
from kizuna.plugins.users.models.user import User
from kizuna.support.utils import build_url


class UserRefreshCommand(SlackCommand):
    """
    usage: {bot} refresh users - Make sure my users database is up-to-date with slack. You probably want to run this if
    someone has changed their name or a new user has joined slack.
    """

    @staticmethod
    def handle(message: SlackMessage, bot: SlackAdapter, db: DB):

        res = bot.client.api_call('users.list')

        if not res['ok']:
            raise RuntimeError('call to users.list failed')

        slack_members = [member for member in res['members'] if not member['deleted']]

        with db.session_scope() as session:
            def maybe_create(slack_id):
                return User.maybe_create_user_from_slack_id(slack_id, bot.client, session)

            kizuna_members = [maybe_create(member['id']) for member in slack_members]

            for member in kizuna_members:
                el = [x for x in slack_members if x['id'] == member.slack_id]
                if not el:
                    continue

                el = el[0]

                if member.name != el['name']:
                    member.name = el['name']

        bot.reply(message, 'Refreshed users. :^)')


class LoginCommand(SlackCommand):
    """usage: {bot} login - login to the web interface"""

    @staticmethod
    def handle(message: SlackMessage, bot: SlackAdapter, db: DB):
        with db.session_scope() as session:
            user = User.get_by_slack_id(session, message.user)

            if not user:
                return bot.reply(message, """
                I don't have your user in the db. Prolly run 'kizuna refresh users' and if that still doesn't fix it:
                Austin fucked up somewhere :^(
                """.strip(), ephemeral=True)

            bot.reply(message, build_url(KIZUNA_WEB_URL, '/login', {'auth': user.get_token()}), ephemeral=True)
