# Backpropagation


> Notes intent.
> 

> **Short definition** of the topic.
> 

> Note: Weight update is also known as **credit assignment**.
> 

- [ ]  https://visionbook.mit.edu/backpropagation.html
- [ ]  http://neuralnetworksanddeeplearning.com/chap2.html
- [ ]  https://d2l.ai/chapter_recurrent-neural-networks/bptt.html
- [ ]  https://en.wikipedia.org/wiki/Chain_rule
- [ ]  https://en.wikipedia.org/wiki/Automatic_differentiation

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Backpropagation — 1-1-1 Network</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<script src="https://cdn.tailwindcss.com"></script>
<style>
:root{--bg:#0b0b12;--fg:#e8e4df;--muted:#6b6578;--accent:#f59e0b;--card:#111119;--card2:#15151f;--border:#222233;--fwd:#22d3a7;--bwd:#f97352;--loss:#ef4444}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Space Grotesk',sans-serif;background:var(--bg);color:var(--fg);overflow:hidden;height:100vh;-webkit-font-smoothing:antialiased}
.mono{font-family:'JetBrains Mono',monospace}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:linear-gradient(var(--accent),var(--bwd));border-radius:3px}
input[type="range"]{-webkit-appearance:none;appearance:none;width:100%;height:5px;border-radius:3px;outline:none;cursor:pointer;background:linear-gradient(to right,var(--accent) var(--p,50%),var(--border) var(--p,50%))}
input[type="range"]::-webkit-slider-thumb{-webkit-appearance:none;width:15px;height:15px;border-radius:50%;background:var(--fg);border:2px solid var(--accent);cursor:grab;box-shadow:0 0 0 0 rgba(245,158,11,0);transition:box-shadow .18s,transform .18s}
input[type="range"]:hover::-webkit-slider-thumb{box-shadow:0 0 0 5px rgba(245,158,11,.16)}
input[type="range"]:active::-webkit-slider-thumb{transform:scale(1.18);cursor:grabbing;box-shadow:0 0 0 7px rgba(245,158,11,.24)}
input[type="range"]::-moz-range-thumb{width:15px;height:15px;border-radius:50%;background:var(--fg);border:2px solid var(--accent);cursor:grab}
input[type="range"]::-moz-range-track{height:5px;border-radius:3px;background:var(--border)}
input[type="range"]::-moz-range-progress{height:5px;border-radius:3px;background:var(--accent)}
.btn{position:relative;padding:7px 12px;border-radius:8px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid var(--border);background:var(--card);color:var(--fg);transition:transform .16s cubic-bezier(.2,.8,.3,1),box-shadow .2s,border-color .2s,color .2s,background .2s;font-family:'Space Grotesk',sans-serif;white-space:nowrap}
.btn:hover{transform:translateY(-2px);border-color:var(--accent);color:var(--accent);box-shadow:0 8px 22px -8px rgba(245,158,11,.5)}
.btn:active{transform:translateY(0) scale(.97)}
.btn i{transition:transform .2s}.btn:hover i{transform:translateX(1px)}
.btn-fwd{border-color:rgba(34,211,167,.4);color:var(--fwd)}.btn-fwd:hover{background:var(--fwd);color:var(--bg);box-shadow:0 8px 22px -8px rgba(34,211,167,.6)}
.btn-bwd{border-color:rgba(249,115,82,.4);color:var(--bwd)}.btn-bwd:hover{background:var(--bwd);color:var(--bg);box-shadow:0 8px 22px -8px rgba(249,115,82,.6)}
.btn-accent{border-color:rgba(245,158,11,.4);color:var(--accent)}.btn-accent:hover{background:var(--accent);color:var(--bg)}
.btn-active{background:var(--accent)!important;color:var(--bg)!important;border-color:var(--accent)!important;box-shadow:0 0 0 4px rgba(245,158,11,.2)!important}
.log-entry{padding:2px 0;font-size:11.5px;line-height:1.65;border-bottom:1px solid rgba(255,255,255,.02);animation:fiu .28s ease both}
@keyframes fiu{from{opacity:0;transform:translateX(-5px)}to{opacity:1;transform:translateX(0)}}
@keyframes slideL{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:translateX(0)}}
@keyframes fade{from{opacity:0}to{opacity:1}}
.stitle{font-size:9.5px;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;color:var(--muted);margin-bottom:8px}
.pr{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.pr:hover .pl{color:var(--accent)}
.pl{font-size:12px;min-width:22px;font-family:'JetBrains Mono',monospace;color:var(--muted);transition:color .2s}
.pv{font-size:11px;min-width:52px;text-align:right;font-family:'JetBrains Mono',monospace;color:var(--fg);transition:color .2s}
.toast{position:fixed;top:16px;right:16px;padding:9px 18px;border-radius:9px;font-size:12px;z-index:100;opacity:0;transform:translateY(-10px);transition:all .3s cubic-bezier(.2,.8,.3,1);pointer-events:none;font-family:'Space Grotesk',sans-serif;background:rgba(245,158,11,.14);border:1px solid var(--accent);color:var(--accent);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);box-shadow:0 10px 30px -8px rgba(245,158,11,.4)}
.toast.show{opacity:1;transform:translateY(0)}
.glass{background:rgba(17,17,25,.72);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
#badge{transition:color .3s,border-color .3s,background .3s}
aside{animation:slideL .5s cubic-bezier(.2,.8,.3,1) both}
main{animation:fade .5s ease both}
.modal-overlay{position:fixed;inset:0;background:rgba(5,5,10,.78);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;z-index:200;opacity:0;pointer-events:none;transition:opacity .28s}
.modal-overlay.show{opacity:1;pointer-events:auto}
.modal-card{background:var(--card);border:1px solid var(--border);border-radius:16px;max-width:580px;width:92%;max-height:84vh;overflow-y:auto;padding:26px 28px 22px;position:relative;transform:translateY(18px) scale(.97);transition:transform .32s cubic-bezier(.2,.9,.3,1.1);box-shadow:0 30px 80px rgba(0,0,0,.6)}
.modal-overlay.show .modal-card{transform:translateY(0) scale(1)}
.modal-close{position:absolute;top:12px;right:14px;width:28px;height:28px;border-radius:8px;background:rgba(255,255,255,.04);border:1px solid var(--border);color:var(--muted);cursor:pointer;font-size:12px;display:flex;align-items:center;justify-content:center;transition:all .2s}
.modal-close:hover{color:var(--fg);border-color:var(--accent);transform:rotate(90deg)}
.mh2{font-size:18px;font-weight:700;color:var(--accent);margin-bottom:4px}
.msub{font-size:11px;color:var(--muted);margin-bottom:16px}
.msec{font-size:9.5px;font-weight:600;text-transform:uppercase;letter-spacing:1.3px;color:var(--muted);margin:16px 0 6px}
.mbody{font-size:12.5px;line-height:1.6;color:var(--fg)}
.meq{font-family:'JetBrains Mono',monospace;font-size:12px;background:rgba(255,255,255,.03);border:1px solid var(--border);border-radius:8px;padding:8px 12px;margin:6px 0}
.mli{font-size:12.5px;line-height:1.55;color:var(--fg);display:flex;gap:9px;margin:4px 0}
.mdot{flex-shrink:0;width:8px;height:8px;border-radius:50%;margin-top:6px}
@media(prefers-reduced-motion:reduce){*{animation-duration:0s!important;transition-duration:0s!important}}
</style></style>
</head>
<body>
<div id="toast" class="toast"></div>
<div id="modal" class="modal-overlay">
<div class="modal-card">
<button class="modal-close" id="modal-x"><i class="fas fa-times"></i></button>
<div class="mh2">How this works</div>
<div class="msub">Backpropagation on the simplest neural network — 1 input, 1 hidden neuron, 1 output.</div>
<div class="msec">The network</div>
<div class="meq">x &nbsp;→&nbsp; <span style="color:var(--accent)">z₁=w₁x+b₁</span> → σ → h &nbsp;→&nbsp; <span style="color:var(--accent)">z₂=w₂h+b₂</span> → σ → ŷ &nbsp;→&nbsp; L
<div style="margin-top:6px">h = σ(z₁) &nbsp;·&nbsp; ŷ = σ(z₂) &nbsp;·&nbsp; L = ½(ŷ − t)²</div></div>
<div class="msec">What is z? (pre-activation)</div>
<div class="mbody"><b style="color:var(--accent)">z</b> is the weighted sum (w·input + b) computed <b>before</b> the sigmoid. Each neuron has two stages: the linear sum <span class="mono" style="color:var(--accent)">z</span>, then the activation <span class="mono">σ(z)</span>. The <b>bias feeds into z</b>, not after the sigmoid — which is why ∂L/∂b equals ∂L/∂z.</div>
<div class="msec">The three phases</div>
<div class="mli"><span class="mdot" style="background:var(--fwd)"></span><div><b>Forward</b> (green): compute z₁ → h → z₂ → ŷ → L, left to right.</div></div>
<div class="mli"><span class="mdot" style="background:var(--bwd)"></span><div><b>Backward</b> (orange): chain rule right to left — how each w and b moves the loss.</div></div>
<div class="mli"><span class="mdot" style="background:var(--accent)"></span><div><b>Update</b>: w ← w − η·∂L/∂w. Repeat to shrink the loss.</div></div>
<div class="msec">Controls</div>
<div class="mbody">Drag sliders to set <span class="mono">x, t, w, b, η</span>. Use <b>Step</b> to advance one operation, <b>Forward/Backward</b> for a full pass, or <b>Auto Train</b> to loop. Hover a node to highlight it.</div>
<div class="msec">Legend</div>
<div class="mli"><span class="mdot" style="background:var(--accent)"></span><div>Pre-activation <span class="mono">z</span> (weighted sum + bias)</div></div>
<div class="mli"><span class="mdot" style="background:var(--fwd)"></span><div>Forward values (activations, loss)</div></div>
<div class="mli"><span class="mdot" style="background:var(--bwd)"></span><div>Backward gradients</div></div>
</div>
</div>
<div class="flex h-screen">
<!-- Sidebar -->
<aside class="w-[280px] flex-shrink-0 border-r flex flex-col" style="border-color:var(--border);background:var(--card)">
<div class="p-4 border-b flex items-start justify-between gap-2" style="border-color:var(--border)">
<div>
<h1 class="text-base font-bold tracking-tight" style="color:var(--accent)">Backpropagation</h1>
<p class="text-[11px] mt-0.5" style="color:var(--muted)">1-1-1 Network — simplest chain rule</p>
</div>
<button class="btn btn-accent" id="btn-help" title="How it works" style="padding:5px 9px;flex-shrink:0"><i class="fas fa-question fa-xs"></i></button>
</div>
<div class="flex-1 overflow-y-auto p-3.5 space-y-4">
<!-- Data -->
<div><div class="stitle">Data</div>
<div class="pr"><span class="pl">x</span><input type="range" id="sl-x" min="-2" max="2" step="0.05" value="0.50"><span class="pv" id="val-x">0.50</span></div>
<div class="pr"><span class="pl">t</span><input type="range" id="sl-t" min="-1" max="1" step="0.05" value="0.80"><span class="pv" id="val-t">0.80</span></div>
</div>
<!-- Weights -->
<div><div class="stitle">Weights &amp; Biases</div>
<div class="pr"><span class="pl">w₁</span><input type="range" id="sl-w0" min="-2" max="2" step="0.05" value="0.40"><span class="pv" id="val-w0">0.40</span></div>
<div class="pr"><span class="pl">b₁</span><input type="range" id="sl-b0" min="-2" max="2" step="0.05" value="0.10"><span class="pv" id="val-b0">0.10</span></div>
<div class="pr"><span class="pl">w₂</span><input type="range" id="sl-w1" min="-2" max="2" step="0.05" value="-0.60"><span class="pv" id="val-w1">-0.60</span></div>
<div class="pr"><span class="pl">b₂</span><input type="range" id="sl-b1" min="-2" max="2" step="0.05" value="-0.10"><span class="pv" id="val-b1">-0.10</span></div>
</div>
<!-- Training -->
<div><div class="stitle">Training</div>
<div class="pr"><span class="pl">η</span><input type="range" id="sl-lr" min="0.01" max="2" step="0.01" value="0.50"><span class="pv" id="val-lr">0.50</span></div>
<div class="pr"><span class="pl">ep</span><span class="pv mono" id="val-epoch" style="min-width:auto;text-align:left;color:var(--accent)">0</span></div>
</div>
<!-- Buttons -->
<div><div class="stitle">Step Through</div>
<div class="grid grid-cols-2 gap-1.5">
<button class="btn btn-fwd" id="btn-fwd-s"><i class="fas fa-angle-right fa-xs"></i> Fwd Step</button>
<button class="btn btn-bwd" id="btn-bwd-s"><i class="fas fa-angle-left fa-xs"></i> Bwd Step</button>
<button class="btn btn-fwd" id="btn-fwd-a"><i class="fas fa-forward fa-xs"></i> Forward</button>
<button class="btn btn-bwd" id="btn-bwd-a"><i class="fas fa-backward fa-xs"></i> Backward</button>
<button class="btn btn-accent" id="btn-update"><i class="fas fa-arrow-down fa-xs"></i> Update</button>
<button class="btn btn-accent" id="btn-train"><i class="fas fa-bolt fa-xs"></i> Full Step</button>
</div>
<div class="grid grid-cols-2 gap-1.5 mt-1.5">
<button class="btn" id="btn-auto"><i class="fas fa-play fa-xs"></i> Auto Train</button>
<button class="btn" id="btn-reset"><i class="fas fa-undo fa-xs"></i> Reset All</button>
</div>
<button class="btn w-full mt-1.5" id="btn-rand"><i class="fas fa-dice fa-xs"></i> Randomize Weights</button>
</div>
</div>
<div class="p-3 border-t text-[10.5px] space-y-1" style="border-color:var(--border);color:var(--muted)">
<div class="flex items-center gap-2"><span class="inline-block w-2.5 h-2.5 rounded-full" style="background:var(--accent)"></span>Pre-activation z</div>
<div class="flex items-center gap-2"><span class="inline-block w-2.5 h-2.5 rounded-full" style="background:var(--fwd)"></span>Forward values</div>
<div class="flex items-center gap-2"><span class="inline-block w-2.5 h-2.5 rounded-full" style="background:var(--bwd)"></span>Backward gradients</div>
<div class="flex items-center gap-2"><span class="inline-block w-2.5 h-2.5 rounded-full" style="background:var(--loss)"></span>Loss (MSE)</div>
</div>
</aside>
<!-- Main -->
<main class="flex-1 flex flex-col min-w-0">
<div class="flex-1 relative" id="cw"><canvas id="graph"></canvas>
<div class="absolute top-3 right-3 mono text-[11px] px-3 py-1.5 rounded-lg flex gap-4 glass" style="background:rgba(17,17,25,.72);border:1px solid var(--border)">
<span><span style="color:var(--muted)">Loss </span><span id="ov-loss" style="color:var(--loss)">—</span></span>
<span><span style="color:var(--muted)">ŷ </span><span id="ov-yh" style="color:var(--fwd)">—</span></span>
</div>
<div class="absolute top-3 left-3 mono text-[10px] px-2.5 py-1 rounded glass" id="badge" style="background:rgba(17,17,25,.72);border:1px solid var(--border);color:var(--muted)">IDLE</div>
</div>
<div class="h-[185px] border-t flex flex-col" style="border-color:var(--border);background:var(--card)">
<div class="px-4 py-1.5 border-b flex items-center justify-between" style="border-color:var(--border)">
<span class="stitle" style="margin:0">Computation Log</span>
<button class="text-[10px] cursor-pointer hover:text-white" style="color:var(--muted);background:none;border:none;font-family:inherit" id="btn-clr">Clear</button>
</div>
<div class="flex-1 overflow-y-auto px-4 py-1.5 mono" id="log"></div>
</div>
</main>
</div>

<script>
(function(){
'use strict';
const SUB='₀₁₂₃₄₅₆₇₈₉';
function sub(n){return String(n).split('').map(d=>SUB[+d]).join('')}

/* ===== State ===== */
const S={
  x:0.5, t:0.8, w:[0.4,-0.6], b:[0.1,-0.1], lr:0.5, epoch:0,
  z1:null, h:null, z2:null, yh:null, loss:null,
  dLdy:null, dydz2:null, dLdz2:null,
  dLdw2:null, dLdb2:null, dLdh:null, dLdz1:null,
  dLdw1:null, dLdb1:null
};
let fStep=0, bStep=0, autoOn=false;
const lossH=[];
let particles=[], bParticles=[], nodePulse={}, hovNode=null;

/* ===== Motion helpers ===== */
let intro=0;
const tweens={};
function tw(k,t){const o=tweens[k]=tweens[k]||{v:0,t:0};o.t=t}
function tv(k){const o=tweens[k];if(!o)return 0;o.v+=(o.t-o.v)*0.25;if(Math.abs(o.t-o.v)<1e-5)o.v=o.t;return o.v}
function easeOut(t){return 1-Math.pow(1-t,3)}
function clamp01(t){return Math.max(0,Math.min(1,t))}
function updFill(el){const mn=+el.min,mx=+el.max,v=+el.value;el.style.setProperty('--p',((v-mn)/(mx-mn)*100).toFixed(2)+'%')}

function sig(x){return 1/(1+Math.exp(-Math.max(-500,Math.min(500,x))))}

/* ===== Sliders ===== */
const SL=['x','t','w0','b0','w1','b1','lr'];
const SM={x:'x',t:'t',w0:'w|0',b0:'b|0',w1:'w|1',b1:'b|1',lr:'lr'};
SL.forEach(id=>{
  const el=document.getElementById('sl-'+id);
  if(!el)return;
  el.addEventListener('input',()=>{
    document.getElementById('val-'+id).textContent=(+el.value).toFixed(2);
    updFill(el); readSl(); resetComp(); if(autoOn)stopAuto();
  });
});
function readSl(){
  S.x=+document.getElementById('sl-x').value;
  S.t=+document.getElementById('sl-t').value;
  S.w[0]=+document.getElementById('sl-w0').value;
  S.w[1]=+document.getElementById('sl-w1').value;
  S.b[0]=+document.getElementById('sl-b0').value;
  S.b[1]=+document.getElementById('sl-b1').value;
  S.lr=+document.getElementById('sl-lr').value;
}
function writeSl(){
  document.getElementById('sl-x').value=S.x;document.getElementById('val-x').textContent=S.x.toFixed(2);
  document.getElementById('sl-t').value=S.t;document.getElementById('val-t').textContent=S.t.toFixed(2);
  document.getElementById('sl-w0').value=S.w[0];document.getElementById('val-w0').textContent=S.w[0].toFixed(2);
  document.getElementById('sl-w1').value=S.w[1];document.getElementById('val-w1').textContent=S.w[1].toFixed(2);
  document.getElementById('sl-b0').value=S.b[0];document.getElementById('val-b0').textContent=S.b[0].toFixed(2);
  document.getElementById('sl-b1').value=S.b[1];document.getElementById('val-b1').textContent=S.b[1].toFixed(2);
  document.getElementById('sl-lr').value=S.lr;document.getElementById('val-lr').textContent=S.lr.toFixed(2);
  SL.forEach(id=>{const e=document.getElementById('sl-'+id);if(e)updFill(e)});
}
function resetComp(){
  fStep=0;bStep=0;bParticles.length=0;
  S.z1=S.h=S.z2=S.yh=S.loss=null;
  S.dLdy=S.dydz2=S.dLdz2=null;
  S.dLdw2=S.dLdb2=S.dLdh=S.dLdz1=S.dLdw1=S.dLdb1=null;
  document.getElementById('ov-loss').textContent='—';
  document.getElementById('ov-yh').textContent='—';
  updBadge();
}

/* ===== Toast / Log / Badge ===== */
let tTm=0;
function toast(m){const e=document.getElementById('toast');e.textContent=m;e.classList.add('show');clearTimeout(tTm);tTm=setTimeout(()=>e.classList.remove('show'),1600)}
function addLog(h,c){const l=document.getElementById('log'),d=document.createElement('div');d.className='log-entry';d.style.color=c||'var(--fg)';d.innerHTML=h;l.appendChild(d);l.scrollTop=l.scrollHeight}
function clearLog(){document.getElementById('log').innerHTML=''}
function updBadge(){
  const e=document.getElementById('badge');
  if(bStep>=6){e.textContent='BACKWARD DONE';e.style.color='var(--bwd)'}
  else if(bStep>0){e.textContent='BACKWARD '+bStep+'/6';e.style.color='var(--bwd)'}
  else if(fStep>=5){e.textContent='FORWARD DONE';e.style.color='var(--fwd)'}
  else if(fStep>0){e.textContent='FORWARD '+fStep+'/5';e.style.color='var(--fwd)'}
  else{e.textContent='IDLE';e.style.color='var(--muted)'}
}

/* ===== Forward ===== */
function doFwd(){
  if(fStep>=5){toast('Forward pass complete');return false}
  fStep++;const c='var(--fwd)';
  if(fStep===1){
    S.z1=S.w[0]*S.x+S.b[0];
    addLog(`<span style="color:${c}">▶ Step 1: Pre-activation (hidden)</span>`);
    addLog(`  z${sub(1)} = w${sub(1)}·x + b${sub(1)} = ${S.w[0].toFixed(2)}·${S.x.toFixed(2)} + ${S.b[0].toFixed(2)} = <b>${S.z1.toFixed(4)}</b>`,c);
    spawnP(0,1,'#22d3a7');spawnBP(0,1,'#22d3a7');pulse(['h']);
  }else if(fStep===2){
    S.h=sig(S.z1);
    addLog(`<span style="color:${c}">▶ Step 2: Sigmoid (hidden)</span>`);
    addLog(`  h = σ(${S.z1.toFixed(4)}) = 1/(1+e${sup('−'+S.z1.toFixed(4))}) = <b>${S.h.toFixed(4)}</b>`,c);
  }else if(fStep===3){
    S.z2=S.w[1]*S.h+S.b[1];
    addLog(`<span style="color:${c}">▶ Step 3: Pre-activation (output)</span>`);
    addLog(`  z${sub(2)} = w${sub(2)}·h + b${sub(2)} = ${S.w[1].toFixed(2)}·${S.h.toFixed(4)} + ${S.b[1].toFixed(2)} = <b>${S.z2.toFixed(4)}</b>`,c);
    spawnP(1,1,'#22d3a7');spawnBP(1,1,'#22d3a7');pulse(['yh']);
  }else if(fStep===4){
    S.yh=sig(S.z2);
    addLog(`<span style="color:${c}">▶ Step 4: Sigmoid (output)</span>`);
    addLog(`  ŷ = σ(${S.z2.toFixed(4)}) = <b>${S.yh.toFixed(4)}</b>`,c);
    tw('yh',S.yh);
  }else if(fStep===5){
    S.loss=0.5*(S.yh-S.t)**2;
    addLog(`<span style="color:var(--loss)">▶ Step 5: Loss (MSE)</span>`);
    addLog(`  L = ½(ŷ − t)² = ½(${S.yh.toFixed(4)} − ${S.t.toFixed(2)})² = <b>${S.loss.toFixed(6)}</b>`,'var(--loss)');
    tw('loss',S.loss);
    spawnP(2,1,'#ef4444');pulse(['L']);
  }
  if(S.z1!==null)tw('z1',S.z1);if(S.h!==null)tw('h',S.h);if(S.z2!==null)tw('z2',S.z2);if(S.yh!==null)tw('yh',S.yh);if(S.loss!==null)tw('loss',S.loss);
  updBadge();return true;
}
function sup(s){return '<sup style="font-size:8px">'+s+'</sup>'}

/* ===== Backward ===== */
function doBwd(){
  if(fStep<5){toast('Run forward pass first');return false}
  if(bStep>=6){toast('Backward pass complete');return false}
  bStep++;const c='var(--bwd)';
  if(bStep===1){
    S.dLdy=S.yh-S.t;
    addLog(`<span style="color:${c}">◀ Step 1: ∂L/∂ŷ</span>`);
    addLog(`  ∂L/∂ŷ = ŷ − t = ${S.yh.toFixed(4)} − ${S.t.toFixed(2)} = <b>${S.dLdy.toFixed(4)}</b>`,c);
    spawnP(2,-1,'#f97352');pulse(['yh']);
  }else if(bStep===2){
    S.dydz2=S.yh*(1-S.yh);S.dLdz2=S.dLdy*S.dydz2;
    addLog(`<span style="color:${c}">◀ Step 2: Chain through σ (output)</span>`);
    addLog(`  σ'(z${sub(2)}) = ŷ(1−ŷ) = ${S.yh.toFixed(4)}·${(1-S.yh).toFixed(4)} = ${S.dydz2.toFixed(4)}`,c);
    addLog(`  ∂L/∂z${sub(2)} = ∂L/∂ŷ · σ'(z${sub(2)}) = ${S.dLdy.toFixed(4)} · ${S.dydz2.toFixed(4)} = <b>${S.dLdz2.toFixed(4)}</b>`,c);
  }else if(bStep===3){
    S.dLdw2=S.dLdz2*S.h;S.dLdb2=S.dLdz2;
    addLog(`<span style="color:${c}">◀ Step 3: Gradients for w${sub(2)}, b${sub(2)}</span>`);
    addLog(`  ∂L/∂w${sub(2)} = ∂L/∂z${sub(2)} · h = ${S.dLdz2.toFixed(4)} · ${S.h.toFixed(4)} = <b>${S.dLdw2.toFixed(4)}</b>`,c);
    addLog(`  ∂L/∂b${sub(2)} = ∂L/∂z${sub(2)} = <b>${S.dLdb2.toFixed(4)}</b>`,c);
    spawnBP(1,-1,'#f97352');
  }else if(bStep===4){
    S.dLdh=S.dLdz2*S.w[1];
    addLog(`<span style="color:${c}">◀ Step 4: Propagate gradient to h</span>`);
    addLog(`  ∂L/∂h = ∂L/∂z${sub(2)} · w${sub(2)} = ${S.dLdz2.toFixed(4)} · ${S.w[1].toFixed(2)} = <b>${S.dLdh.toFixed(4)}</b>`,c);
    spawnP(1,-1,'#f97352');pulse(['h']);
  }else if(bStep===5){
    const sp=S.h*(1-S.h);S.dLdz1=S.dLdh*sp;
    addLog(`<span style="color:${c}">◀ Step 5: Chain through σ (hidden)</span>`);
    addLog(`  σ'(z${sub(1)}) = h(1−h) = ${S.h.toFixed(4)}·${(1-S.h).toFixed(4)} = ${sp.toFixed(4)}`,c);
    addLog(`  ∂L/∂z${sub(1)} = ∂L/∂h · σ'(z${sub(1)}) = ${S.dLdh.toFixed(4)} · ${sp.toFixed(4)} = <b>${S.dLdz1.toFixed(4)}</b>`,c);
  }else if(bStep===6){
    S.dLdw1=S.dLdz1*S.x;S.dLdb1=S.dLdz1;
    addLog(`<span style="color:${c}">◀ Step 6: Gradients for w${sub(1)}, b${sub(1)}</span>`);
    addLog(`  ∂L/∂w${sub(1)} = ∂L/∂z${sub(1)} · x = ${S.dLdz1.toFixed(4)} · ${S.x.toFixed(2)} = <b>${S.dLdw1.toFixed(4)}</b>`,c);
    addLog(`  ∂L/∂b${sub(1)} = ∂L/∂z${sub(1)} = <b>${S.dLdb1.toFixed(4)}</b>`,c);
    spawnP(0,-1,'#f97352');spawnBP(0,-1,'#f97352');pulse(['x']);
  }
  updBadge();return true;
}

/* ===== Update ===== */
function doUpdate(){
  if(bStep<6){toast('Run backward pass first');return false}
  const ac='var(--accent)';
  addLog(`<span style="color:${ac}">▼ Weight Update:  w ← w − η · ∂L/∂w   (η = ${S.lr.toFixed(2)})</span>`);
  for(let i=0;i<2;i++){
    const g=i===0?S.dLdw1:S.dLdw2;const old=S.w[i];S.w[i]-=S.lr*g;
    addLog(`  w${sub(i+1)}: ${old.toFixed(4)} − ${S.lr.toFixed(2)}·${g.toFixed(4)} = <b>${S.w[i].toFixed(4)}</b>`,ac);
  }
  for(let i=0;i<2;i++){
    const g=i===0?S.dLdb1:S.dLdb2;const old=S.b[i];S.b[i]-=S.lr*g;
    addLog(`  b${sub(i+1)}: ${old.toFixed(4)} − ${S.lr.toFixed(2)}·${g.toFixed(4)} = <b>${S.b[i].toFixed(4)}</b>`,ac);
  }
  lossH.push(S.loss);if(lossH.length>500)lossH.shift();
  S.epoch++;document.getElementById('val-epoch').textContent=S.epoch;
  writeSl();resetComp();return true;
}

/* ===== Canvas ===== */
const cv=document.getElementById('graph'),cx=cv.getContext('2d'),wr=document.getElementById('cw');
let W=0,H=0;
function resize(){const r=wr.getBoundingClientRect(),d=devicePixelRatio||1;cv.width=r.width*d;cv.height=r.height*d;cv.style.width=r.width+'px';cv.style.height=r.height+'px';cx.setTransform(d,0,0,d,0,0);W=r.width;H=r.height}
window.addEventListener('resize',resize);resize();

/* ===== Layout ===== */
function nds(){
  const cy=H*0.46,gap=W*0.22;
  return{
    x:{x:W*0.1,y:cy},
    h:{x:W*0.1+gap,y:cy},
    yh:{x:W*0.1+gap*2,y:cy},
    L:{x:W*0.1+gap*3,y:cy}
  };
}
const LBL={x:'x',h:'h',yh:'ŷ',L:'L'};
const OPS={x:'input',h:'σ(w₁x + b₁)',yh:'σ(w₂h + b₂)',L:'½(ŷ−t)²'};
const ELBL=['w₁','w₂',''];
const BLBL=['b₁','b₂'];

function edgeState(i){
  if(i===0)return{f:fStep>=1,b:bStep>=6};
  if(i===1)return{f:fStep>=3,b:bStep>=3};
  return{f:fStep>=5,b:bStep>=1};
}

/* ===== Particles ===== */
function spawnP(ei,dir,col){for(let j=0;j<8;j++)particles.push({ei,dir,t:-j*0.1,spd:0.012+Math.random()*0.005,col,sz:2.5+Math.random()*1.5})}
function pulse(ns){const now=performance.now();ns.forEach(n=>nodePulse[n]=now)}

/* ===== Node values / grads ===== */
function nVal(n){return n==='x'?S.x:n==='h'?S.h:n==='yh'?S.yh:n==='L'?S.loss:null}
function nGrad(n){
  if(n==='L')return 1;if(n==='yh')return S.dLdy;
  if(n==='h')return S.dLdh;if(n==='x')return S.dLdz1*S.w[0];return null;
}
function nFwdA(n){return n==='x'?fStep>=1:n==='h'?fStep>=2:n==='yh'?fStep>=4:n==='L'?fStep>=5:false}
function nBwdA(n){return n==='L'?bStep>=1:n==='yh'?bStep>=1:n==='h'?bStep>=4:n==='x'?bStep>=6:false}

/* ===== Drawing ===== */
function rRect(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.lineTo(x+w-r,y);c.quadraticCurveTo(x+w,y,x+w,y+r);c.lineTo(x+w,y+h-r);c.quadraticCurveTo(x+w,y+h,x+w-r,y+h);c.lineTo(x+r,y+h);c.quadraticCurveTo(x,y+h,x,y+h-r);c.lineTo(x,y+r);c.quadraticCurveTo(x,y,x+r,y);c.closePath()}

function drawBg(){
  const t=performance.now()/1000;
  const g=cx.createRadialGradient(W*0.5,H*0.42,0,W*0.5,H*0.42,W*0.72);
  g.addColorStop(0,'#10101c');g.addColorStop(1,'#090910');
  cx.fillStyle=g;cx.fillRect(0,0,W,H);
  const orbs=[{x:0.22,y:0.28,c:'34,211,167'},{x:0.8,y:0.3,c:'245,158,11'},{x:0.6,y:0.82,c:'249,115,82'}];
  orbs.forEach((o,i)=>{const ox=W*(o.x+Math.sin(t*0.18+i*2)*0.035),oy=H*(o.y+Math.cos(t*0.14+i*2)*0.035);const rg=cx.createRadialGradient(ox,oy,0,ox,oy,Math.max(W,H)*0.4);rg.addColorStop(0,'rgba('+o.c+',0.07)');rg.addColorStop(1,'rgba('+o.c+',0)');cx.fillStyle=rg;cx.fillRect(0,0,W,H)});
  cx.fillStyle='rgba(255,255,255,0.018)';
  for(let x=32;x<W;x+=32)for(let y=32;y<H;y+=32){cx.beginPath();cx.arc(x,y,0.7,0,6.283);cx.fill()}
  const vg=cx.createRadialGradient(W*0.5,H*0.5,Math.min(W,H)*0.3,W*0.5,H*0.5,Math.max(W,H)*0.75);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.45)');cx.fillStyle=vg;cx.fillRect(0,0,W,H);
}

function drawEdges(nd){
  for(let i=0;i<3;i++){
    const e=edgeState(i),a=nd[Object.keys(nd)[i]],b=nd[Object.keys(nd)[i+1]];
    let col='#252535',lw=1.5;
    if(e.b){col='#f97352';lw=2.5}else if(e.f){col='#22d3a7';lw=2.5}
    if(hovNode){const kn=Object.keys(nd);if(kn[i]===hovNode||kn[i+1]===hovNode){lw+=1;if(!e.f&&!e.b)col='#444455'}}
    // Glow
    if(e.f||e.b){cx.save();cx.shadowColor=col;cx.shadowBlur=14;cx.beginPath();cx.moveTo(a.x,a.y);cx.lineTo(b.x,b.y);cx.strokeStyle=col;cx.lineWidth=lw;cx.stroke();cx.restore()}
    cx.beginPath();cx.moveTo(a.x,a.y);cx.lineTo(b.x,b.y);cx.strokeStyle=col;cx.lineWidth=lw;cx.stroke();
    if(e.f||e.b){const dir=e.b?-1:1,fl=((performance.now()/1400)*dir)%1;for(let k=0;k<4;k++){let u=(fl+k*0.25);u=u-Math.floor(u);const fx=a.x+(b.x-a.x)*u,fy=a.y+(b.y-a.y)*u;cx.save();cx.globalAlpha=0.5;cx.shadowColor=col;cx.shadowBlur=8;cx.beginPath();cx.arc(fx,fy,1.9,0,6.283);cx.fillStyle=col;cx.fill();cx.restore()}}
    // Arrow
    if(e.f||e.b){
      const dir=e.b?-1:1;
      const t1=dir===1?0.78:0.22,t2=dir===1?0.84:0.16;
      const p1x=a.x+(b.x-a.x)*t1,p1y=a.y+(b.y-a.y)*t1;
      const p2x=a.x+(b.x-a.x)*t2,p2y=a.y+(b.y-a.y)*t2;
      const ang=Math.atan2(p2y-p1y,p2x-p1x),sz=8;
      cx.save();cx.translate(p2x,p2y);cx.rotate(ang);cx.beginPath();cx.moveTo(0,0);cx.lineTo(-sz,-sz*0.45);cx.lineTo(-sz,sz*0.45);cx.closePath();cx.fillStyle=col;cx.fill();cx.restore();
    }
    // Label
    if(i<2){
      const mx=(a.x+b.x)/2,my=(a.y+b.y)/2-22;
      const txt=ELBL[i]+'='+S.w[i].toFixed(2);
      cx.font='500 11px "JetBrains Mono"';cx.textAlign='center';cx.textBaseline='middle';
      const tw=cx.measureText(txt).width+12;
      cx.fillStyle='rgba(11,11,18,0.9)';rRect(cx,mx-tw/2,my-9,tw,18,5);cx.fill();
      cx.strokeStyle=e.b?'rgba(249,115,82,0.3)':e.f?'rgba(34,211,167,0.3)':'rgba(255,255,255,0.05)';cx.lineWidth=0.7;rRect(cx,mx-tw/2,my-9,tw,18,5);cx.stroke();
      cx.fillStyle=e.b?'#f97352':e.f?'#22d3a7':'#6b6578';cx.fillText(txt,mx,my);
      // Gradient on edge during backward
      if(e.b){
        const gv=i===0?S.dLdw1:S.dLdw2;
        if(gv!==null){
          const gt='∂L/∂'+ELBL[i]+'='+gv.toFixed(4);
          cx.font='400 10px "JetBrains Mono"';
          const gtw=cx.measureText(gt).width+10;
          cx.fillStyle='rgba(11,11,18,0.9)';rRect(cx,mx-gtw/2,my+12,gtw,16,4);cx.fill();
          cx.fillStyle='#f97352';cx.fillText(gt,mx,my+20);
        }
      }
    }
  }
}

function drawParticles(nd){
  const keys=Object.keys(nd);
  particles.forEach(p=>{
    if(p.t<0||p.t>1)return;
    const a=nd[keys[p.ei]],b=nd[keys[p.ei+1]];
    const tt=p.dir===1?p.t:1-p.t;
    const px=a.x+(b.x-a.x)*tt,py=a.y+(b.y-a.y)*tt;
    cx.save();cx.globalAlpha=Math.min(1,Math.min(p.t,1-p.t)*5);
    cx.shadowColor=p.col;cx.shadowBlur=10;
    cx.beginPath();cx.arc(px,py,p.sz,0,6.283);cx.fillStyle=p.col;cx.fill();cx.restore();
  });
}

function drawNodes(nd){
  const R=Math.max(28,Math.min(42,W*0.04));
  const ORD={x:0,h:1,yh:2,L:3};
  Object.entries(nd).forEach(([name,pos])=>{
    const ni=easeOut(clamp01((intro-(ORD[name]||0)*0.1)/0.55));if(ni<0.02)return;
    cx.save();cx.globalAlpha=ni;
    const fa=nFwdA(name),ba=nBwdA(name),act=fa||ba;
    const col=ba?'#f97352':fa?'#22d3a7':'#333345';
    const isH=hovNode===name;
    // Pulse ring
    const pt=performance.now()-(nodePulse[name]||0),pa=Math.max(0,1-pt/700);
    if(pa>0){
      cx.save();cx.globalAlpha=pa*0.5;cx.beginPath();cx.arc(pos.x,pos.y,R+16*pa,0,6.283);
      cx.strokeStyle=col;cx.lineWidth=2;cx.stroke();cx.restore();
    }
    // Glow
    if(act){const br=0.5+0.5*Math.sin(performance.now()/450);cx.save();cx.shadowColor=col;cx.shadowBlur=18+br*10;cx.beginPath();cx.arc(pos.x,pos.y,R,0,6.283);cx.fillStyle='rgba(0,0,0,0)';cx.fill();cx.restore()}
    // Fill (neurons split: amber top = pre-activation z, colored bottom = activation)
    const neuron=(name==='h'||name==='yh');
    if(neuron){
      const zOn=(name==='h'?S.z1:S.z2)!==null;
      cx.beginPath();cx.arc(pos.x,pos.y,R,0,Math.PI);cx.closePath();
      const gb=cx.createRadialGradient(pos.x-R*0.25,pos.y-R*0.1,0,pos.x,pos.y,R);
      if(act){gb.addColorStop(0,col+'30');gb.addColorStop(1,col+'08')}else{gb.addColorStop(0,'#1c1c28');gb.addColorStop(1,'#12121c')}
      cx.fillStyle=gb;cx.fill();
      cx.beginPath();cx.arc(pos.x,pos.y,R,Math.PI,2*Math.PI);cx.closePath();
      const gt=cx.createRadialGradient(pos.x-R*0.25,pos.y+R*0.1,0,pos.x,pos.y,R);
      gt.addColorStop(0,zOn?'#f59e0b38':'#1c1c28');gt.addColorStop(1,zOn?'#f59e0b0c':'#12121c');
      cx.fillStyle=gt;cx.fill();
      cx.beginPath();cx.moveTo(pos.x-R,pos.y);cx.lineTo(pos.x+R,pos.y);
      cx.strokeStyle='rgba(255,255,255,0.09)';cx.lineWidth=1;cx.stroke();
      if(zOn){cx.fillStyle='#f59e0b';cx.font='700 9px "JetBrains Mono"';cx.textAlign='center';cx.textBaseline='middle';cx.fillText('z',pos.x,pos.y-R*0.52)}
    }else{
      cx.beginPath();cx.arc(pos.x,pos.y,R,0,6.283);
      const gr=cx.createRadialGradient(pos.x-R*0.25,pos.y-R*0.25,0,pos.x,pos.y,R);
      if(act){gr.addColorStop(0,col+'28');gr.addColorStop(1,col+'08')}else{gr.addColorStop(0,'#1c1c28');gr.addColorStop(1,'#12121c')}
      cx.fillStyle=gr;cx.fill();
    }
    cx.strokeStyle=isH?'#aaa':col;cx.lineWidth=isH?2.5:(act?2.2:1.2);
    cx.beginPath();cx.arc(pos.x,pos.y,R,0,6.283);cx.stroke();
    // Label
    cx.fillStyle='#e8e4df';cx.font='600 '+Math.max(16,R*0.48)+'px "Space Grotesk"';cx.textAlign='center';cx.textBaseline='middle';
    cx.fillText(LBL[name],pos.x,pos.y);
    // Formula + values below
    let yOff=R+16;
    if(name==='h'||name==='yh'){
      const zi=name==='h'?1:2,ins=name==='h'?'x':'h',zKnown=(name==='h'?S.z1:S.z2)!==null;
      const ac=fa?'#22d3a7':'#6b6578',zc=zKnown?'#f59e0b':'#5a5566';
      const parts=[{t:'σ(',c:ac},{t:'z'+sub(zi)+' = w'+sub(zi)+'·'+ins+' + b'+sub(zi),c:zc},{t:')',c:ac}];
      cx.font='400 10.5px "JetBrains Mono"';cx.textAlign='left';cx.textBaseline='middle';
      let w=0;parts.forEach(p=>w+=cx.measureText(p.t).width);
      let xp=pos.x-w/2;
      parts.forEach(p=>{cx.fillStyle=p.c;cx.fillText(p.t,xp,pos.y+yOff);xp+=cx.measureText(p.t).width});
      yOff+=15;
    }else if(name==='L'){
      cx.font='400 10.5px "JetBrains Mono"';cx.textAlign='center';cx.textBaseline='middle';
      cx.fillStyle=fa?'#ef4444':'#6b6578';cx.fillText('L = ½(ŷ−t)²',pos.x,pos.y+yOff);yOff+=15;
    }
    let zL=null,zV=null;
    if(name==='h'&&S.z1!==null){zL='z'+sub(1);zV=tv('z1')}else if(name==='yh'&&S.z2!==null){zL='z'+sub(2);zV=tv('z2')}
    if(zL!==null){
      cx.font='500 11px "JetBrains Mono"';cx.textAlign='center';cx.textBaseline='middle';
      const zt=zL+' = '+zV.toFixed(4),zw=cx.measureText(zt).width+12;
      cx.fillStyle='rgba(245,158,11,0.13)';rRect(cx,pos.x-zw/2,pos.y+yOff-8,zw,16,5);cx.fill();
      cx.strokeStyle='rgba(245,158,11,0.4)';cx.lineWidth=0.8;rRect(cx,pos.x-zw/2,pos.y+yOff-8,zw,16,5);cx.stroke();
      cx.fillStyle='#f59e0b';cx.fillText(zt,pos.x,pos.y+yOff);yOff+=18;
    }
    if(fa){const raw=nVal(name);if(raw!==null){const dv=name==='h'?tv('h'):name==='yh'?tv('yh'):name==='L'?tv('loss'):S.x;cx.font='500 12px "JetBrains Mono"';cx.fillStyle='#22d3a7';cx.textAlign='center';cx.fillText(LBL[name]+' = '+dv.toFixed(4),pos.x,pos.y+yOff);yOff+=16}}
    if(ba){const g=nGrad(name);if(g!==null){cx.font='400 11px "JetBrains Mono"';cx.fillStyle='#f97352';cx.textAlign='center';cx.fillText('∂='+g.toFixed(4),pos.x,pos.y+yOff);yOff+=16}}
    cx.restore();
  });
  // Target label near L
  if(fStep>=5){
    const lp=nd.L;
    cx.font='400 11px "JetBrains Mono"';cx.fillStyle='#6b6578';cx.textAlign='center';
    cx.fillText('t = '+S.t.toFixed(2),lp.x,lp.y+R+48);
  }
}

function drawChainRule(nd){
  // Show the chain rule equation at the top when backward is in progress
  if(bStep===0)return;
  const y=H*0.06+34;
  cx.font='400 12px "JetBrains Mono"';cx.textAlign='center';cx.textBaseline='middle';
  const parts=[];
  parts.push({t:'∂L',c:'#ef4444'});
  parts.push({t:' = ',c:'#6b6578'});
  if(bStep>=1)parts.push({t:'(ŷ−t)',c:'#f97352'});
  if(bStep>=2)parts.push({t:' · ŷ(1−ŷ)',c:'#f97352'});
  if(bStep>=3)parts.push({t:' · w₂',c:'#f97352'});
  if(bStep>=5)parts.push({t:' · h(1−h)',c:'#f97352'});
  if(bStep>=6)parts.push({t:' · x',c:'#f97352'});
  // Build string
  let full='';parts.forEach(p=>full+=p.t);
  // Background
  cx.font='400 13px "JetBrains Mono"';
  const tw=cx.measureText(full).width+24;
  cx.fillStyle='rgba(11,11,18,0.9)';rRect(cx,W/2-tw/2,y-12,tw,24,6);cx.fill();
  cx.strokeStyle='rgba(249,115,82,0.2)';cx.lineWidth=0.7;rRect(cx,W/2-tw/2,y-12,tw,24,6);cx.stroke();
  // Draw parts with colors
  let xp=W/2-tw/2+12;
  parts.forEach(p=>{cx.fillStyle=p.c;cx.fillText(p.t,xp,y);xp+=cx.measureText(p.t).width});
}

function drawLossChart(){
  if(lossH.length<2)return;
  const cw=Math.min(180,W*0.15),ch=50,x0=W-cw-16,y0=H-ch-16;
  cx.fillStyle='rgba(17,17,25,0.92)';cx.strokeStyle='rgba(255,255,255,0.06)';cx.lineWidth=1;
  rRect(cx,x0,y0,cw,ch,6);cx.fill();rRect(cx,x0,y0,cw,ch,6);cx.stroke();
  cx.fillStyle='#6b6578';cx.font='500 8px "Space Grotesk"';cx.textAlign='left';cx.textBaseline='top';
  cx.fillText('LOSS',x0+8,y0+5);
  const last=lossH[lossH.length-1];
  cx.fillStyle='#ef4444';cx.font='500 9px "JetBrains Mono"';cx.textAlign='right';
  cx.fillText(last.toFixed(5),x0+cw-6,y0+5);
  const pad={l:6,r:6,t:20,b:6},pw=cw-pad.l-pad.r,ph=ch-pad.t-pad.b;
  const mx=Math.max(...lossH,0.0001);
  cx.beginPath();cx.strokeStyle='#ef4444';cx.lineWidth=1.2;
  for(let i=0;i<lossH.length;i++){
    const px=x0+pad.l+(i/(lossH.length-1))*pw;
    const py=y0+pad.t+(1-lossH[i]/mx)*ph;
    i===0?cx.moveTo(px,py):cx.lineTo(px,py);
  }
  cx.stroke();
}

function drawSigmoidCurve(nd){
  // Small σ curve diagram in bottom-left
  if(fStep<2)return;
  const cw=100,ch=70,x0=16,y0=H-ch-16;
  cx.fillStyle='rgba(17,17,25,0.92)';cx.strokeStyle='rgba(255,255,255,0.06)';cx.lineWidth=1;
  rRect(cx,x0,y0,cw,ch,6);cx.fill();rRect(cx,x0,y0,cw,ch,6);cx.stroke();
  cx.fillStyle='#6b6578';cx.font='500 8px "Space Grotesk"';cx.textAlign='left';cx.textBaseline='top';
  cx.fillText('SIGMOID σ(z)',x0+6,y0+4);
  const pad={l:14,r:10,t:18,b:14},pw=cw-pad.l-pad.r,ph=ch-pad.t-pad.b;
  // Axes
  cx.strokeStyle='#333';cx.lineWidth=0.5;
  cx.beginPath();cx.moveTo(x0+pad.l,y0+pad.t);cx.lineTo(x0+pad.l,y0+ch-pad.b);cx.lineTo(x0+cw-pad.r,y0+ch-pad.b);cx.stroke();
  // Curve
  cx.beginPath();cx.strokeStyle='#22d3a7';cx.lineWidth=1.5;
  for(let i=0;i<=pw;i++){
    const z=(i/pw)*8-4;
    const v=sig(z);
    const px=x0+pad.l+i,py=y0+ch-pad.b-v*ph;
    i===0?cx.moveTo(px,py):cx.lineTo(px,py);
  }
  cx.stroke();
  // Point for z1
  if(S.z1!==null){
    const v=sig(S.z1);
    const px=x0+pad.l+((S.z1+4)/8)*pw;
    const py=y0+ch-pad.b-v*ph;
    cx.beginPath();cx.arc(px,py,4,0,6.283);cx.fillStyle='#f59e0b';cx.fill();
    cx.fillStyle='#f59e0b';cx.font='500 8px "JetBrains Mono"';cx.textAlign='center';
    cx.fillText('z₁='+S.z1.toFixed(1),px,py-8);
  }
}

/* ===== Bias (explicit) ===== */
function spawnBP(bi,dir,col){for(let j=0;j<6;j++)bParticles.push({bi,dir,t:-j*0.1,spd:0.012+Math.random()*0.005,col,sz:2.2+Math.random()*1})}
function biasPos(nd){const off=Math.max(74,H*0.24);return[{x:nd.h.x,y:nd.h.y-off,t:'h',bi:0},{x:nd.yh.x,y:nd.yh.y-off,t:'yh',bi:1}]}
function biasFwd(bi){return bi===0?fStep>=1:fStep>=3}
function biasBwd(bi){return bi===0?bStep>=6:bStep>=3}
function arrowAt(ax,ay,ang,col,sz){cx.save();cx.translate(ax,ay);cx.rotate(ang);cx.beginPath();cx.moveTo(0,0);cx.lineTo(-sz,-sz*0.45);cx.lineTo(-sz,sz*0.45);cx.closePath();cx.fillStyle=col;cx.fill();cx.restore()}
function drawBiasEdges(nd){
  const bp=biasPos(nd);
  bp.forEach(p=>{
    const Rn=Math.max(28,Math.min(42,W*0.04)),tg={x:nd[p.t].x,y:nd[p.t].y-Rn*0.45},fa=biasFwd(p.bi),ba=biasBwd(p.bi);
    let col='#252535',lw=1.5;
    if(ba){col='#f97352';lw=2.5}else if(fa){col='#22d3a7';lw=2.5}
    if(fa||ba){cx.save();cx.shadowColor=col;cx.shadowBlur=12;cx.beginPath();cx.moveTo(p.x,p.y);cx.lineTo(tg.x,tg.y);cx.strokeStyle=col;cx.lineWidth=lw;cx.stroke();cx.restore()}
    cx.beginPath();cx.moveTo(p.x,p.y);cx.lineTo(tg.x,tg.y);cx.strokeStyle=col;cx.lineWidth=lw;cx.stroke();
    if(fa){const t2=0.86,ax=p.x+(tg.x-p.x)*t2,ay=p.y+(tg.y-p.y)*t2;arrowAt(ax,ay,Math.atan2(tg.y-p.y,tg.x-p.x),col,7)}
    else if(ba){const t2=0.14,ax=p.x+(tg.x-p.x)*t2,ay=p.y+(tg.y-p.y)*t2;arrowAt(ax,ay,Math.atan2(p.y-tg.y,p.x-tg.x),col,7)}
    const mx=p.x+(tg.x-p.x)*0.5,my=p.y+(tg.y-p.y)*0.5,lx=mx+30;
    const txt=BLBL[p.bi]+'='+S.b[p.bi].toFixed(2);
    cx.font='500 11px "JetBrains Mono"';cx.textAlign='center';cx.textBaseline='middle';
    const tw=cx.measureText(txt).width+12;
    cx.fillStyle='rgba(11,11,18,0.9)';rRect(cx,lx-tw/2,my-9,tw,18,5);cx.fill();
    cx.strokeStyle=ba?'rgba(249,115,82,0.3)':fa?'rgba(34,211,167,0.3)':'rgba(255,255,255,0.05)';cx.lineWidth=0.7;rRect(cx,lx-tw/2,my-9,tw,18,5);cx.stroke();
    cx.fillStyle=ba?'#f97352':fa?'#22d3a7':'#6b6578';cx.fillText(txt,lx,my);
    if(ba){
      const gv=p.bi===0?S.dLdb1:S.dLdb2,gt='∂L/∂'+BLBL[p.bi]+'='+gv.toFixed(4);
      cx.font='400 10px "JetBrains Mono"';
      const gtw=cx.measureText(gt).width+10;
      cx.fillStyle='rgba(11,11,18,0.9)';rRect(cx,lx-gtw/2,my+12,gtw,16,4);cx.fill();
      cx.fillStyle='#f97352';cx.fillText(gt,lx,my+20);
    }
  });
}
function drawBParticles(nd){
  const bp=biasPos(nd);
  bParticles.forEach(p=>{
    if(p.t<0||p.t>1)return;
    const o=bp[p.bi],tg={x:nd[o.t].x,y:nd[o.t].y-(Math.max(28,Math.min(42,W*0.04)))*0.45},tt=p.dir===1?p.t:1-p.t;
    const px=o.x+(tg.x-o.x)*tt,py=o.y+(tg.y-o.y)*tt;
    cx.save();cx.globalAlpha=Math.min(1,Math.min(p.t,1-p.t)*5);
    cx.shadowColor=p.col;cx.shadowBlur=9;
    cx.beginPath();cx.arc(px,py,p.sz,0,6.283);cx.fillStyle=p.col;cx.fill();cx.restore();
  });
}
function drawBiasNodes(nd){
  const bp=biasPos(nd),Rb=Math.max(13,Math.min(19,W*0.018));
  bp.forEach(p=>{
    const fa=biasFwd(p.bi),ba=biasBwd(p.bi),act=fa||ba;
    const col=ba?'#f97352':fa?'#22d3a7':'#333345';
    if(act){cx.save();cx.shadowColor=col;cx.shadowBlur=16;cx.beginPath();cx.arc(p.x,p.y,Rb,0,6.283);cx.fillStyle='rgba(0,0,0,0)';cx.fill();cx.restore()}
    cx.beginPath();cx.arc(p.x,p.y,Rb,0,6.283);
    const gr=cx.createRadialGradient(p.x-Rb*0.25,p.y-Rb*0.25,0,p.x,p.y,Rb);
    if(act){gr.addColorStop(0,col+'28');gr.addColorStop(1,col+'08')}else{gr.addColorStop(0,'#1c1c28');gr.addColorStop(1,'#12121c')}
    cx.fillStyle=gr;cx.fill();
    cx.strokeStyle=col;cx.lineWidth=act?2:1.2;cx.stroke();
    cx.fillStyle='#e8e4df';cx.font='600 '+Math.max(11,Rb*0.62)+'px "Space Grotesk"';cx.textAlign='center';cx.textBaseline='middle';
    cx.fillText('1',p.x,p.y);
  });
}

/* ===== Main loop ===== */
function draw(){
  const nd=nds();cx.clearRect(0,0,W,H);
  if(intro<1)intro=Math.min(1,intro+0.02);
  drawBg();drawEdges(nd);drawBiasEdges(nd);drawParticles(nd);drawBParticles(nd);drawNodes(nd);drawBiasNodes(nd);
  drawChainRule(nd);drawLossChart();drawSigmoidCurve(nd);
  document.getElementById('ov-yh').textContent=S.yh!==null?tv('yh').toFixed(4):'—';
  document.getElementById('ov-loss').textContent=S.loss!==null?tv('loss').toFixed(6):'—';
  particles.forEach(p=>p.t+=p.spd);particles=particles.filter(p=>p.t<=1.1);
  bParticles.forEach(p=>p.t+=p.spd);bParticles=bParticles.filter(p=>p.t<=1.1);
  requestAnimationFrame(draw);
}
requestAnimationFrame(draw);

/* ===== Hover ===== */
cv.addEventListener('mousemove',e=>{
  const r=cv.getBoundingClientRect(),mx=e.clientX-r.left,my=e.clientY-r.top;
  const nd=nds();hovNode=null;
  const R=Math.max(28,Math.min(42,W*0.04));
  for(const[n,p]of Object.entries(nd)){if((mx-p.x)**2+(my-p.y)**2<(R+8)**2){hovNode=n;break}}
  cv.style.cursor=hovNode?'pointer':'default';
});
cv.addEventListener('mouseleave',()=>{hovNode=null});

/* ===== Async helpers ===== */
const wait=ms=>new Promise(r=>setTimeout(r,ms));

/* ===== Buttons ===== */
document.getElementById('btn-fwd-s').onclick=()=>{stopAuto();doFwd()};
document.getElementById('btn-bwd-s').onclick=()=>{stopAuto();doBwd()};
document.getElementById('btn-fwd-a').onclick=async()=>{stopAuto();while(fStep<5){doFwd();await wait(300)}};
document.getElementById('btn-bwd-a').onclick=async()=>{stopAuto();while(bStep<6){doBwd();await wait(300)}};
document.getElementById('btn-update').onclick=()=>{stopAuto();doUpdate()};
document.getElementById('btn-train').onclick=async()=>{stopAuto();while(fStep<5){doFwd();await wait(150)}while(bStep<6){doBwd();await wait(150)}doUpdate()};
document.getElementById('btn-reset').onclick=()=>{stopAuto();clearLog();S.w=[0.4,-0.6];S.b=[0.1,-0.1];S.epoch=0;lossH.length=0;document.getElementById('val-epoch').textContent='0';writeSl();resetComp();toast('Reset')};
document.getElementById('btn-rand').onclick=()=>{stopAuto();resetComp();for(let i=0;i<2;i++)S.w[i]=Math.round((Math.random()*2-1)*40)/40;for(let i=0;i<2;i++)S.b[i]=Math.round((Math.random()*2-1)*40)/40;writeSl();toast('Randomized')};
document.getElementById('btn-clr').onclick=clearLog;

function stopAuto(){autoOn=false;const b=document.getElementById('btn-auto');b.classList.remove('btn-active');b.innerHTML='<i class="fas fa-play fa-xs"></i> Auto Train'}
async function autoLoop(){while(autoOn){if(fStep<5){doFwd();await wait(80)}else if(bStep<6){doBwd();await wait(80)}else{doUpdate();await wait(20)}}}
document.getElementById('btn-auto').onclick=()=>{if(autoOn){stopAuto();return}autoOn=true;const b=document.getElementById('btn-auto');b.classList.add('btn-active');b.innerHTML='<i class="fas fa-pause fa-xs"></i> Pause';autoLoop()};

/* ===== Modal ===== */
const modal=document.getElementById('modal');
const openModal=()=>modal.classList.add('show');
const closeModal=()=>modal.classList.remove('show');
document.getElementById('btn-help').onclick=openModal;
document.getElementById('modal-x').onclick=closeModal;
modal.addEventListener('click',e=>{if(e.target===modal)closeModal()});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal()});

/* ===== Init ===== */
writeSl();
addLog('<span style="color:var(--muted)">Network: x → σ(w₁x+b₁) → σ(w₂h+b₂) → ½(ŷ−t)²</span>');
addLog('<span style="color:var(--muted)">Step through <b>Forward</b>, then <b>Backward</b>, then <b>Update</b> to see the chain rule in action.</span>');
})();
</script>
</body>
</html>
```

- I need to reason deeply about the chain rule.
- I need to reason deeply about the cost function - and better names - that I Should Give It.

## 🗂️ Index

## ❓ QA

- What is the relation between **Gradient Descent** and **Backpropagation**? **Backprop answers**: *“How much does this parameter affect the loss?” vs* **Gradient Descent answers**: *“How should I change this parameter to reduce the loss?”.*
- How can someone have arrived to these ideas? Which was the idea path that lead to this?
- How back **propagation works**?
- How to monitor the **training process**?
- What is the **semantics** and name of the  **`(@)`** operator?
- Is the loss function a **local** (data point) or **global** (the entire dataset) metric in **Batch Gradient Descent**?
- Which alternatives to optimization methods exists to Gradient Descent*?
- How to characterize a **$n$** optimization method?
- Why is the error derivative in backpropagation taken with respect to the pre-activation $z$ rather than the activation $a$?
- Why $z$ denotes the pre-activiation?  **Historical/Math Convention**: In mathematics, $z$
 often denotes an intermediate variable in functions or transformations.  Since pre-activation is an intermediate state (between the linear  transform and activation function), $z$ naturally fits.
- How to think deeply about backprogation? Which is the set of minimal ideas required to derivate the algorithm?
- How can I deeply understand backpropagation using the idea of perturbation — thinking of propagation and weight adjustments as “reverse engineering the perturbations”?
- What is a **local gradient**?
- Do different neural network architectures require adaptations or modifications to the standard backpropagation algorithm?
- **Mathematical Foundations**
    - Derive backpropagation from first principles using Lagrangian multipliers for a feedforward network. Why does this yield the same result?
    - Prove that backpropagation is an application of reverse-mode automatic differentiation. How does this compare in computational complexity to forward-mode AD?
    - Show how the chain rule is expressed in tensor notation for a multilayer perceptron. How do you deal with broadcasting during derivative computation?
    - In a general computation graph, how do you formalize the derivative of a scalar loss with respect to an arbitrary node using dual numbers?
    - What is the Jacobian of a layer with respect to its parameters and why is it not computed explicitly during backprop?
    - Given a composite function $f(g(h(x)))$, under what conditions is the gradient computation via backprop stable?
- **Implementation-Level Deep Dives**
    - In practice, why do we compute gradients with respect to pre-activations $z^{(\ell)}$ instead of activations $a^{(\ell)}$?
    - Describe how backpropagation works in a network with weight-sharing (e.g., convolutional neural nets). How is the gradient aggregated?
    - Explain how backpropagation handles parameter tying or constraints (e.g., symmetric weight matrices).
    - How does backpropagation differ in recurrent networks? Derive the gradient for an unrolled RNN across time steps.
    - What optimizations are possible to reduce memory usage during backpropagation in deep networks (e.g., checkpointing)?
    - How would you implement backpropagation for a network with custom non-differentiable operations (e.g., argmax)? What techniques can you use?
- **Numerical Precision and Stability**
    - Why is softmax + cross-entropy gradient computation numerically unstable, and how is it typically stabilized?
    - Why do **vanishing and exploding gradients** occur specifically during backpropagation through time?
    - What role does the condition number of the Jacobian matrix play in gradient stability during backpropagation?
    - Explain the effect of float16 vs float32 in gradient accumulation and how mixed-precision training preserves accuracy.
    - How does gradient checkpointing reduce memory usage in backpropagation? Derive the trade-off between recomputation and memory savings.
- **Advanced Architectures and Backprop Variants**
    - How is backpropagation adapted for attention-based mechanisms (e.g., self-attention in transformers)?
    - How does gradient flow change in ResNets vs plain MLPs? What is the theoretical explanation for better trainability?
    - What is synthetic gradient and how does it bypass backpropagation’s need for sequential layer-wise updates?
    - Compare target propagation, feedback alignment, and equilibrium propagation to classical backpropagation. What assumptions are relaxed in each?
    - **Derive the backpropagation equations for an LSTM cell**, including the flow of gradients through the forget, input, and output gates.
    - **How does backpropagation through time (BPTT) differ from standard backprop?** What are the challenges in very long sequences?
    - **Explain how second-order optimization (e.g., Hessian-free, K-FAC) modifies backpropagation.** How does it approximate the inverse Hessian?
    - **What is the role of implicit differentiation in backpropagation** for systems with equilibrium states (e.g., Deep Equilibrium Models)?
- 📐 **Geometric and Statistical Intuitions**
    - Interpret the backpropagation gradient geometrically in weight space. How does it relate to the gradient of a scalar field?
    - How does the curvature of the loss surface affect the path taken by backpropagation? How is this addressed in second-order methods?
    - Why is backpropagation not biologically plausible? What parts of the algorithm break biological constraints?
- **Debugging & Practical Challenges**
    - **How would you diagnose a neural network where gradients are zero during backprop?** Provide a systematic debugging approach.
    - **What are the implications of non-differentiable operations (e.g., `argmax`, `ReLU` at 0) in backpropagation?** How are they handled in practice?
    - **Explain how gradient clipping mitigates instability in backpropagation.** What are the trade-offs between different clipping strategies (global vs. layer-wise)?
    - **How does batch normalization affect gradient flow during backprop?** Derive the gradients through the batch norm layer.
- **Theoretical Limits & Alternatives**
    - **Can backpropagation be replaced by biologically plausible alternatives (e.g., predictive coding, feedback alignment)?** What are their limitations?
    - **What is the computational complexity of backpropagation** for a transformer model with `N` layers and `d` attention heads?
    - **How does backpropagation scale in distributed training (e.g., data vs. model parallelism)?** Explain gradient synchronization challenges.
    - **What are the fundamental limits of backpropagation** in terms of credit assignment over very long horizons (e.g., reinforcement learning)?
- Why we use the derivative of the loss with respect to the pre-activations (z) and not directly with respect to the weights? Well the parameters → pre-activiations;  …
- How do we update the **parameters** using the **derivative** of the loss with respect to the **pre-activations** (z)?

## **✅ Note Quality Evaluation** ⭐⭐

> (**⭐⭐⭐⭐⭐**)  → Does this note adhere to the prototype structure? If it is incomplete, in what way? See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21).
> 

> ⭐⭐: Some value, but incomplete or poorly aligned with the prototype. Needs significant refinement.
> 

## 📘 Breviarium

> A comprehensive exploration of the topic.
> 

> **Nucleus (🧬)** → Deepest Essence (What is the deepest essence?)
> 

> **Telos (🎯)** → Intent (What is it for? Toward what end is it directed?)
> 

> **Techne (🛠️)** → Function / Used (By what craft or process is it made to work?)
> 

> **Idoneitas (📏)** → Suitability (How well is it fitted for its purpose?)
> 

> **Limites** (🚧) → Limits (What are its boundaries? What constraints define its operation?)
> 

> **Contextus (🌐)** → Context (What is the historical, cultural, or situational context in which this study occurs?)
> 

## 🧠 Autovaluation

> What is my **epistemic assessment** of **Backpropagation** this topic? How well do I understand this subject?
> 

> This topics really required several passes; in order to better understand everything; it’s  an extremaly powerful concept;  probably the most general in mathematics;  function optimization in streamly high dimension spaces.
> 

> **Note:** One cannot seriously expect to understand the topic in one go. It will be a notice that the topic is either near to our field of expertise; or it’s streamly rich.
> 

## 📘 Study Guide

> The backpropagation algorithm is very difficult to learn because the online material is just horrible (not notation clarification; basic one dimensional example;  un clear cost / loss function / unclear meaning of pronating error back; on how that helps in updating the weights;  in the introduction they give the specification of the weight update; but this is not the strategy;  and more failures).
> 

> Note: This is not **easy** to take your time; several passes read other blogs; try to read; run examples;  take a bit of time off;  go back;  It’s key to understand Backdrop since all **Neural Networks (NN)** is about representation + evaluation + optimization.
> 

> Another problem is the notational difference between tutorials to denotes the parts of the computational graph structure.
> 

Understanding Path:

- Surface Level (basic equations, mechanical calculation):
    - You can learn how to compute gradients by following examples.
    - You can implement backprop for simple networks (1–2 hidden layers).
- Working Understanding (intuition + implementation):
    - You feel why the chain rule is used.
    - You understand how the error flows back.
    - You can implement backprop manually without "just copying formulas.”
    - You can debug when your network doesn't learn.
- Deep Understanding (theory + optimization issues):
    - You know *why* backprop sometimes fails (e.g., vanishing/exploding gradients).
    - You can modify backprop to work with architectures like CNNs, RNNs.
    - You understand second-order methods (e.g., Hessians), advanced tricks like BatchNorm, Residual connections.
    - You understand backprop as applied to **computational graphs** and automatic differentiation.
- Very Deep (Researcher Level):
    - Variants of backpropagation
    - Limitations (biological plausibility, efficiency)
    - Alternatives like Target Propagation, Feedback Alignment
    - Backprop through time (BPTT) for sequences
    - Neural tangent kernels, implicit differentiation

## TODO

- [ ]  Use tinigrad
- [ ]  Compare my network training with sklearn
- [ ]  Realtime graph of the loss function
- [ ]  Checkpoints
- [ ]  Weight Store / Upload
- [ ]  Inference Engine
- [ ]  How to think about NN → Learnig Representations, Features Detectors.
- [ ]  https://github.com/karpathy/minGPT

## ✍️Formulation

> Backpropagation, short for **backward propagation of errors**, is a central algorithm used to compute gradients of the loss function with respect to the weights in a neural network. It leverages the **chain rule of calculus** to propagate the error signal backward through the layers of the network, enabling gradient-based optimization methods such as **Stochastic Gradient Descent (SGD)** or **Adam**.
> 

![image.png](../assets/note/epistemica/optimization/backpropagation/image.png)

### 📌 Preliminaries

Let a neural network be a composition of functions:

$f(x; \theta) = f^{(L)} \circ f^{(L-1)} \circ \cdots \circ f^{(1)}(x)$

- $x \in \mathbb{R}^{n_0}$: input
- $\theta$: set of all weights and biases
    - $W^{(\ell)} \in \mathbb{R}^{n_\ell \times n_{\ell-1}}$: weight matrix
    - $b^{(\ell)} \in \mathbb{R}^{n_\ell}$: bias vector
- $f^{(\ell)}$: function computed at layer $\ell$
- $L$: number of layers (output layer is $L$)

Computation:

- $L$ = loss function (e.g., MSE, cross-entropy)
- $\sigma(\cdot)$ = activation function (e.g., ReLU, sigmoid)
- $z^{(\ell)} = W^{(\ell)} a^{(\ell-1)} + b^{(\ell)}$ = pre-activation values
- $a^{(\ell)} = \sigma^{(\ell)}(z^{(\ell)})$;  activations of layer $l$
- $\delta^l$ = error at layer $l$ (gradient of loss w.r.t. $z^l$)

### 🔁 **What is $\delta^l$?**

> In backpropagation, the error term at layer ll, denoted: $\delta^l = \frac{\partial \mathcal{L}}{\partial z^l}$ is the **partial derivative of the loss function $\mathcal{L}$** with respect to the **pre-activation** value $z^l$ of layer $l$.
> 

$\delta^l$ **is a derivative** — but it’s **not** the derivative of the loss with respect to the weights or outputs directly. Instead:

- $\delta^l$ is a "local" gradient that helps you build up to computing the gradients of $\mathcal{L}$ w.r.t. the weights and biases.
- It's used to **chain the gradients backwards** using the chain rule.

### 🚀 **Forward Pass**

> Compute for each layer $l$:
> 
- $z^l = W^l a^{l-1} + b^l$
- $a^l = \sigma(z^l)$

### **🔁 Backward Pass** (Error Signal Propagation)

> **Goal**: compute $\nabla_\theta \mathcal{L}$, i.e., the gradient of the loss with respect to all trainable parameters.
> 

> Let  $\delta^{(\ell)} = \frac{\partial \mathcal{L}}{\partial z^{(\ell)}} \in \mathbb{R}^{n_\ell}$  be  the **error signal** at layer $\ell$, i.e., the gradient of the loss w.r.t. in the pre-activation $z^{(\ell)}$.
> 

- Start from the output layer $L$: $\delta^L = \nabla_{a^L} \mathcal{L} \odot \sigma'(z^L)$ ; Where $\odot$ is element-wise multiplication.
- Then for hidden layers $l=L−1,...,1$ ;  $\delta^l = ((W^{l+1})^T \delta^{l+1}) \odot \sigma'(z^l)$

### **🧮 Gradient Computation**

> The gradients of the loss w.r.t. weights and biases:
> 
- $\frac{\partial \mathcal{L}}{\partial W^l} = \delta^l (a^{l-1})^T$
- $\frac{\partial \mathcal{L}}{\partial b^l} = \delta^l$

## **🔧 Parameters Updates**

> 🚨 This **is wrong**; fix the **recurrence here**.
> 

> Using learning rate $\eta$:
> 
- $W^l := W^l - \eta \frac{\partial \mathcal{L}}{\partial W^l}$ → $W^l - \eta \delta^l (a^{l-1})^T$
- $b^l := b^l - \eta \frac{\partial \mathcal{L}}{\partial b^l}$ →   $b^l - \eta \delta^l$

## 💻 Computational Complexity

> 
- **Backpropagation** reuses intermediate results from the forward pass (e.g., $z^{(\ell)}$,  $a^{(\ell)})$, avoiding recomputation.
- Efficiently implemented using **computational graphs** and **automatic differentiation**.
- Time complexity per sample: $O(N)$ where $N$ is a number of parameters.

## 📊 Case Study

- [ ]  [Concrete Strength](https://app.notion.com/p/Concrete-Strength-1d7c0f5171ec8066b7f8c9a058ed850e?pvs=21)

## ❓ QA

### Why is it necessary to use the weights from the next layer when computing the gradient of the loss with respect to the current layer's activations during backpropagation?

> Backpropagation computes the **gradient of the loss** with respect to each weight in the network, layer by layer from the **output** back to the **input**.
> 

Let’s say you have a 3-layer feedforward network:

```
Input → [Layer 1] → [Layer 2] → [Layer 3] → Output
```

```c
dL_da2 = dL_dy @ W3.T               # Pull error from Layer 3 back to Layer 2
dL_dz2 = dL_da2 * relu_derivative(z2)  # Apply derivative of activation (ReLU)
dL_dW2 = a1.T @ dL_dz2              # Get gradient w.r.t. W2
dL_db2 = np.sum(dL_dz2, axis=0)     # Gradient w.r.t. bias
```

Let’s focus on computing the gradient for **Layer 2**, but to do that, we need:

- The **gradient of the loss** w.r.t. the **activation output** of Layer 2 (denoted as `a2`)
- That means we need to "pull back" the error from **Layer 3** to **Layer 2**

⛓️ Chain Rule in Action:

- To get the gradient of the loss $\mathcal{L}$ with respect to $z_2$, you apply the **chain rule**: $\frac{\partial \mathcal{L}}{\partial z_2} = \frac{\partial \mathcal{L}}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2}$
- But here’s the catch: $\frac{\partial \mathcal{L}}{\partial a_2} = \frac{\partial \mathcal{L}}{\partial z_3} \cdot W_3^T$

So the **gradient of the loss with respect to $a_2$** depends on:

- The **gradient flowing back from Layer 3**
- The **weights $W_3$** of Layer 3

🧠 Intuition: Imagine the loss is like a ripple that starts at the output. To understand how much Layer 2 contributed to that loss, you need to know:

- How sensitive the output is to changes in Layer 2
- That sensitivity is filtered through the weights $W_3$ of the next layer

## Simulation

> Computation Graph + Gradient Flow.
> 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Editable Computation Graph</title>
  <script src="https://unpkg.com/cytoscape/dist/cytoscape.min.js"></script>
  <style>
    #cy { width: 800px; height: 500px; border: 1px solid #ccc; }
    #controls { margin-top: 10px; font-family: sans-serif; }
    input[type="number"] { width: 60px; }
    .node-input, .edge-weight { margin: 5px 0; }
  </style>
</head>
<body>
  <h2>Editable Computation Graph</h2>
  <div id="cy"></div>

  <div id="controls">
    <h3>Inputs</h3>
    <div id="inputs"></div>

    <h3>Edge Weights</h3>
    <div id="weights"></div>

    <h3>Output</h3>
    <pre id="output">Press "Simulate"</pre>
    <button onclick="simulate()">Simulate</button>
  </div>

  <script>
    const nodes = [
      { id: 'A', type: 'input', value: 2 },
      { id: 'B', type: 'input', value: 3 },
      { id: 'Add', type: 'add' },
      { id: 'Mul', type: 'multiply' },
      { id: 'Out', type: 'output' }
    ];

    const edges = [
      { source: 'A', target: 'Add', weight: 1 },
      { source: 'B', target: 'Add', weight: 1 },
      { source: 'Add', target: 'Mul', weight: 1 },
      { source: 'B', target: 'Mul', weight: 1 },
      { source: 'Mul', target: 'Out', weight: 1 }
    ];

    const cy = cytoscape({
      container: document.getElementById('cy'),
      elements: [
        ...nodes.map(n => ({
          data: { id: n.id, label: `${n.id}${n.value !== undefined ? `: ${n.value}` : ''}`, type: n.type },
          position: { x: Math.random() * 500 + 100, y: Math.random() * 300 + 100 }
        })),
        ...edges.map(e => ({
          data: { id: `${e.source}->${e.target}`, source: e.source, target: e.target, weight: e.weight }
        }))
      ],
      style: [
        {
          selector: 'node',
          style: {
            'label': 'data(label)',
            'background-color': ele => {
              const type = ele.data('type');
              if (type === 'input') return '#0074D9';
              if (type === 'output') return '#FF851B';
              return '#2ECC40';
            },
            'color': '#fff',
            'text-valign': 'center',
            'text-halign': 'center',
            'padding': '10px'
          }
        },
        {
          selector: 'edge',
          style: {
            'width': 2,
            'label': ele => `w=${ele.data('weight')}`,
            'line-color': '#ccc',
            'target-arrow-shape': 'triangle',
            'target-arrow-color': '#ccc',
            'text-background-opacity': 1,
            'text-background-color': '#fff',
            'text-background-shape': 'roundrectangle',
            'text-margin-y': -10
          }
        }
      ]
    });

    const renderInputs = () => {
      const container = document.getElementById('inputs');
      container.innerHTML = '';
      nodes.filter(n => n.type === 'input').forEach(n => {
        const div = document.createElement('div');
        div.className = 'node-input';
        div.innerHTML = `${n.id}: <input type="number" id="input-${n.id}" value="${n.value}">`;
        container.appendChild(div);
      });
    };

    const renderWeights = () => {
      const container = document.getElementById('weights');
      container.innerHTML = '';
      edges.forEach(e => {
        const div = document.createElement('div');
        div.className = 'edge-weight';
        div.innerHTML = `${e.source} → ${e.target}: <input type="number" id="weight-${e.source}-${e.target}" value="${e.weight}" step="0.1">`;
        container.appendChild(div);
      });
    };

    const simulate = () => {
      const values = {};

      // Update input values
      nodes.filter(n => n.type === 'input').forEach(n => {
        const inputEl = document.getElementById(`input-${n.id}`);
        n.value = parseFloat(inputEl.value);
        values[n.id] = n.value;
        cy.getElementById(n.id).data('label', `${n.id}: ${n.value}`);
      });

      // Update edge weights
      edges.forEach(e => {
        const weightEl = document.getElementById(`weight-${e.source}-${e.target}`);
        e.weight = parseFloat(weightEl.value);
        const edgeId = `${e.source}->${e.target}`;
        cy.getElementById(edgeId).data('weight', e.weight);
      });

      // Evaluate nodes in topological order
      const order = ['A', 'B', 'Add', 'Mul', 'Out'];
      for (const nodeId of order) {
        const node = nodes.find(n => n.id === nodeId);
        if (node.type === 'add' || node.type === 'multiply' || node.type === 'output') {
          const incoming = edges.filter(e => e.target === nodeId);
          const inputs = incoming.map(e => values[e.source] * e.weight);
          let result = 0;
          if (node.type === 'add') {
            result = inputs.reduce((a, b) => a + b, 0);
          } else if (node.type === 'multiply') {
            result = inputs.reduce((a, b) => a * b, 1);
          } else {
            result = inputs[0]; // Output just passes through
          }
          values[nodeId] = result;
          cy.getElementById(nodeId).data('label', `${nodeId}: ${result.toFixed(2)}`);
        }
      }

      document.getElementById('output').textContent = `Output: ${values['Out'].toFixed(2)}`;
    };

    renderInputs();
    renderWeights();
  </script>
</body>
</html>
```

## 📚 References

- [General Topic Note Template](https://app.notion.com/p/General-Topic-Note-Template-1cec0f5171ec801e86e6c894702cfe23?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- https://en.wikipedia.org/wiki/Backpropagation
- https://github.com/dbremont/algorithms/blob/main/opm/gd.ipynb
- https://en.wikipedia.org/wiki/Automatic_differentiation
- http://neuralnetworksanddeeplearning.com/chap2.html
- [https://ieeexplore.ieee.org/document/118638](https://ieeexplore.ieee.org/document/118638)
- https://huggingface.co/blog/andmholm/what-is-automatic-differentiation
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- https://arxiv.org/abs/2305.07546
- https://colah.github.io/posts/2015-08-Backprop/
- https://arxiv.org/abs/1502.05767
- https://danieltakeshi.github.io/2017/01/21/understanding-higher-order-local-gradient-computation-for-backpropagation-in-deep-neural-networks/
- https://www.cl.cam.ac.uk/archive/mjcg/plans/Backpropagation.html
- https://www.briandolhansky.com/blog/2013/9/27/artificial-neural-networks-backpropagation-part-4
- https://dustinstansbury.github.io/theclevermachine/derivation-backpropagation
- https://dl.acm.org/doi/10.5555/3327546.3327682
- [ ]  [‣](https://app.notion.com/p/10e598edb790811da00deca89d07c17b?pvs=21)
- [ ]  Origins
    - [ ]  https://link.springer.com/chapter/10.1007/BFb0006203
    - [ ]  https://zenodo.org/records/1262035
    - [ ]  https://dl.acm.org/doi/abs/10.1007/BF01931367
    - [ ]  [Amari, Shun'ichi](https://en.wikipedia.org/wiki/Shun%27ichi_Amari) (1967). "A theory of adaptive pattern classifier". *IEEE Transactions*. **EC** (16): 279–307.
    - [ ]  https://arxiv.org/abs/2212.11279
- [ ]  https://en.wikipedia.org/wiki/Gradient
- [ ]  https://en.wikipedia.org/wiki/Gradient_descent
