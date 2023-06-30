self.addEventListener('push', function(e) {
    const data = e.data.json();
    self.registration.showNotification(data.title, {
        body: '😊',
        icon: '../assets/otter-solid.svg',
        badge: '../assets/otter-solid.svg'
    });
});