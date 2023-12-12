const dbName = 'hotelDB';
const dbVersion = 1;
const roomStoreName = 'rooms';
const guestStoreName = 'guests';

let db;

const request = indexedDB.open(dbName, dbVersion);

request.onerror = (event) => {
    console.error("Błąd połączenia:", event.target.error);
};

request.onupgradeneeded = (event) => {
    db = event.target.result;

    const roomStore = db.createObjectStore(roomStoreName, { keyPath: 'number' });
    const guestStore = db.createObjectStore(guestStoreName, { autoIncrement: true });

    //indeksy
    roomStore.createIndex('availability', 'availability', { unique: false });
    guestStore.createIndex('fullName', ['firstName', 'lastName'], { unique: true });

    for (let i = 1; i <= 4; i++) {
        const room = { number: i, availability: Math.floor(Math.random() * 5)+1, guests: [] };
        roomStore.add(room);
    }

    const guests = [
        { firstName: 'Jan', lastName: 'Kowalski' },
        { firstName: 'Andrzej', lastName: 'Nowak' }
    ];

    guests.forEach((guest) => {
        guestStore.add(guest);
    });

    console.log("Utworzono baze danych", db)
};

request.onsuccess = (event) => {
    db = event.target.result;
    console.log("Połączono z bazą danych");
};

function executeCommand() {
    const commandInput = document.getElementById('cmd-line').value.trim();
    const commandArray = commandInput.split(' ');

    const command = commandArray[0];
    const params = commandArray.slice(1);

    switch (command.toLowerCase()) {
        case 'book':
            bookRoom(params);
            break;
        case 'guests':
            displayGuests();
            break;
        case 'status':
            displayHotelStatus();
            break;
        default:
            console.error("Nieznana komenda");
    }
}

function bookRoom(params) {
    const roomNumber = parseInt(params[0]);
    const guestFullName = params.slice(1);

    const transaction = db.transaction([roomStoreName, guestStoreName], 'readwrite');
    const roomStore = transaction.objectStore(roomStoreName);
    const guestStore = transaction.objectStore(guestStoreName);

    const roomRequest = roomStore.get(roomNumber);

    roomRequest.onsuccess = () => {
        const room = roomRequest.result;

        if (room) {
        if (room.availability > 0) {
            const guestRequest = guestStore.index('fullName').get(guestFullName);

            guestRequest.onsuccess = () => {
                const guest = guestRequest.result;

                if (!guest) {
                    console.error("Nie znaleziono gościa, utworzono nowego");
                    guestStore.add({
                        firstName: params[1],
                        lastName: params[2]
                        })
                }
                
                console.group("Wynajem pokoju");
                console.log(`Pokój ${roomNumber} został wynajęty ${guestFullName}`);
                console.groupEnd();

                room.availability -= 1;
                room.guests.push(guestFullName)
                roomStore.put(room);
            };

            guestRequest.onerror = (event) => {
                console.error("Błąd przy pobieraniu gościa:", event.target.error);
            };
        }else{
            console.warn("Nie można zakwaterować do pełnego pytania")
        }
        } else {
            console.warn("Pokój nie istnieje");
        }
    };

    roomRequest.onerror = (event) => {
        console.error("Error fetching room:", event.target.error);
    };

    transaction.onerror = (event) => {
        console.error("Transaction error:", event.target.error);
    };
}

function displayGuests() {
    const transaction = db.transaction([guestStoreName, roomStoreName], 'readonly');
    const guestStore = transaction.objectStore(guestStoreName);
    const roomStore = transaction.objectStore(roomStoreName);

    const roomCursorRequest = roomStore.openCursor();
    let roomGuestPairs = {}
    roomCursorRequest.onsuccess = (event) => {
        const cursor = event.target.result;

        if(cursor){
            cursor.value.guests.forEach(item => {
                roomGuestPairs[item] = cursor.key;
            })
            cursor.continue();
        }
    }

    const cursorRequest = guestStore.openCursor();

    console.group("Lista gości");
    cursorRequest.onsuccess = (event) => {
        const cursor = event.target.result;

        if (cursor) {
            console.log(`Id: ${cursor.key}, Imię i nazwisko: ${cursor.value.firstName} ${cursor.value.lastName}`);
            console.log(`Rezerwacje: ${roomGuestPairs[cursor.value.firstName+','+cursor.value.lastName] ?? "Brak"}`)
            cursor.continue();
        }
    };

    cursorRequest.onerror = (event) => {
        console.error("Error:", event.target.error);
    };

    console.groupEnd();
}

function displayHotelStatus() {
    const transaction = db.transaction([roomStoreName], 'readonly');
    const roomStore = transaction.objectStore(roomStoreName);

    const cursorRequest = roomStore.openCursor();

    console.group("Status pokoi");
    cursorRequest.onsuccess = (event) => {
        const cursor = event.target.result;

        if (cursor) {
            console.group(`Pokój ${cursor.value.number}`);
            console.log(`${cursor.value.availability} dostępnych miejsc`);
            console.log(`goście: ${cursor.value.guests ?? "brak"}`);
            console.groupEnd();
            cursor.continue();
        }
    };

    cursorRequest.onerror = (event) => {
        console.error("Error", event.target.error);
    };

    console.groupEnd();
}
