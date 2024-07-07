package dal

import (
    "context"
    "time"

    "backend/models"

    "go.mongodb.org/mongo-driver/bson"
    "go.mongodb.org/mongo-driver/bson/primitive"
    "go.mongodb.org/mongo-driver/mongo"
)

type UserDAL struct {
    collection *mongo.Collection
}

func NewUserDAL(client *mongo.Client, dbName, collName string) *UserDAL {
    return &UserDAL{
        collection: client.Database(dbName).Collection(collName),
    }
}

func (dal *UserDAL) CreateUser(ctx context.Context, user *models.User) error {
    user.ID = primitive.NewObjectID()
    user.CreatedAt = time.Now()
    user.LastLogin = time.Now()
    _, err := dal.collection.InsertOne(ctx, user)
    return err
}

func (dal *UserDAL) GetUserByID(ctx context.Context, id primitive.ObjectID) (*models.User, error) {
    var user models.User
    err := dal.collection.FindOne(ctx, bson.M{"_id": id}).Decode(&user)
    return &user, err
}