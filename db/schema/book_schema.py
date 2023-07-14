import graphene
from db.entity.books_entity import Book 
from repository.repo_book import Books_repository 

#### CONSULTAS  get #####
class Query(graphene.ObjectType):
    book = graphene.List(Book)
    books = graphene.List(
        Book,
        title=graphene.String(),
        subtitle=graphene.String(),
        author=graphene.String(),
        category=graphene.String(),
        published_date=graphene.String(),
        publisher=graphene.String()
    )

    @staticmethod
    def resolve_books(root, info,
                      title: str = None,
                      subtitle: str = None,
                      author: str = None,
                      category: str = None,
                      published_date: str = None,
                      publisher: str = None):
        
        repo = Books_repository()
        data_books = repo.read_books(title, subtitle, author, category, published_date, publisher)
        return data_books
            

### MODIFICACIONES delete, update, create
class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)