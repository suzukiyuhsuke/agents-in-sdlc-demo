from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key, name):
        """
        Validate that the category name meets minimum length requirements.
        
        Args:
            key (str): The attribute name being validated
            name (str): The category name value to validate
            
        Returns:
            str: The validated category name
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key, description):
        """
        Validate that the category description meets minimum length requirements.
        
        Args:
            key (str): The attribute name being validated
            description (str): The description value to validate
            
        Returns:
            str: The validated description
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self):
        """
        Return a string representation of the Category object.
        
        Returns:
            str: A string showing the category name
        """
        return f'<Category {self.name}>'
        
    def to_dict(self):
        """
        Convert the Category object to a dictionary for JSON serialization.
        
        Returns:
            dict: A dictionary containing the category's attributes including
                  the count of associated games
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }