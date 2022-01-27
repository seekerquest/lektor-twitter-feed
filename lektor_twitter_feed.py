# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from markupsafe import Markup

TEMPLATE = '''
    <a class="twitter-timeline" href="https://twitter.com/%(SCREEN_NAME)s">Tweets by %(SCREEN_NAME)s</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
'''


class TwitterFeedPlugin(Plugin):
    name = 'twitter-feed'
    description = u'Lektor plugin to add Twitter feed snippets to a website.'

    # def on_process_template_context(self, context, **extra):
    #     def test_function():
    #         return 'Value from plugin %s' % self.name
    #     context['test_function'] = test_function

    def on_setup_env(self, **extra):
        screen_name = self.get_config().get('SCREEN_NAME')

        if screen_name is None:
            raise RuntimeError('SCREEN_NAME is not configured.'
                               'Please configure it in '
                               '`./configs/twitter-feed.ini` file')

        def render_twitter_feed():
            return Markup(TEMPLATE % {'SCREEN_NAME': screen_name})

        self.env.jinja_env.globals['render_twitter_feed'] = render_twitter_feed
