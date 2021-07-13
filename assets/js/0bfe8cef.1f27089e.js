(window.webpackJsonp=window.webpackJsonp||[]).push([[7],{119:function(e,t,r){"use strict";r.d(t,"a",(function(){return d})),r.d(t,"b",(function(){return h}));var n=r(0),a=r.n(n);function s(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function o(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){s(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},s=Object.keys(e);for(n=0;n<s.length;n++)r=s[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(n=0;n<s.length;n++)r=s[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var l=a.a.createContext({}),u=function(e){var t=a.a.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):o(o({},t),e)),r},d=function(e){var t=u(e.components);return a.a.createElement(l.Provider,{value:t},e.children)},b={inlineCode:"code",wrapper:function(e){var t=e.children;return a.a.createElement(a.a.Fragment,{},t)}},p=a.a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,s=e.originalType,i=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),d=u(r),p=n,h=d["".concat(i,".").concat(p)]||d[p]||b[p]||s;return r?a.a.createElement(h,o(o({ref:t},l),{},{components:r})):a.a.createElement(h,o({ref:t},l))}));function h(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var s=r.length,i=new Array(s);i[0]=p;var o={};for(var c in t)hasOwnProperty.call(t,c)&&(o[c]=t[c]);o.originalType=e,o.mdxType="string"==typeof e?e:n,i[1]=o;for(var l=2;l<s;l++)i[l]=r[l];return a.a.createElement.apply(null,i)}return a.a.createElement.apply(null,r)}p.displayName="MDXCreateElement"},74:function(e,t,r){"use strict";r.r(t),r.d(t,"frontMatter",(function(){return i})),r.d(t,"metadata",(function(){return o})),r.d(t,"toc",(function(){return c})),r.d(t,"default",(function(){return u}));var n=r(3),a=r(7),s=(r(0),r(119)),i={sidebar_position:2},o={unversionedId:"classes/naip-classes",id:"classes/naip-classes",isDocsHomePage:!1,title:"NAIP Imagery",description:"\x3c!--",source:"@site/docs/classes/naip-classes.md",sourceDirName:"classes",slug:"/classes/naip-classes",permalink:"/CoastTrain/docs/classes/naip-classes",editUrl:"https://github.com/dbuscombe-usgs/CoastTrain/edit/master/website/docs/classes/naip-classes.md",version:"current",sidebarPosition:2,frontMatter:{sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"Satellite Imagery",permalink:"/CoastTrain/docs/classes/satellite-classes"},next:{title:"USGS Orthomosaic Imagery",permalink:"/CoastTrain/docs/classes/usgs-classes"}},c=[{value:"1. Water",id:"1-water",children:[]},{value:"2. Whitewater",id:"2-whitewater",children:[]},{value:"3. Sand",id:"3-sand",children:[]},{value:"4. Vegetated terrain - herbaceous",id:"4-vegetated-terrain---herbaceous",children:[]},{value:"5. Vegetated terrain - woody",id:"5-vegetated-terrain---woody",children:[]},{value:"6. Other natural terrain",id:"6-other-natural-terrain",children:[]},{value:"7. Developed",id:"7-developed",children:[]},{value:"8. Unusual",id:"8-unusual",children:[]},{value:"9. Unknown",id:"9-unknown",children:[]}],l={toc:c};function u(e){var t=e.components,r=Object(a.a)(e,["components"]);return Object(s.b)("wrapper",Object(n.a)({},l,r,{components:t,mdxType:"MDXLayout"}),Object(s.b)("h3",{id:"1-water"},"1. Water"),Object(s.b)("p",null,"Ocean, lakes, rivers, lagoons, estuaries, creeks, inlets, etc"),Object(s.b)("h3",{id:"2-whitewater"},"2. Whitewater"),Object(s.b)("p",null,"This is breaking and broken waves in the surf and swash of open-coast environments, and also whitewater in rivers."),Object(s.b)("h3",{id:"3-sand"},"3. Sand"),Object(s.b)("p",null,"On beaches, dunes, etc, where it is apparently that the sand is bare or mostly bare (i.e. free from vegetation) - otherwise, use 'vegetated terrain' defined below"),Object(s.b)("h3",{id:"4-vegetated-terrain---herbaceous"},"4. Vegetated terrain - herbaceous"),Object(s.b)("p",null,"Any natural surface that is significantly vegetated, by herbaceous (non-woody) vegetation such as grasses."),Object(s.b)("h3",{id:"5-vegetated-terrain---woody"},"5. Vegetated terrain - woody"),Object(s.b)("p",null,"Any natural surface that is significantly vegetated, by woody vegetation such as trees and shrubs."),Object(s.b)("h3",{id:"6-other-natural-terrain"},"6. Other natural terrain"),Object(s.b)("p",null,"Only natural surfaces that are not sand or vegetated, such as steep cliffs"),Object(s.b)("h3",{id:"7-developed"},"7. Developed"),Object(s.b)("p",null,"Roads, buildings, paved areas such as parking lots, but not parks, golf courses, etc ; they are 'other natural terrain'"),Object(s.b)("h3",{id:"8-unusual"},"8. Unusual"),Object(s.b)("p",null,"Genuine cases for where it is possible to tell what it is, but it is a category not listed. This is usually an 'unusual' thing in the scene. For example, a boat at sea, or an algal bloom, etc. These portions of the imagery will be reclassified later."),Object(s.b)("h3",{id:"9-unknown"},"9. Unknown"),Object(s.b)("p",null,"Genuine cases where it is impossible to tell, from texture/color and spatial context. Use sparingly"))}u.isMDXComponent=!0}}]);