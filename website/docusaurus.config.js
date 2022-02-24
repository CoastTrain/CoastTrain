/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'CoastTrain',
  tagline: 'Labeled images of coastal environments for training Machine Learning classification models.',
  url: 'https://dbuscombe-usgs.github.io',
  baseUrl: '/CoastTrain/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'dbuscombe-usgs', // Usually your GitHub org/user name.
  projectName: 'CoastTrain', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: '',
      logo: {
        alt: 'CoastTrain',
        src: 'img/Coast_train_logo.jpg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Project Information',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/Doodleverse/',
          label: 'Coast Train is made possible by the Doodleverse',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Project Information',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Doodler',
              href: 'https://dbuscombe-usgs.github.io/dash_doodler/',
            },
            {
              label: 'The Doodleverse',
              href: 'https://github.com/Doodleverse',
            },
            {
              label: 'Coastal Image Labeler by Dr Evan Goldstein',
              href: 'https://coastalimagelabeler.science/',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'Doodler github',
              href: 'https://github.com/dbuscombe-usgs/dash_doodler',
            },
            {
              label: 'Makesense.ai (an alternative way to segment imagery)',
              href: 'https://www.makesense.ai/',
            },
          ],
        },

      ],
      copyright: `This website is written and maintained by Daniel Buscombe, Marda Science, LLC, contracted to the U.S. Geological Survey Pacific Coastal and Marine Science Center in Santa Cruz, CA, on behalf of the Coast Train team. Coast Train is funded by the U.S. Geological Survey Community for Data Integration, and is for the primary usage of U.S. Geological Survey scientists, researchers and affiliated colleagues working on coastal hazards, processes, and ecosystems research. Copyright © ${new Date().getFullYear()} Marda Science, LLC. `,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/dbuscombe-usgs/CoastTrain/edit/master/website/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/dbuscombe-usgs/CoastTrain/edit/master/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
