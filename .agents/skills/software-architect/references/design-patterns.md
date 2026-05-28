# Design Patterns Reference

A practical reference for design patterns commonly used in Python and JavaScript/TypeScript projects. Focused on real-world usage, not academic theory.

---

## Creational Patterns

### Factory

**Problem**: You need to create objects without specifying the exact class, or you want to centralize complex creation logic.

**When to use**:
- Object creation involves logic beyond simple instantiation
- You need to return different subtypes based on input
- You want to decouple client code from concrete classes

**Python**:
```python
from typing import Protocol

class Notifier(Protocol):
    def send(self, message: str) -> None: ...

class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SlackNotifier:
    def send(self, message: str) -> None:
        print(f"Slack: {message}")

def create_notifier(channel: str) -> Notifier:
    notifiers = {
        "email": EmailNotifier,
        "slack": SlackNotifier,
    }
    if channel not in notifiers:
        raise ValueError(f"Unknown channel: {channel}")
    return notifiers[channel]()
```

**TypeScript**:
```typescript
interface Notifier {
  send(message: string): void;
}

class EmailNotifier implements Notifier {
  send(message: string): void {
    console.log(`Email: ${message}`);
  }
}

class SlackNotifier implements Notifier {
  send(message: string): void {
    console.log(`Slack: ${message}`);
  }
}

function createNotifier(channel: "email" | "slack"): Notifier {
  const notifiers = {
    email: () => new EmailNotifier(),
    slack: () => new SlackNotifier(),
  };
  return notifiers[channel]();
}
```

**Pitfalls**:
- Over-abstracting when you only have one implementation
- Creating a factory for objects that don't need polymorphism
- Factories that grow into god-objects with too many creation methods

---

### Builder

**Problem**: You need to construct complex objects step-by-step, especially when the constructor would have many parameters.

**When to use**:
- Object has many optional configuration parameters
- Construction requires multiple steps or validation
- You want to create different representations of the same object

**Python**:
```python
from dataclasses import dataclass, field

@dataclass
class QueryBuilder:
    _table: str = ""
    _conditions: list[str] = field(default_factory=list)
    _order_by: str | None = None
    _limit: int | None = None

    def table(self, name: str) -> "QueryBuilder":
        self._table = name
        return self

    def where(self, condition: str) -> "QueryBuilder":
        self._conditions.append(condition)
        return self

    def order(self, column: str) -> "QueryBuilder":
        self._order_by = column
        return self

    def limit(self, n: int) -> "QueryBuilder":
        self._limit = n
        return self

    def build(self) -> str:
        query = f"SELECT * FROM {self._table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._order_by:
            query += f" ORDER BY {self._order_by}"
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query

# Usage
query = (
    QueryBuilder()
    .table("users")
    .where("active = true")
    .where("age > 18")
    .order("created_at")
    .limit(10)
    .build()
)
```

**TypeScript**:
```typescript
class QueryBuilder {
  private _table = "";
  private _conditions: string[] = [];
  private _orderBy?: string;
  private _limit?: number;

  table(name: string): this {
    this._table = name;
    return this;
  }

  where(condition: string): this {
    this._conditions.push(condition);
    return this;
  }

  order(column: string): this {
    this._orderBy = column;
    return this;
  }

  limit(n: number): this {
    this._limit = n;
    return this;
  }

  build(): string {
    let query = `SELECT * FROM ${this._table}`;
    if (this._conditions.length > 0) {
      query += ` WHERE ${this._conditions.join(" AND ")}`;
    }
    if (this._orderBy) query += ` ORDER BY ${this._orderBy}`;
    if (this._limit) query += ` LIMIT ${this._limit}`;
    return query;
  }
}
```

**Pitfalls**:
- Using a builder when a simple constructor or config object suffices
- Forgetting to validate required fields in `build()`
- Making builders mutable when they should produce immutable objects

---

### Singleton (Use with Caution)

**Problem**: You need exactly one instance of a class, typically for shared resources like configuration, connection pools, or loggers.

**When to use**:
- Managing a shared resource that must not be duplicated (e.g., DB connection pool)
- Global configuration that is read-only after initialization
- **Prefer dependency injection over singletons in most cases**

**Python**:
```python
# Preferred: module-level instance (Python's natural singleton)
# config.py
class _Config:
    def __init__(self) -> None:
        self.debug = False
        self.db_url = ""

    def load(self, **kwargs: object) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

config = _Config()  # Module-level — imported as a singleton

# Usage: from config import config
```

**TypeScript**:
```typescript
// Preferred: module-level instance
class Config {
  debug = false;
  dbUrl = "";

  load(options: Partial<Config>): void {
    Object.assign(this, options);
  }
}

export const config = new Config();
```

**Pitfalls**:
- Hidden global state that makes testing difficult
- Thread-safety issues in concurrent environments
- Tight coupling — components depend on the global instance
- **Prefer DI containers** in production applications

---

## Structural Patterns

### Adapter

**Problem**: You need to make incompatible interfaces work together without modifying existing code.

**When to use**:
- Integrating a third-party library with a different interface
- Migrating from one service/library to another
- Wrapping legacy code with a modern interface

**Python**:
```python
from typing import Protocol

class PaymentGateway(Protocol):
    def charge(self, amount_cents: int, currency: str) -> dict: ...

class StripeAdapter:
    """Adapts Stripe SDK to our PaymentGateway interface."""
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def charge(self, amount_cents: int, currency: str) -> dict:
        # Wraps stripe.PaymentIntent.create(...)
        return {"id": "pi_xxx", "status": "succeeded", "amount": amount_cents}

class PayPalAdapter:
    """Adapts PayPal SDK to our PaymentGateway interface."""
    def __init__(self, client_id: str, secret: str) -> None:
        self.client_id = client_id
        self.secret = secret

    def charge(self, amount_cents: int, currency: str) -> dict:
        amount_dollars = amount_cents / 100
        return {"id": "PAY-xxx", "status": "approved", "amount": amount_dollars}
```

**TypeScript**:
```typescript
interface PaymentGateway {
  charge(amountCents: number, currency: string): Promise<PaymentResult>;
}

interface PaymentResult {
  id: string;
  status: string;
  amount: number;
}

class StripeAdapter implements PaymentGateway {
  constructor(private apiKey: string) {}

  async charge(amountCents: number, currency: string): Promise<PaymentResult> {
    // Wraps Stripe API call
    return { id: "pi_xxx", status: "succeeded", amount: amountCents };
  }
}
```

**Pitfalls**:
- Creating adapters when you control both interfaces (just change one)
- Leaking abstraction details from the adapted library
- Over-adapting — adding logic beyond simple interface translation

---

### Decorator

**Problem**: You need to add behavior to objects dynamically without modifying their class.

**When to use**:
- Adding cross-cutting concerns (logging, caching, retry, auth)
- Composing behaviors at runtime
- Extending functionality without subclassing

**Python**:
```python
import functools
import time
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

def retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator that retries a function on failure."""
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_error: Exception | None = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
            raise last_error  # type: ignore
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url: str) -> dict:
    # ... HTTP request
    pass
```

**TypeScript**:
```typescript
function withRetry<T>(
  fn: (...args: unknown[]) => Promise<T>,
  maxAttempts = 3,
  delay = 1000
): (...args: unknown[]) => Promise<T> {
  return async (...args) => {
    let lastError: Error | undefined;
    for (let attempt = 0; attempt < maxAttempts; attempt++) {
      try {
        return await fn(...args);
      } catch (error) {
        lastError = error as Error;
        if (attempt < maxAttempts - 1) {
          await new Promise((r) => setTimeout(r, delay * 2 ** attempt));
        }
      }
    }
    throw lastError;
  };
}
```

**Pitfalls**:
- Stacking too many decorators — makes debugging hard
- Order dependency between decorators
- Losing function signatures and type information (use `functools.wraps` in Python)

---

### Facade

**Problem**: You need a simplified interface to a complex subsystem with many interacting parts.

**When to use**:
- Hiding complexity of a multi-step process
- Providing a high-level API for a library or subsystem
- Reducing coupling between client code and subsystem internals

**Python**:
```python
class DeploymentFacade:
    """Simplifies the multi-step deployment process."""
    def __init__(self, builder, tester, deployer, notifier):
        self.builder = builder
        self.tester = tester
        self.deployer = deployer
        self.notifier = notifier

    def deploy(self, version: str) -> bool:
        artifact = self.builder.build(version)
        if not self.tester.run_tests(artifact):
            self.notifier.send("Tests failed")
            return False
        self.deployer.deploy(artifact)
        self.notifier.send(f"v{version} deployed successfully")
        return True
```

**TypeScript**:
```typescript
class DeploymentFacade {
  constructor(
    private builder: Builder,
    private tester: Tester,
    private deployer: Deployer,
    private notifier: Notifier
  ) {}

  async deploy(version: string): Promise<boolean> {
    const artifact = await this.builder.build(version);
    if (!(await this.tester.runTests(artifact))) {
      await this.notifier.send("Tests failed");
      return false;
    }
    await this.deployer.deploy(artifact);
    await this.notifier.send(`v${version} deployed successfully`);
    return true;
  }
}
```

**Pitfalls**:
- Facade becoming a god object that does too much
- Hiding important configuration that clients need access to
- Not providing escape hatches for advanced use cases

---

### Proxy

**Problem**: You need to control access to an object, add lazy initialization, caching, or access control.

**When to use**:
- Lazy loading expensive resources
- Adding access control or permission checks
- Caching expensive operation results
- Logging/auditing access to an object

**Python**:
```python
class CachedRepository:
    """Proxy that caches results from the underlying repository."""
    def __init__(self, repo, cache_ttl: int = 300):
        self._repo = repo
        self._cache: dict[str, tuple[float, object]] = {}
        self._ttl = cache_ttl

    def get(self, id: str):
        import time
        if id in self._cache:
            timestamp, value = self._cache[id]
            if time.time() - timestamp < self._ttl:
                return value
        value = self._repo.get(id)
        self._cache[id] = (time.time(), value)
        return value
```

**TypeScript**:
```typescript
class CachedRepository<T> {
  private cache = new Map<string, { timestamp: number; value: T }>();

  constructor(
    private repo: { get(id: string): Promise<T> },
    private ttlMs: number = 300_000
  ) {}

  async get(id: string): Promise<T> {
    const cached = this.cache.get(id);
    if (cached && Date.now() - cached.timestamp < this.ttlMs) {
      return cached.value;
    }
    const value = await this.repo.get(id);
    this.cache.set(id, { timestamp: Date.now(), value });
    return value;
  }
}
```

**Pitfalls**:
- Cache invalidation complexity ("the hardest problem in CS")
- Proxy hiding important errors from the underlying object
- Adding too many responsibilities to a single proxy

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

---

### Dependency Injection

**Problem**: You need to decouple object creation from usage, making components testable and configurable.

**When to use**:
- Always — DI is a fundamental design principle, not just a pattern
- Any class that depends on external services, repositories, or configuration
- When you need to swap implementations for testing

**Python**:
```python
# Manual DI (preferred for small-medium projects)
def create_app() -> App:
    db = Database(url=config.db_url)
    user_repo = SQLUserRepository(db)
    email_service = SMTPEmailService(config.smtp_host)
    user_service = UserService(user_repo, email_service)
    return App(user_service=user_service)

# For larger projects, consider a lightweight container:
from dataclasses import dataclass

@dataclass
class Container:
    """Simple DI container — just a factory with named dependencies."""
    config: Config

    @property
    def db(self) -> Database:
        return Database(self.config.db_url)

    @property
    def user_repo(self) -> UserRepository:
        return SQLUserRepository(self.db)

    @property
    def user_service(self) -> UserService:
        return UserService(self.user_repo, self.email_service)
```

**TypeScript**:
```typescript
// Manual DI with factory function
function createApp(config: AppConfig) {
  const db = new Database(config.dbUrl);
  const userRepo = new PrismaUserRepository(db);
  const emailService = new SendGridEmailService(config.sendgridKey);
  const userService = new UserService(userRepo, emailService);
  return new App(userService);
}

// For larger projects, consider inversify or tsyringe
```

**Pitfalls**:
- Over-engineering with full DI frameworks for small projects
- Deep dependency chains that are hard to trace
- Registering everything as singletons when request-scoped is appropriate

---

### Middleware Pipeline

**Problem**: You need to process requests through a chain of handlers, each adding a concern (auth, logging, validation).

**When to use**:
- HTTP request/response processing
- Message processing pipelines
- Any pipeline where cross-cutting concerns need to be applied in order

**Python**:
```python
from typing import Callable

Middleware = Callable[[dict, Callable], dict]

def logging_middleware(request: dict, next_handler: Callable) -> dict:
    print(f"→ {request['method']} {request['path']}")
    response = next_handler(request)
    print(f"← {response['status']}")
    return response

def auth_middleware(request: dict, next_handler: Callable) -> dict:
    if "authorization" not in request.get("headers", {}):
        return {"status": 401, "body": "Unauthorized"}
    return next_handler(request)

class Pipeline:
    def __init__(self, handler: Callable):
        self._handler = handler

    def use(self, middleware: Middleware) -> "Pipeline":
        inner = self._handler
        self._handler = lambda req: middleware(req, inner)
        return self

    def handle(self, request: dict) -> dict:
        return self._handler(request)
```

**TypeScript**:
```typescript
type Middleware = (
  req: Request,
  next: () => Promise<Response>
) => Promise<Response>;

function loggingMiddleware(): Middleware {
  return async (req, next) => {
    console.log(`→ ${req.method} ${req.url}`);
    const response = await next();
    console.log(`← ${response.status}`);
    return response;
  };
}

function authMiddleware(): Middleware {
  return async (req, next) => {
    if (!req.headers.get("authorization")) {
      return new Response("Unauthorized", { status: 401 });
    }
    return next();
  };
}
```

**Pitfalls**:
- Middleware order dependencies not being documented
- Error handling gaps between middleware layers
- Performance overhead from deeply nested middleware chains

---

### Pub/Sub (Publish/Subscribe)

**Problem**: You need to broadcast events to multiple subscribers without the publisher knowing who the subscribers are.

**When to use**:
- Decoupling components that react to events
- Implementing eventual consistency across bounded contexts
- Background task triggering (email, notifications, analytics)

**Python**:
```python
import asyncio
from typing import Callable, Any
from collections import defaultdict

class MessageBus:
    def __init__(self):
        self._handlers: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable) -> None:
        self._handlers[event_type].append(handler)

    async def publish(self, event_type: str, data: Any) -> None:
        handlers = self._handlers.get(event_type, [])
        await asyncio.gather(*(h(data) for h in handlers))

# Usage
bus = MessageBus()
bus.subscribe("order.created", send_confirmation_email)
bus.subscribe("order.created", update_inventory)
bus.subscribe("order.created", notify_warehouse)

await bus.publish("order.created", {"order_id": "123", "total": 99.99})
```

**TypeScript**:
```typescript
type Handler<T = unknown> = (data: T) => Promise<void>;

class MessageBus {
  private handlers = new Map<string, Set<Handler>>();

  subscribe<T>(eventType: string, handler: Handler<T>): () => void {
    if (!this.handlers.has(eventType)) {
      this.handlers.set(eventType, new Set());
    }
    const handlerSet = this.handlers.get(eventType)!;
    handlerSet.add(handler as Handler);

    // Return unsubscribe function
    return () => handlerSet.delete(handler as Handler);
  }

  async publish<T>(eventType: string, data: T): Promise<void> {
    const handlers = this.handlers.get(eventType);
    if (handlers) {
      await Promise.all([...handlers].map((h) => h(data)));
    }
  }
}
```

**Pitfalls**:
- Lost events if a subscriber is down (consider persistent message queues for reliability)
- Debugging difficulty — hard to trace the full event flow
- Event schema evolution — changes to event data break subscribers
- No guaranteed delivery order

---

## Data Access Patterns

### Repository

**Problem**: You need to abstract data access logic and decouple business logic from the persistence layer.

**When to use**:
- Any project with a database or external storage
- When you want to test business logic without a real database
- When you might switch storage technology (e.g., from PostgreSQL to MongoDB)

**Python**:
```python
from typing import Protocol
from uuid import UUID

class UserRepository(Protocol):
    def find_by_id(self, user_id: UUID) -> "User | None": ...
    def find_by_email(self, email: str) -> "User | None": ...
    def save(self, user: "User") -> None: ...
    def delete(self, user_id: UUID) -> None: ...

# SQLAlchemy implementation
class SQLUserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def find_by_id(self, user_id: UUID) -> "User | None":
        return self._session.get(UserModel, user_id)

    def find_by_email(self, email: str) -> "User | None":
        return self._session.scalar(
            select(UserModel).where(UserModel.email == email)
        )

    def save(self, user: "User") -> None:
        self._session.merge(user)

    def delete(self, user_id: UUID) -> None:
        user = self._session.get(UserModel, user_id)
        if user:
            self._session.delete(user)

# In-memory implementation (for tests)
class InMemoryUserRepository:
    def __init__(self) -> None:
        self._store: dict[UUID, "User"] = {}

    def find_by_id(self, user_id: UUID) -> "User | None":
        return self._store.get(user_id)

    def find_by_email(self, email: str) -> "User | None":
        return next((u for u in self._store.values() if u.email == email), None)

    def save(self, user: "User") -> None:
        self._store[user.id] = user

    def delete(self, user_id: UUID) -> None:
        self._store.pop(user_id, None)
```

**TypeScript**:
```typescript
interface UserRepository {
  findById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
  save(user: User): Promise<void>;
  delete(id: string): Promise<void>;
}

// Prisma implementation
class PrismaUserRepository implements UserRepository {
  constructor(private prisma: PrismaClient) {}

  async findById(id: string): Promise<User | null> {
    return this.prisma.user.findUnique({ where: { id } });
  }

  async findByEmail(email: string): Promise<User | null> {
    return this.prisma.user.findUnique({ where: { email } });
  }

  async save(user: User): Promise<void> {
    await this.prisma.user.upsert({
      where: { id: user.id },
      create: user,
      update: user,
    });
  }

  async delete(id: string): Promise<void> {
    await this.prisma.user.delete({ where: { id } });
  }
}

// In-memory (for tests)
class InMemoryUserRepository implements UserRepository {
  private store = new Map<string, User>();

  async findById(id: string): Promise<User | null> {
    return this.store.get(id) ?? null;
  }

  async findByEmail(email: string): Promise<User | null> {
    return [...this.store.values()].find((u) => u.email === email) ?? null;
  }

  async save(user: User): Promise<void> {
    this.store.set(user.id, user);
  }

  async delete(id: string): Promise<void> {
    this.store.delete(id);
  }
}
```

**Pitfalls**:
- Fat repositories that accumulate query logic — use Specification pattern for complex queries
- Repository returning domain objects coupled to ORM models — use mappers to separate them
- Testing with a real DB when InMemory would suffice

---

### Unit of Work

**Problem**: You need to coordinate multiple repository operations within a single transaction boundary.

**When to use**:
- Operations that span multiple repositories must succeed or fail atomically
- Avoiding partial writes that leave data in inconsistent state
- When you need to track changes and commit them together

**Python**:
```python
from contextlib import contextmanager
from typing import Generator

class UnitOfWork:
    def __init__(self, session_factory) -> None:
        self._session_factory = session_factory

    def __enter__(self) -> "UnitOfWork":
        self._session = self._session_factory()
        self.users = SQLUserRepository(self._session)
        self.orders = SQLOrderRepository(self._session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            self._session.rollback()
        self._session.close()

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()

# Usage
def transfer_order(uow: UnitOfWork, from_user_id: str, to_user_id: str, order_id: str):
    with uow:
        order = uow.orders.find_by_id(order_id)
        order.owner_id = to_user_id
        uow.orders.save(order)
        uow.commit()  # Atomic — both changes or neither
```

**TypeScript**:
```typescript
interface UnitOfWork {
  users: UserRepository;
  orders: OrderRepository;
  commit(): Promise<void>;
  rollback(): Promise<void>;
}

class PrismaUnitOfWork implements UnitOfWork {
  users: UserRepository;
  orders: OrderRepository;

  constructor(private prisma: PrismaClient) {
    this.users = new PrismaUserRepository(prisma);
    this.orders = new PrismaOrderRepository(prisma);
  }

  async commit(): Promise<void> {
    // Prisma batches writes automatically within a transaction
    await this.prisma.$transaction(async (tx) => {
      // operations are committed here
    });
  }

  async rollback(): Promise<void> {
    // handled by Prisma transaction
  }
}
```

**Pitfalls**:
- Long-lived units of work holding database connections
- Forgetting to call commit() — changes are silently rolled back
- Nested units of work creating unexpected transaction boundaries

---

### Middleware / Pipeline

**Problem**: You need to add cross-cutting concerns (auth, logging, rate limiting, validation) to a request/response flow without cluttering the core handlers.

**When to use**:
- HTTP request processing (Express, Fastify, FastAPI)
- Message/event processing pipelines
- Command/query handling with decorators
- Any chain of responsibility where each step can short-circuit

**Python** (FastAPI middleware):
```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RequestTimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start
        response.headers["X-Process-Time"] = f"{duration:.4f}s"
        return response

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if not token and not request.url.path.startswith("/public"):
            return JSONResponse({"error": "Unauthorized"}, status_code=401)
        return await call_next(request)

app.add_middleware(RequestTimingMiddleware)
app.add_middleware(AuthMiddleware)
```

**TypeScript** (Express-style pipeline):
```typescript
type Middleware<T> = (ctx: T, next: () => Promise<void>) => Promise<void>;

class Pipeline<T> {
  private middlewares: Middleware<T>[] = [];

  use(middleware: Middleware<T>): this {
    this.middlewares.push(middleware);
    return this;
  }

  async execute(ctx: T): Promise<void> {
    const run = async (index: number): Promise<void> => {
      if (index >= this.middlewares.length) return;
      await this.middlewares[index](ctx, () => run(index + 1));
    };
    await run(0);
  }
}

// Usage
const pipeline = new Pipeline<RequestContext>()
  .use(authMiddleware)
  .use(rateLimitMiddleware)
  .use(loggingMiddleware)
  .use(validationMiddleware);

await pipeline.execute(requestContext);
```

**Pitfalls**:
- Order of middleware matters — auth before business logic, logging around everything
- Silent swallowing of next() — forgetting to call next stops the pipeline
- Shared mutable context between middlewares causing subtle bugs

---

## Architectural Patterns

### CQRS (Command Query Responsibility Segregation)

**Problem**: Read and write operations have different scaling needs, complexity, and consistency requirements.

**When to use**:
- Read-heavy applications where query optimization is critical
- Complex domain logic that differs significantly between reads and writes
- Event-sourced systems
- When you need different consistency guarantees for reads vs. writes

**Python**:
```python
from dataclasses import dataclass
from typing import Protocol

# Commands (write side) — return None, cause side effects
@dataclass
class CreateOrderCommand:
    user_id: str
    item_ids: list[str]
    shipping_address: str

class CreateOrderHandler:
    def __init__(self, repo: OrderRepository, event_bus: EventBus) -> None:
        self.repo = repo
        self.event_bus = event_bus

    def handle(self, cmd: CreateOrderCommand) -> str:
        order = Order.create(cmd.user_id, cmd.item_ids, cmd.shipping_address)
        self.repo.save(order)
        self.event_bus.publish("order.created", order.to_dict())
        return order.id

# Queries (read side) — return data, no side effects
@dataclass
class GetUserOrdersQuery:
    user_id: str
    page: int = 1
    page_size: int = 20

@dataclass
class OrderSummary:
    id: str
    status: str
    total: float
    created_at: str

class GetUserOrdersHandler:
    def __init__(self, db) -> None:
        self.db = db

    def handle(self, query: GetUserOrdersQuery) -> list[OrderSummary]:
        # Direct SQL for read — optimized, denormalized, no ORM overhead
        rows = self.db.execute("""
            SELECT o.id, o.status, o.total, o.created_at
            FROM orders o
            WHERE o.user_id = %s
            ORDER BY o.created_at DESC
            LIMIT %s OFFSET %s
        """, (query.user_id, query.page_size, (query.page - 1) * query.page_size))
        return [OrderSummary(**row) for row in rows]
```

**TypeScript**:
```typescript
// Command bus
interface Command {}
interface CommandHandler<TCommand extends Command, TResult = void> {
  handle(command: TCommand): Promise<TResult>;
}

class CreateOrderCommand implements Command {
  constructor(
    public readonly userId: string,
    public readonly itemIds: string[],
  ) {}
}

class CreateOrderHandler implements CommandHandler<CreateOrderCommand, string> {
  constructor(private repo: OrderRepository) {}

  async handle(command: CreateOrderCommand): Promise<string> {
    const order = Order.create(command.userId, command.itemIds);
    await this.repo.save(order);
    return order.id;
  }
}

// Query bus — optimized read side
interface Query<TResult> {}

class GetUserOrdersQuery implements Query<OrderSummary[]> {
  constructor(public readonly userId: string, public readonly page = 1) {}
}
```

**Pitfalls**:
- Overkill for simple CRUD — adds complexity without benefit
- Eventual consistency in distributed CQRS (read model may lag behind write model)
- Keeping read models in sync with write model requires care

---

### Dependency Injection Container

**Problem**: Wiring up complex object graphs manually is tedious and couples your bootstrapping code to concrete implementations.

**When to use**:
- Applications with many interdependent services
- When you want to swap implementations easily (e.g., real vs. fake in tests)
- When managing object lifecycles (singleton, per-request, transient)

**Python** (using `dependency-injector`):
```python
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Infrastructure
    db_session = providers.Resource(create_session, url=config.database_url)

    # Repositories
    user_repo = providers.Factory(SQLUserRepository, session=db_session)
    order_repo = providers.Factory(SQLOrderRepository, session=db_session)

    # Services
    email_service = providers.Singleton(SmtpEmailService, smtp_url=config.smtp_url)
    user_service = providers.Factory(
        UserService,
        repo=user_repo,
        email=email_service,
    )

# Usage in FastAPI
@app.post("/users")
@inject
async def create_user(
    body: CreateUserRequest,
    service: UserService = Depends(Provide[Container.user_service]),
):
    return service.create(body.email, body.password)

# Bootstrap
container = Container()
container.config.from_yaml("config.yml")
container.wire(modules=[__name__])
```

**TypeScript** (manual DI container):
```typescript
class Container {
  private _instances = new Map<string, unknown>();

  register<T>(token: string, factory: () => T, singleton = true): void {
    if (singleton) {
      this._instances.set(token, factory());
    } else {
      // Store factory for transient instances
      this._instances.set(`factory:${token}`, factory);
    }
  }

  resolve<T>(token: string): T {
    if (this._instances.has(token)) {
      return this._instances.get(token) as T;
    }
    const factory = this._instances.get(`factory:${token}`) as () => T;
    if (!factory) throw new Error(`No binding found for token: ${token}`);
    return factory();
  }
}

// Bootstrap
const container = new Container();
container.register("db", () => new PrismaClient());
container.register("userRepo", () =>
  new PrismaUserRepository(container.resolve("db"))
);
container.register("userService", () =>
  new UserService(container.resolve("userRepo"))
);

// Resolve
const userService = container.resolve<UserService>("userService");
```

**Pitfalls**:
- Container becoming a service locator (anti-pattern) — prefer constructor injection
- Circular dependencies causing infinite loops at startup
- Over-engineering for small applications — manual wiring is fine for < 10 services
- Hidden dependencies — container obscures what a class actually needs
