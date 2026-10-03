from django.shortcuts import render

def home(request):
    sidebar_sect = [
        {
            "title": "Trending",
            "items": [
                {"name": "Bestsellers"},
                {"name": "New Releases"},
            ],
        },
        {
            "title": "Digital Content and Devices",
            "items": [
                {"name": "Echo & Alexa"},
                {"name": "Fire TV"},
                {"name": "Kindle E-Readers & eBooks"},
                {"name": "Audible Audiobooks"},
                {"name": "Amazon Prime Video"},
                {"name": "Amazon Music"},
            ],
        },
        {
            "title": "Shop by Category",
            "items": [
                {"name": "Mobiles, Computers"},
                {"name": "TV, Appliances, Electronics"},
                {"name": "Men's Fashion"},
                {"name": "Women's Fashion"},
            ],
        },
        {
            "title": "Programs & Features",
            "items": [
                {"name": "Gift Cards & Mobile Recharges"},
                {"name": "Amazon Launchpad"},
                {"name": "Amazon Business"},
                {"name": "Handloom and Handicrafts"},
            ],
        },
        {
            "title": "Help & Settings",
            "items": [
                {"name": "Customer Service"},
                {"name": "Your Account"},
                {"name": "Sign Out"},
            ],
        },
    ]

    return render(request, "index.html", {"sidebar_sect": sidebar_sect})

