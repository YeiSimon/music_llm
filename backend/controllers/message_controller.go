package controllers

import (
    "net/http"

    "backend/models"
    "backend/services"

    "github.com/gin-gonic/gin"
    "go.mongodb.org/mongo-driver/bson/primitive"
)

type MessageController struct {
    service *services.MessageService
}

func NewMessageController(service *services.MessageService) *MessageController {
    return &MessageController{service: service}
}

func (ctrl *MessageController) CreateMessage(c *gin.Context) {
    var message models.Message
    if err := c.BindJSON(&message); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    if err := ctrl.service.CreateMessage(c.Request.Context(), &message); err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusCreated, message)
}

func (ctrl *MessageController) GetMessage(c *gin.Context) {
    id := c.Param("id")
    objID, err := primitive.ObjectIDFromHex(id)
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid ID"})
        return
    }
    message, err := ctrl.service.GetMessageByID(c.Request.Context(), objID)
    if err != nil {
        c.JSON(http.StatusNotFound, gin.H{"error": "Message not found"})
        return
    }
    c.JSON(http.StatusOK, message)
}
