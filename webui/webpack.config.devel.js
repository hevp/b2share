var path = require('path');
var webpack = require('webpack');

module.exports = {
    mode: 'development',
    entry: './src/main.jsx',
    devtool: 'cheap-module-eval-source-map',
    output: {
        path: __dirname+"/app",
        filename: 'b2share-bundle.js'
    },
    plugins: [
    ],
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                use: {
                    loader: 'babel-loader',
                },
                exclude: /node_modules/,
                include: path.join(__dirname, 'src')
            }
        ]
    }
};
