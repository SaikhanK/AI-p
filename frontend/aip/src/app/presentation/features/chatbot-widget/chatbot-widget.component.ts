import { Component, ViewChild, ElementRef, AfterViewChecked } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { HttpClient, HttpParams } from '@angular/common/http';

interface ChatMessage {
  role: 'user' | 'bot';
  text: string;
  products?: RecommendedProduct[];
}

interface RecommendedProduct {
  id: number;
  title: string;
  price: number;
  category_name: string;
}

interface LlmResponse {
  answer: string;
  recommended_products: RecommendedProduct[];
}

@Component({
  selector: 'app-chatbot-widget',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './chatbot-widget.component.html',
  styleUrl: './chatbot-widget.component.css',
})
export class ChatbotWidgetComponent implements AfterViewChecked {
  @ViewChild('messageContainer') private messageContainer!: ElementRef;
  @ViewChild('inputField') private inputField!: ElementRef;

  isOpen = false;
  isLoading = false;
  hasUnread = false;
  inputText = '';

  messages: ChatMessage[] = [
    {
      role: 'bot',
      text: 'Hallo! Ich helfe dir gerne bei der Produktsuche. Was suchst du?',
    },
  ];

  constructor(private http: HttpClient) { }

  ngAfterViewChecked(): void {
    this.scrollToBottom();
  }

  toggleChat(): void {
    this.isOpen = !this.isOpen;
    if (this.isOpen) {
      this.hasUnread = false;
      setTimeout(() => this.inputField?.nativeElement.focus(), 150);
    }
  }

  sendMessage(): void {
    const text = this.inputText.trim();
    if (!text || this.isLoading) return;

    this.messages.push({ role: 'user', text });
    this.inputText = '';
    this.isLoading = true;

    const params = new HttpParams().set('user_input', text);

    this.http.get<LlmResponse>('http://localhost:8000/api/llm/', { params }).subscribe({
      next: (res) => {
        this.messages.push({
          role: 'bot',
          text: res.answer,
          products: res.recommended_products,
        });
        this.isLoading = false;
        if (!this.isOpen) this.hasUnread = true;
      },
      error: () => {
        this.messages.push({
          role: 'bot',
          text: 'Entschuldigung, da ist etwas schiefgelaufen. Bitte versuche es nochmal.',
        });
        this.isLoading = false;
      },
    });
  }

  private scrollToBottom(): void {
    try {
      const el = this.messageContainer?.nativeElement;
      if (el) el.scrollTop = el.scrollHeight;
    } catch { }
  }
}
