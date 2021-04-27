import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';


const B = (props) => <Text style={{fontWeight: 'bold'}}>{props.children}</Text>

const FeatureList = [
  {
    title: '1. Humans label images ...',
    Svg: require('../../static/img/doodler-logo.svg').default,
    description: (
      <>
        We label pixels in images corresponding to a pre-determined set of classes. We have built a special program for this, called "Doodler".
      </>
    ),
  },
  {
    title: '2. Models are trained to mimic humans ...',
    Svg: require('../../static/img/zoo-logo.svg').default,
    description: (
      <>
        We use the labels to train sophisticated Machine Learning models to mimic what a human could achieve. We have built a special program for this too, called "Zoo".
      </>
    ),
  },
  {
    title: '3. Use these models to label images instead of humans',
    Svg: require('../../static/img/example.svg').default,
    description: (
      <>
        Once we have trained the models to label images, they can be applied to tens of thousands or even millions of individual images, which collectively can be used for many scientific applications. Click 'About' at the top of this page to begin.
      </>
    ),
  },

];


function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
