# High Throughput Event Processing System

Event-driven processing platform built with Python, AWS Lambda,
SQS, DynamoDB, retries, dead-letter queues, and observability.

## Problem

Designed to process large volumes of asynchronous business events
while ensuring reliability and fault tolerance.

## Architecture

Producer → SQS → Lambda Workers → DynamoDB

Dead Letter Queue → Monitoring Pipeline

## Results

- Processed 50,000+ events/day
- Reduced failed message loss through retry and DLQ strategy
- Automated asynchronous processing workflows
- Improved reliability through monitoring and observability

- ## Design Decisions

### Why SQS?
Provides decoupling between producers and consumers.

### Why Dead Letter Queues?
Prevents poison messages from blocking the queue.

### Why DynamoDB?
Low-latency event persistence at scale.
