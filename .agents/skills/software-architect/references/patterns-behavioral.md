# Design Patterns Reference

A practical reference for design patterns commonly used in Python and JavaScript/TypeScript projects. Focused on real-world usage, not academic theory.

---

## Behavioral Patterns

### Strategy

**Problem**: You have multiple algorithms for the same task and want to switch between them at runtime.

**When to use**:
- Different validation rules, sorting algorithms, or pricing calculations
- You need to swap behavior without changing the client
- Eliminating complex conditional logic (if/elif/else chains)

**Python**:
```python
from typing import Protocol

class PricingStrategy(Protocol):
    def calculate(self, base_price: float) -> float: ...

class RegularPricing:
    def calculate(self, base_price: float) -> float:
        return base_price

class PremiumDiscount:
    def calculate(self, base_price: float) -> float:
        return base_price * 0.8

class SeasonalSale:
    def __init__(self, discount_pct: float = 0.15):
        self.discount_pct = discount_pct

    def calculate(self, base_price: float) -> float:
        return base_price * (1 - self.discount_pct)

class Order:
    def __init__(self, pricing: PricingStrategy):
        self.pricing = pricing
        self.items: list[float] = []

    def total(self) -> float:
        return sum(self.pricing.calculate(p) for p in self.items)
```

**TypeScript**:
```typescript
interface PricingStrategy {
  calculate(basePrice: number): number;
}

const regularPricing: PricingStrategy = {
  calculate: (price) => price,
};

const premiumDiscount: PricingStrategy = {
  calculate: (price) => price * 0.8,
};

class Order {
  items: number[] = [];
  constructor(private pricing: PricingStrategy) {}

  total(): number {
    return this.items.reduce((sum, p) => sum + this.pricing.calculate(p), 0);
  }
}
```

**Pitfalls**:
- Overhead when you only have two strategies that never change
- Client must know about available strategies to select one
- Strategies sharing state can lead to subtle bugs

---

### Observer

**Problem**: You need to notify multiple objects when something changes, without tight coupling.

**When to use**:
- Event systems and pub/sub within an application
- UI components reacting to state changes
- Decoupling producers from consumers

**Python**:
```python
from typing import Callable

class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, list[Callable]] = {}

    def on(self, event: str, callback: Callable) -> None:
        self._listeners.setdefault(event, []).append(callback)

    def off(self, event: str, callback: Callable) -> None:
        if event in self._listeners:
            self._listeners[event].remove(callback)

    def emit(self, event: str, *args, **kwargs) -> None:
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)

# Usage
emitter = EventEmitter()
emitter.on("user:created", lambda user: print(f"Welcome {user}"))
emitter.on("user:created", lambda user: send_email(user))
emitter.emit("user:created", "Alice")
```

**TypeScript**:
```typescript
type Listener<T = unknown> = (data: T) => void;

class EventEmitter<Events extends Record<string, unknown>> {
  private listeners = new Map<keyof Events, Set<Listener>>();

  on<K extends keyof Events>(event: K, listener: Listener<Events[K]>): void {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, new Set());
    }
    this.listeners.get(event)!.add(listener as Listener);
  }

  off<K extends keyof Events>(event: K, listener: Listener<Events[K]>): void {
    this.listeners.get(event)?.delete(listener as Listener);
  }

  emit<K extends keyof Events>(event: K, data: Events[K]): void {
    this.listeners.get(event)?.forEach((listener) => listener(data));
  }
}

// Usage with type safety
interface AppEvents {
  "user:created": { id: string; name: string };
  "order:placed": { orderId: string; total: number };
}

const emitter = new EventEmitter<AppEvents>();
emitter.on("user:created", (user) => console.log(user.name));
```

**Pitfalls**:
- Memory leaks from unremoved listeners
- Cascading events causing infinite loops
- Debugging difficulty — hard to trace event flow
- Order of listener execution may matter but isn't guaranteed

---

### Command

**Problem**: You need to encapsulate operations as objects, enabling undo/redo, queuing, or logging.

**When to use**:
- Implementing undo/redo functionality
- Queuing and scheduling operations
- Macro recording and playback
- Transaction-like operations that may need rollback

**Python**:
```python
from typing import Protocol
from dataclasses import dataclass

class Command(Protocol):
    def execute(self) -> None: ...
    def undo(self) -> None: ...

@dataclass
class AddItemCommand:
    cart: list
    item: str

    def execute(self) -> None:
        self.cart.append(self.item)

    def undo(self) -> None:
        self.cart.remove(self.item)

class CommandHistory:
    def __init__(self):
        self._history: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo_last(self) -> None:
        if self._history:
            command = self._history.pop()
            command.undo()
```

**TypeScript**:
```typescript
interface Command {
  execute(): void;
  undo(): void;
}

class AddItemCommand implements Command {
  constructor(private cart: string[], private item: string) {}

  execute(): void {
    this.cart.push(this.item);
  }

  undo(): void {
    const index = this.cart.indexOf(this.item);
    if (index > -1) this.cart.splice(index, 1);
  }
}

class CommandHistory {
  private history: Command[] = [];

  execute(command: Command): void {
    command.execute();
    this.history.push(command);
  }

  undoLast(): void {
    const command = this.history.pop();
    command?.undo();
  }
}
```

**Pitfalls**:
- Overhead for simple operations that don't need undo
- Undo becoming complex when commands have side effects
- Memory growth if history isn't bounded

---

### State

**Problem**: An object's behavior changes based on its internal state, and you want to avoid large conditional blocks.

**When to use**:
- Object behavior varies significantly by state (e.g., order status, document workflow)
- State transitions have complex rules
- You want to make state-specific behavior explicit and testable

**Python**:
```python
from typing import Protocol

class OrderState(Protocol):
    def pay(self, order: "Order") -> None: ...
    def ship(self, order: "Order") -> None: ...
    def cancel(self, order: "Order") -> None: ...

class PendingState:
    def pay(self, order: "Order") -> None:
        print("Payment processed")
        order.state = PaidState()

    def ship(self, order: "Order") -> None:
        raise ValueError("Cannot ship unpaid order")

    def cancel(self, order: "Order") -> None:
        print("Order cancelled")
        order.state = CancelledState()

class PaidState:
    def pay(self, order: "Order") -> None:
        raise ValueError("Already paid")

    def ship(self, order: "Order") -> None:
        print("Order shipped")
        order.state = ShippedState()

    def cancel(self, order: "Order") -> None:
        print("Refund issued, order cancelled")
        order.state = CancelledState()

class ShippedState:
    def pay(self, order: "Order") -> None:
        raise ValueError("Already paid")

    def ship(self, order: "Order") -> None:
        raise ValueError("Already shipped")

    def cancel(self, order: "Order") -> None:
        raise ValueError("Cannot cancel shipped order")

class CancelledState:
    def pay(self, order: "Order") -> None:
        raise ValueError("Order is cancelled")

    def ship(self, order: "Order") -> None:
        raise ValueError("Order is cancelled")

    def cancel(self, order: "Order") -> None:
        raise ValueError("Already cancelled")

class Order:
    def __init__(self):
        self.state: OrderState = PendingState()

    def pay(self) -> None:
        self.state.pay(self)

    def ship(self) -> None:
        self.state.ship(self)

    def cancel(self) -> None:
        self.state.cancel(self)
```

**TypeScript**:
```typescript
interface OrderState {
  pay(order: Order): void;
  ship(order: Order): void;
  cancel(order: Order): void;
}

class PendingState implements OrderState {
  pay(order: Order): void {
    console.log("Payment processed");
    order.state = new PaidState();
  }
  ship(_order: Order): void {
    throw new Error("Cannot ship unpaid order");
  }
  cancel(order: Order): void {
    console.log("Order cancelled");
    order.state = new CancelledState();
  }
}

// ... PaidState, ShippedState, CancelledState follow the same pattern

class Order {
  state: OrderState = new PendingState();

  pay(): void { this.state.pay(this); }
  ship(): void { this.state.ship(this); }
  cancel(): void { this.state.cancel(this); }
}
```

**Pitfalls**:
- Over-engineering for simple state machines with 2-3 states
- States accumulating business logic that belongs elsewhere
- Difficulty tracking state transitions without logging

---

## Architectural Patterns

### Repository

**Problem**: You need to abstract data access logic from business logic, providing a collection-like interface for domain objects.

**When to use**:
- Decoupling business logic from database specifics
- You need to swap storage backends (SQL → NoSQL, in-memory for tests)
- Centralizing query logic for a domain entity

**Python**:
```python
from typing import Protocol
from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    email: str

class UserRepository(Protocol):
    def get_by_id(self, user_id: str) -> User | None: ...
    def get_by_email(self, email: str) -> User | None: ...
    def save(self, user: User) -> None: ...
    def delete(self, user_id: str) -> None: ...
    def list_all(self, limit: int = 100, offset: int = 0) -> list[User]: ...

class SQLUserRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_by_id(self, user_id: str) -> User | None:
        row = self.db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        return User(**row) if row else None

    def save(self, user: User) -> None:
        self.db.execute(
            "INSERT OR REPLACE INTO users (id, name, email) VALUES (?, ?, ?)",
            (user.id, user.name, user.email),
        )
    # ... other methods

class InMemoryUserRepository:
    """For testing."""
    def __init__(self):
        self._store: dict[str, User] = {}

    def get_by_id(self, user_id: str) -> User | None:
        return self._store.get(user_id)

    def save(self, user: User) -> None:
        self._store[user.id] = user
    # ... other methods
```

**TypeScript**:
```typescript
interface UserRepository {
  getById(id: string): Promise<User | null>;
  getByEmail(email: string): Promise<User | null>;
  save(user: User): Promise<void>;
  delete(id: string): Promise<void>;
}

class PrismaUserRepository implements UserRepository {
  constructor(private prisma: PrismaClient) {}

  async getById(id: string): Promise<User | null> {
    return this.prisma.user.findUnique({ where: { id } });
  }

  async save(user: User): Promise<void> {
    await this.prisma.user.upsert({
      where: { id: user.id },
      update: user,
      create: user,
    });
  }
  // ... other methods
}
```

**Pitfalls**:
- Leaking ORM/database concepts into the repository interface
- Repositories growing too many query methods (consider CQRS for read-heavy apps)
- Ignoring transactions when multiple repositories need coordination

---

### Unit of Work

**Problem**: You need to track changes to multiple entities and commit them atomically as a single transaction.

**When to use**:
- Multiple repositories need to be coordinated in a single transaction
- You want to batch database operations for performance
- Ensuring consistency across related changes

**Python**:
```python
class UnitOfWork:
    def __init__(self, session_factory):
        self._session_factory = session_factory

    def __enter__(self):
        self.session = self._session_factory()
        self.users = SQLUserRepository(self.session)
        self.orders = SQLOrderRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

# Usage
with UnitOfWork(session_factory) as uow:
    user = uow.users.get_by_id("123")
    uow.orders.save(Order(user_id=user.id, total=99.99))
    uow.commit()
```

**Pitfalls**:
- Overly complex UoW for simple CRUD applications
- Long-lived units of work holding database locks
- Forgetting to call `commit()` — changes are silently lost

---

### Service Layer

**Problem**: You need to orchestrate business operations that span multiple domain objects and repositories.

**When to use**:
- Business logic involves coordinating multiple repositories or external services
- You need a clear API layer for your application's use cases
- Separating "what to do" (service) from "how to store" (repository)

**Python**:
```python
class UserService:
    def __init__(self, user_repo: UserRepository, email_service: EmailService):
        self.user_repo = user_repo
        self.email_service = email_service

    def register_user(self, name: str, email: str) -> User:
        existing = self.user_repo.get_by_email(email)
        if existing:
            raise ValueError(f"Email {email} already registered")

        user = User(id=generate_id(), name=name, email=email)
        self.user_repo.save(user)
        self.email_service.send_welcome(user)
        return user

    def deactivate_user(self, user_id: str) -> None:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        user.active = False
        self.user_repo.save(user)
```

**Pitfalls**:
- Services becoming "god classes" with too many methods
- Business logic leaking into controllers/handlers instead of the service
- Circular dependencies between services

<!-- APPEND HERE -->
