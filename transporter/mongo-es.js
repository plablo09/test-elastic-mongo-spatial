pipeline = Source({name:"mongo", tail: true, namespace: "twitter.tweets"})
  .transform({filename: "transformers/passthrough_and_log.js", namespace: "twitter.tweets"})
  .save({name:"es", namespace: "twitter.tweets"})
