# Software Requirement Specification (SRS)

## Project Title

Smart Shoe Management App

## 1. Introduction

### 1.1 Purpose

The Smart Shoe Management App is designed to assist sneaker collectors, ranging from casual enthusiasts to serious "sneakerheads," in managing their shoe collections effectively. The app will provide features to track inventory, log wear use, send maintenance alerts, and display real-time market price data. This document outlines the complete technical and functional requirements for the scalable MVP version of the app.

### 1.2 Scope

- Manage personal sneaker inventory with detailed product information and photos
- Track shoe usage and provide cleaning reminders
- Display real-time sneaker pricing and market trends via integration with StockX and GOAT public APIs
- User authentication with email and Google login via Supabase Auth
- Scalable backend architecture to support up to 10,000 active users

### 1.3 Definitions, Acronyms, and Abbreviations

- MVP: Minimum Viable Product
- SKU: Stock Keeping Unit
- API: Application Programming Interface
- UI: User Interface
- UX: User Experience
- SRS: Software Requirement Specification

## 2. Overall Description

### 2.1 Product Perspective

The app is a new standalone mobile application developed using Flutter for cross-platform (iOS and Android) deployment. The backend will use Supabase and PostgreSQL for data management, authentication, and image storage.

### 2.2 User Needs

- Easy inventory management including adding shoes with details and photos
- Quick logging of wear usage
- Automated maintenance alerts to extend shoe lifespan
- Access to market price information to understand current value of collection
- Secure and simple authentication flow

### 2.3 Assumptions and Dependencies

- Integration with StockX and GOAT public APIs will be stable and reliable
- Users will have internet connectivity for real-time pricing and alerts
- Supabase services will be used for authentication, storage, and database

## 3. Functional Requirements

### 3.1 User Authentication

- Support email/password login
- Support Google login via Supabase Auth
- Provide user session management and secure data access

### 3.2 Inventory Management

- Allow users to add new shoes with fields:
    - Brand
    - Model
    - SKU
    - Purchase price
- Upload multiple high-resolution images per shoe with:
    - Automatic compression to optimize storage
    - Basic editing: cropping and rotating images
- View and edit shoe details

### 3.3 Wear Tracker

- On shoe detail page, provide a “Tap to Wear” button to log each usage
- Maintain and display a history of wear logs as a calendar view for each shoe

### 3.4 Cleaning Alerts

- Automatically track the number of wears per shoe
- Send push notifications for cleaning reminders every 10 wears
- Allow users to toggle cleaning alerts on or off globally or per shoe

### 3.5 Real-Time Market Pricing

- Integrate with StockX and GOAT public APIs to fetch sneaker price data
- Display current market price on the shoe detail page
- Present a 7-day price trend chart showing market price fluctuations

## 4. Non-Functional Requirements

### 4.1 Performance

- Backend capable of supporting up to 10,000 active users simultaneously
- Efficient handling of thousands of high-resolution images with fast load times
- Real-time fetching and updating of market price data with minimal latency

### 4.2 Scalability

- Design backend infrastructure to scale with user growth, utilizing Supabase and PostgreSQL capabilities

### 4.3 Security

- Secure authentication mechanisms via Supabase Auth
- Encrypted data transmission between client and server
- Proper access control to user data

### 4.4 Usability

- User-friendly and intuitive UI for both casual and serious sneaker collectors
- Cross-platform support through Flutter on iOS and Android

### 4.5 Availability

- Target 99.9% app and backend uptime

## 5. System Architecture

- Flutter mobile app for iOS and Android platforms
- Supabase backend services including:
    - PostgreSQL database for data storage
    - Storage service for images with compression
    - Authentication service (email and Google login)
- External API integrations with StockX and GOAT for market data retrieval

## 6. Constraints

- No fixed file size limit for photos but must implement automatic compression before upload
- Focus on scalable MVP; additional marketplace and social features planned beyond initial version
- Push notifications limited to cleaning alerts at present

## 7. Future Enhancements (Out of Scope for MVP)

- Marketplace feature for professional sellers to list shoes
- Social sharing and wishlist functionalities
- Additional authentication methods and integrations

This document comprehensively captures the technical and functional requirements for the Smart Shoe Management App MVP.
