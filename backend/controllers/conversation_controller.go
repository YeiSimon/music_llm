package controllers

import (
    "net/http"

    "backend/models"
    "backend/services"

    "github.com/gin-gonic/gin"
    "go.mongodb.org/mongo-driver/bson/primitive"
)

type ConversationController struct {
    service *services.ConversationService
}

func NewConversationController(service *services.ConversationService) *ConversationController {
    return &ConversationController{service: service}
}

func (ctrl *ConversationController) CreateConversation(c *gin.Context) {
    var conversation models.Conversation
    if err := c.BindJSON(&conversation); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    if err := ctrl.service.CreateConversation(c.Request.Context(), &conversation); err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusCreated, conversation)
}

func (ctrl *ConversationController) GetConversation(c *gin.Context) {
    id := c.Param("id")
    objID, err := primitive.ObjectIDFromHex(id)
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid ID"})
        return
    }
    conversation, err := ctrl.service.GetConversationByID(c.Request.Context(), objID)
    if err != nil {
        c.JSON(http.StatusNotFound, gin.H{"error": "Conversation not found"})
        return
    }
    c.JSON(http.StatusOK, conversation)
}
