// Dynamically add the HTML for the duck playground
const wrapper = document.createElement('div');
wrapper.classList.add('wrapper');
wrapper.style.position = 'fixed';
wrapper.style.top = '0';
wrapper.style.left = '0';
wrapper.style.width = '100%';
wrapper.style.height = '100%';
wrapper.style.pointerEvents = 'none';
wrapper.style.zIndex = '9999';
wrapper.innerHTML = `
    <div class="marker red"></div>
    <div class="marker blue"></div>
    <div class="marker yellow"></div>
    <div class="marker pink"></div>
    <div class="marker green"></div>
    <div class="marker purple"></div>
    <div class="duck down">
        <div class="neck-base">
            <div class="neck">
                <div class="head"></div>
            </div>
        </div>
        <div class="tail"></div>
        <div class="body"></div>
        <div class="legs">
            <div class="leg"></div>
            <div class="leg"></div>
        </div>
    </div>
`;
document.body.appendChild(wrapper);

const createDucklingBtn = document.createElement('button');
createDucklingBtn.classList.add('create-duckling');
createDucklingBtn.textContent = "Add Duckling";
createDucklingBtn.style.position = 'fixed';
createDucklingBtn.style.bottom = '20px';
createDucklingBtn.style.right = '20px';
createDucklingBtn.style.zIndex = '10000';
createDucklingBtn.style.pointerEvents = 'auto';
document.body.appendChild(createDucklingBtn);

const indicator = document.createElement('div');
indicator.classList.add('indicator');
indicator.style.position = 'fixed';
indicator.style.top = '10px';
indicator.style.right = '10px';
indicator.style.color = '#fff';
indicator.style.fontFamily = 'Arial, sans-serif';
indicator.style.zIndex = '10001';
document.body.appendChild(indicator);

// Inject basic styles dynamically
const styles = document.createElement('style');
styles.textContent = `
    .wrapper .marker {
        position: absolute;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        display: none;
    }
    .marker.red { background-color: red; }
    .marker.blue { background-color: blue; }
    .marker.yellow { background-color: yellow; }
    .marker.pink { background-color: pink; }
    .marker.green { background-color: green; }
    .marker.purple { background-color: purple; }
    .duck, .duckling {
        position: absolute;
        width: 40px;
        height: 40px;
        background-color: yellow;
        border-radius: 50%;
        transition: transform 0.3s;
    }
    .duck .head { background-color: orange; width: 20px; height: 20px; border-radius: 50%; }
    .duck .body { background-color: yellow; }
    .duck .leg { background-color: orange; width: 5px; height: 10px; position: absolute; bottom: 0; }
    .indicator {
        color: white;
        font-size: 14px;
        font-family: Arial, sans-serif;
    }
    .create-duckling {
        padding: 10px;
        font-size: 14px;
        background-color: #444;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
`;
document.head.appendChild(styles);

// Duck and movement logic
const data = {
    interval: null,
    target: { x: 0, y: 0 },
    newTarget: { x: 0, y: 0 },
    cursor: { x: 0, y: 0 },
    duck: {
        x: 0,
        y: 0,
        angle: 0,
        direction: 'down',
        offset: { x: 20, y: 14 },
        el: wrapper.querySelector('.duck'),
    },
    ducklingTargets: [],
    ducklings: [],
};

const px = num => `${num}px`;
const randomN = max => Math.ceil(Math.random() * max);
const updateData = (dataObj, newData) => {
    Object.keys(newData).forEach(key => {
        dataObj[key] = newData[key];
    });
};

const setStyles = ({ el, x, y }) => {
    el.style.transform = `translate(${x ? px(x) : 0}, ${y ? px(y) : 0})`;
    el.style.zIndex = y;
};

const moveDuck = (duck, { x, y }) => {
    updateData(duck, { x, y });
    setStyles(duck);
};

const moveMotherDuck = ({ x, y }) => {
    moveDuck(data.duck, { x, y });
    data.ducklingTargets.forEach((duckling, i) => {
        setTimeout(() => {
            moveDuck(duckling, {
                x: x - (i + 1) * 40,
                y: y - (i + 1) * 40,
            });
        }, 100 * (i + 1));
    });
};

const updateCursorPos = e => {
    data.cursor.x = e.pageX;
    data.cursor.y = e.pageY;
};

const triggerDuckMovement = () => {
    data.interval = setInterval(() => {
        const { x, y } = data.cursor;
        moveMotherDuck({ x, y });
    }, 200);
};

const createDuckling = () => {
    const duckling = document.createElement('div');
    duckling.className = 'duckling';
    wrapper.appendChild(duckling);
    const ducklingData = { el: duckling, x: 0, y: 0 };
    data.ducklings.push(ducklingData);
    data.ducklingTargets.push(ducklingData);
};

// Initialize the playground
['mousemove'].forEach(event => window.addEventListener(event, updateCursorPos));
createDucklingBtn.addEventListener('click', createDuckling);
triggerDuckMovement();
for (let i = 0; i < 3; i++) createDuckling();
