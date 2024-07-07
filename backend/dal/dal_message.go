package dal

import (
    "context"
    "time"

    "backend/models"

    "go.mongodb.org/mongo-driver/bson"
    "go.mongodb.org/mongo-driver/bson/primitive"
    "go.mongodb.org/mongo-driver/mongo"
)

type MessageDAL struct {
    collection *mongo.Collection
}

func NewMessageDAL(client *mongo.Client, dbName, collName string) *MessageDAL {
    return &MessageDAL{
        collection: client.Database(dbName).Collection(collName),
    }
}

func (dal *MessageDAL) CreateMessage(ctx context.Context, message *models.Message) error {
    message.ID = primitive.NewObjectID()
    message.Timestamp = time.Now()
    _, err := dal.collection.InsertOne(ctx, message)
    return err
}

func (dal *MessageDAL) GetMessageByID(ctx context.Context, id primitive.ObjectID) (*models.Message, error) {
    var message models.Message
    err := dal.collection.FindOne(ctx, bson.M{"_id": id}).Decode(&message)
    return &message, err
}
