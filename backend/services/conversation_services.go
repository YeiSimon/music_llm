package services

import (
    "context"

    "backend/dal"
    "backend/models"

    "go.mongodb.org/mongo-driver/bson/primitive"
)

type ConversationService struct {
    dal *dal.ConversationDAL
}

func NewConversationService(dal *dal.ConversationDAL) *ConversationService {
    return &ConversationService{dal: dal}
}

func (s *ConversationService) CreateConversation(ctx context.Context, conversation *models.Conversation) error {
    return s.dal.CreateConversation(ctx, conversation)
}

func (s *ConversationService) GetConversationByID(ctx context.Context, id primitive.ObjectID) (*models.Conversation, error) {
    return s.dal.GetConversationByID(ctx, id)
}
