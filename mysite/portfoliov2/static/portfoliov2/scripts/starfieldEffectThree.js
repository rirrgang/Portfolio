// Create a scene
var scene = new THREE.Scene();

// Create a camera
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

var hexagonImg = document.getElementById("hexagonImg");

// Create a renderer
var renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.domElement.id = "starfieldCanvas"; // Set the ID of the canvas
renderer.setSize(document.body.offsetWidth, document.body.offsetHeight);
renderer.setClearColor(0x000000, 0); // Set clear color to transparent
document.body.appendChild(renderer.domElement); // Append to the body element

// Create a texture loader
var textureLoader = new THREE.TextureLoader();

// Define an array of random colors
var colors = ["#E28F0A", "#BDBDBD", "#F59B0B", "#4D4D4D", "#B0820F"];

// Create a starfield effect
var starAmount = 100000; // 10000
var starSpread = 2000; // 2000

// Pass the Image object to the textureLoader.load function using its HTMLImageElement constructor
textureLoader.load(hexagonImg.src, function (texture) {
  // Create a starfield
  var starGeometry = new THREE.BufferGeometry();
  var starPositions = new Float32Array(starAmount * 3);
  var starRotations = new Float32Array(starAmount * 3);
  var starColors = new Float32Array(starAmount * 3); // Add a new array for star colors
  for (var i = 0; i < starAmount; i++) {
    var x = THREE.MathUtils.randFloatSpread(starSpread);
    var y = THREE.MathUtils.randFloatSpread(starSpread);
    var z = THREE.MathUtils.randFloatSpread(starSpread);
    //randomize the position of each star
    starPositions[i * 3] = x;
    starPositions[i * 3 + 1] = y;
    starPositions[i * 3 + 2] = z;
    //pick a random color from the colors array and set the color of each star
    var color = new THREE.Color(colors[Math.floor(Math.random() * colors.length)]);
    starColors[i * 3] = color.r;
    starColors[i * 3 + 1] = color.g;
    starColors[i * 3 + 2] = color.b;
    //add a random rotation for each star
    starRotations[i * 3] = Math.random() * Math.PI * 2;
    starRotations[i * 3 + 1] = Math.random() * Math.PI * 2;
  }

  starGeometry.setAttribute("position", new THREE.BufferAttribute(starPositions, 3));
  starGeometry.setAttribute("color", new THREE.BufferAttribute(starColors, 3)); // Set the color attribute
  starGeometry.setAttribute("rotation", new THREE.BufferAttribute(starRotations, 3)); // Set the rotation attribute
  var starMaterial = new THREE.PointsMaterial({
    size: 1,
    map: texture,
    vertexColors: true, // Enable vertex colors
    transparent: true,
    opacity: 0.5,
  });

  var stars = new THREE.Points(starGeometry, starMaterial);
  scene.add(stars);

  // mouse
  let mouseX = 0;
  let mouseY = 0;
  document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  // Create an animation loop
  function animate() {
    requestAnimationFrame(animate);
    stars.rotation.x += 0.00005; // Remove the random rotation in the animate function
    stars.rotation.y += 0.00001;
    //stars.position.x = mouseX * 0.005;
    //stars.position.y = mouseY * -0.005;
    camera.position.x += (mouseX - camera.position.x) * 0.0001;
    camera.position.y += (-mouseY - camera.position.y) * 0.0005;
    renderer.render(scene, camera);
  }
  animate();

  // Create a resize observer
  var resizeObserver = new ResizeObserver(updateRendererSize);
  resizeObserver.observe(document.body);

  // Function to update the renderer size
  function updateRendererSize() {
    renderer.setSize(document.body.offsetWidth, document.body.offsetHeight);
    camera.aspect = document.body.offsetWidth / document.body.offsetHeight;
    camera.updateProjectionMatrix();
  }

  // Add event listener to update the canvas size when the window is resized
  window.addEventListener("resize", updateRendererSize);
});
