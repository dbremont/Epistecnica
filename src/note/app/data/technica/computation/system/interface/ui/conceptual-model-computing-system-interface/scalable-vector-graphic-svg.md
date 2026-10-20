# Scalable Vector Graphic (SVG)


> **SVG (Scalable Vector Graphics)** is an XML-based format for vector graphics that allows for scalable, high-quality images and graphics that can be rendered at any size without loss of resolution.
> 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Physics Models Map</title>
    <style>
        .map {
            width: 100%;
            height: 600px;
            position: relative;
        }
        .popup {
            display: none;
            position: absolute;
            background: #fff;
            border: 1px solid #000;
            padding: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>
    <div class="map">
        <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <!-- Add SVG elements here -->
            <circle cx="100" cy="100" r="10" fill="blue" data-popup="popup1"></circle>
            <circle cx="200" cy="150" r="10" fill="red" data-popup="popup2"></circle>
            <!-- Add more circles here -->
        </svg>
        <div id="popup1" class="popup">Newton's Laws of Motion</div>
        <div id="popup2" class="popup">Quantum Mechanics</div>
        <!-- Add more popups here -->
    </div>

    <script>
        document.querySelectorAll('circle').forEach(circle => {
            circle.addEventListener('mouseover', function() {
                const popupId = this.getAttribute('data-popup');
                document.getElementById(popupId).style.display = 'block';
                document.getElementById(popupId).style.left = this.cx.baseVal.value + 'px';
                document.getElementById(popupId).style.top = this.cy.baseVal.value + 'px';
            });

            circle.addEventListener('mouseout', function() {
                const popupId = this.getAttribute('data-popup');
                document.getElementById(popupId).style.display = 'none';
            });
        });
    </script>
</body>
</html>

```

## References

- https://en.wikipedia.org/wiki/SVG
- [Scalable Vector Graphics (SVG) Spec](https://www.w3.org/TR/SVG2/)
- https://news.ycombinator.com/item?id=46235959
- Example: https://asiasociety.org/policy-institute/taiwan-policy-database#timeline-visualization