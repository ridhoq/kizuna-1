from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from kizuna.support.models.Models import Base


class MentionGraphEdge(Base):
    __tablename__ = 'at_graph_edges'

    id = Column('id', Integer, primary_key=True)
    head_user_id = Column('head_user_id', Integer, ForeignKey('users.id'))
    head_user = relationship("User", foreign_keys=[head_user_id])
    tail_user_id = Column('tail_user_id', Integer, ForeignKey('users.id'))
    tail_user = relationship("User", foreign_keys=[tail_user_id])
    weight = Column('weight', Integer, nullable=False)

    def __repr__(self):
        return "<AtGraphEdge(id='{}', head_user_name='{}', tail_user_name='{}')>".format(self.id,
                                                                                         self.head_user.name,
                                                                                         self.tail_user.name)

    @staticmethod
    def increment_edge(head_user, tail_user, session):
        edge = session \
            .query(MentionGraphEdge) \
            .filter(MentionGraphEdge.head_user_id == head_user.id) \
            .filter(MentionGraphEdge.tail_user_id == tail_user.id) \
            .first()

        if not edge:
            edge = MentionGraphEdge(head_user_id=head_user.id,
                                    tail_user_id=tail_user.id,
                                    weight=0)
            return session.add(edge)

        edge.weight = MentionGraphEdge.weight + 1
        session.add(edge)
