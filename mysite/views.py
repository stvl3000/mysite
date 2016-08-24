#-*- coding:utf-8 -*-

from django.http import HttpResponse

def index(request):
    httpString = """
    <head>
    <meta http-equiv="refresh" content="5;url=polls/">
    </head>
    <body>
    Hi there, welcome to my site.<br/>You will be redirected to <font color="blue">polls</font> page.
    <ul>
    <li><a href="polls/">polls</a></li>
    <li><a href="admin/">admin</a></li>
    </ul>
    </body>
    """
    return HttpResponse(httpString)



def index_temp(request):        
    
    htmlstring = """<!DOCTYPE html><html lang="en" class=" mdzr-js mdzr-borderradius mdzr-boxshadow mdzr-cssanimations mdzr-svg"><head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="ROBOTS" content="ALL">
    <meta http-equiv="imagetoolbar" content="no">
    <meta name="MSSmartTagsPreventParsing" content="true">
    <meta name="Copyright" content="Django Software Foundation">
    <meta name="keywords" content="Python, Django, framework, open-source">
    <meta name="description" content="">

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="https://www.djangoproject.com/s/img/icon-touch.e4872c4da341.png">
    <link rel="icon" sizes="192x192" href="https://www.djangoproject.com/s/img/icon-touch.e4872c4da341.png">
    <link rel="shortcut icon" href="https://www.djangoproject.com/s/img/favicon.6dbf28c0650e.ico">
    <meta name="msapplication-TileColor" content="#113228">
    <meta name="msapplication-TileImage" content="https://www.djangoproject.com/s/img/icon-tile.b01ac0ef9f67.png">

    <title>My Django site from scratch</title>

    <!--[if lte IE 8]>
        <link rel="stylesheet" href="https://www.djangoproject.com/s/css/output-ie.1b9cf0397c55.css" >
     <![endif]-->
    <!--[if gt IE 8]><!-->
        <link rel="stylesheet" href="https://www.djangoproject.com/s/css/output.fa0469ada9bd.css">
    <!--<![endif]-->
    <script src="https://www.djangoproject.com/s/js/lib/webfontloader/webfontloader.e75218f5f090.js"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400italic,700italic,300,700,400&amp;subset=latin"><script>
    WebFont.load({
      custom: {
        families: ['FontAwesome', 'Fira+Mono'],
      },
      google: {
        families: ['Roboto:400italic,700italic,300,700,400:latin'
        ]
      },
      classes: false,
      events: false,
      timeout: 1000
    });
    </script>
    <script src="https://www.djangoproject.com/s/js/lib/modernizr.3b36762e418a.js"></script>
    
      <script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="main.e3fa98aeaa99" src="https://www.djangoproject.com/s/js/main.e3fa98aeaa99.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mod/mobile-menu" src="https://www.djangoproject.com/s/js/mod/mobile-menu.841726ee903a.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mod/list-feature" src="https://www.djangoproject.com/s/js/mod/list-feature.73529480f25b.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="jquery" src="https://www.djangoproject.com/s/js/lib/jquery/dist/jquery.min.87e69028f78d.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="jquery.inview" src="https://www.djangoproject.com/s/js/lib/jquery.inview/jquery.inview.min.4edba1c65592.js"></script></head>

      <body id="homepage" class="homepage">

    <div role="banner" id="top">
      <div class="container">
        <a class="logo" href="https://www.djangoproject.com/">Django</a>
        <p class="meta">The web framework for perfectionists with deadlines.</p>
        <div class="menu-button"><i class="icon icon-reorder"></i><span>Menu</span></div><div role="navigation" class="nav-menu-on">
        <ul>
        <li>
          <a href="https://www.djangoproject.com/start/overview/">Overview</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/download/">Download</a>
        </li>
        <li>
          <a href="https://docs.djangoproject.com/">Documentation</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/weblog/">News</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/community/">Community</a>
        </li>
        <li>
          <a href="https://code.djangoproject.com/">Code</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/foundation/">About</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/fundraising/">Donate</a>
        </li>
        </ul>
        </div>
      </div>
    </div>


        <div>
            <style type="text/css">
                .listicons {width: 30px; margin: 5px }
                .whiteback {background:white}
                .rotate90 { transform: rotate(90deg); }
            </style>    
            <div class="whiteback">
            <div style="max-width:600px; margin:auto">    
            <dl class="list-features">
                <dt align="left"><i class="icon inview">&#9755;</i><a style="margin-left:0px" href="polls/">Polls App Demo on this site</a></dt>
                <dd>
                <p>The demo polls app created according the Django official tutorial, Writing you first Django app, has been lunched here.</p>
                </dd>
            </dl>
            </div>
            </div> 
        </div>


    <div class="container sidebar-right">
      <div role="main">
        
    <div class="section">
        <h1>Meet Django</h1>
        <p>
          Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
          Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus
          on writing your app without needing to reinvent the wheel. It’s free and open source.</p>
          <dl class="list-features">
          <dt><i class="icon icon-bolt inview"></i> Ridiculously fast.</dt>
          <dd>
            <p>Django was designed to help developers take applications from concept to completion as quickly as possible.</p>
          </dd>

          <dt><i class="icon icon-lock inview"></i> Reassuringly secure.</dt>
          <dd>
            <p>Django takes security seriously and helps developers avoid many common security mistakes.</p>
          </dd>

          <dt><i class="icon icon-dashboard inview"></i> Exceedingly scalable.</dt>
          <dd>
            <p>Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.</p>
          </dd>
        </dl>

        <a href="https://www.djangoproject.com/start/overview/" class="cta outline">Learn more about Django</a>
    </div>

    

    <div class="section">
    <h1>Stay in the loop</h1>
    <p>Subscribe to one of our mailing lists to stay up to date with everything in the Django community:</p>
    <div class="layout-2col">
    <div class="col form-email">
    <h3><a href="http://groups.google.com/group/django-users">Using Django</a></h3>
    <p class="meta">Get help with Django and follow announcements.</p>
    <form class="form-input" action="https://groups.google.com/group/django-users/boxsubscribe">
      <input type="email" name="email" placeholder="Enter email">
      <button type="submit">
        <i class="icon icon-envelope-o"></i>
        <span class="visuallyhidden">Subscribe</span>
      </button>
    </form>
    <p class="meta">
      You can also subscribe by sending an email to
      <a href="mailto:django-users+subscribe@googlegroups.com">
      django-users+subscribe@googlegroups.com</a> and following the
      instructions that will be sent to you.
    </p>
    </div>
    <div class="col form-email last-child">
    <h3><a href="http://groups.google.com/group/django-developers">Contributing to Django</a></h3>
    <p class="meta">Contribute to the development of Django itself.</p>
    <form class="form-input" action="https://groups.google.com/group/django-developers/boxsubscribe">
      <input type="email" name="email" placeholder="Enter email">
      <button type="submit">
        <i class="icon icon-envelope-o"></i>
        <span class="visuallyhidden">Subscribe</span>
      </button>
    </form>
    <p class="meta">
      You can also subscribe by sending an email to
      <a href="mailto:django-developers+subscribe@googlegroups.com">
      django-developers+subscribe@googlegroups.com</a> and following the
      instructions that will be sent to you.
    </p>
    </div>

    </div>
    <p>
    We have a few other specialized lists (mentorship, i18n, ...). You can
    find more information about them in our
    <a href="https://docs.djangoproject.com/en/dev/internals/mailing-lists/">
    mailing list documentation</a>.
    </p>

    </div>

    <!-- END #content-secondary -->

        <a href="#top" class="backtotop"><i class="icon icon-chevron-up"></i> Back to Top</a>
      </div>

      
    <div role="complementary">
      <a href="https://www.djangoproject.com/download/" class="cta">
          Download <em>latest release: 1.9.6</em>
      </a>
      <a href="https://docs.djangoproject.com/" class="link-readmore">Django documentation</a>

      


    <div class="fundraising-sidebar">
    <h2>Support Django!</h2>

    <div class="small-heart">
      <img src="https://www.djangoproject.com/s/img/small-fundraising-heart.png" alt="Support Django!">
    </div>

    <div class="small-cta">
      <ul class="list-links-small">
        <li><a href="https://www.djangoproject.com/fundraising/">
          Alexander Herrmann donated to the Django Software Foundation to
          support Django development. Donate today!
        </a></li>
      </ul>
    </div>
    </div>



      <h3>Latest news</h3>
      <ul class="list-news">

    <li>
    <h4>
    <a href="https://www.djangoproject.com/weblog/2016/may/02/bugfix-releases/">Django bugfix releases issued: 1.9.6 and 1.8.13</a>
    </h4>
  
    <p>Today the Django project issued bugfix releases for the 1.9 and 1.8 release series.</p>

  
      <span class="meta">
        Posted by <strong>Tim Graham</strong> on 五月 2, 2016
      </span>
  
  
    </li>


    <li>
      <h4>
        <a href="https://www.djangoproject.com/weblog/2016/apr/16/djangocon-europe-2016-thank-you/">DjangoCon Europe - a thank-you on behalf of the community</a>
      </h4>
  
    <p>DjangoCon Europe 2016 was an exemplary edition of the conference. On behalf of the community, the Django Software Foundation would like to thank the organisers for the care and thought that they invested in the event.</p>

  
      <span class="meta">
        Posted by <strong>Daniele Procida</strong> on 四月 16, 2016
      </span>
  
  
    </li>


    </ul>

      <a href="https://www.djangoproject.com/weblog/" class="link-readmore">More news</a>

      <h3>New to Django?</h3>
      <ul class="list-links-small docs-list">
          <li><a href="https://docs.djangoproject.com/en/stable/intro/install/">Installation guide</a></li>
          <li><a href="https://docs.djangoproject.com/en/stable/intro/tutorial01/">Write your first Django app</a></li>
      </ul>
      <a href="https://www.djangoproject.com/start/" class="link-readmore">Getting started with Django</a>

      <h3>The power of Django</h3>
      <ul class="list-links-small docs-list">
          <li><a href="https://docs.djangoproject.com/en/stable/topics/db/models/">Object-relational mapper</a></li>
          <li><a href="https://docs.djangoproject.com/en/stable/intro/tutorial02/">Automatic admin interface</a></li>
          <li><a href="https://docs.djangoproject.com/en/stable/topics/templates/">Robust template system</a></li>
          <li><a href="https://docs.djangoproject.com/en/stable/topics/i18n/">Quick internationalization</a></li>
      </ul>
      <a href="https://www.djangoproject.com/start/overview/" class="link-readmore">Explore more features</a>

      <h3>Get involved</h3>
      <dl class="list-links-small">
         <dt><a href="irc://irc.freenode.net/django">#django IRC channel</a></dt>
          <dd>
            Chat with other Django users
          </dd>

          <dt><a href="https://code.djangoproject.com/">Ticket system</a></dt>
          <dd>
            Report bugs and make feature requests
          </dd>
      </dl>
      <a href="https://www.djangoproject.com/community/" class="link-readmore">Inside the Django community</a>

      <h3>The Django Software Foundation</h3>
      <dl class="list-links-small">
        <dt><a href="https://www.djangoproject.com/foundation/">About the Foundation</a></dt>
        <dd>
          Our non-profit supports the project
        </dd>

        <dt><a href="https://www.djangoproject.com/foundation/donate/">Support Django</a></dt>
        <dd>
          Your contribution makes Django stronger
        </dd>

        <dt><a href="https://www.djangoproject.com/contact/foundation/">Contact the Django Software Foundation</a></dt>
        <dd></dd>
      </dl>
      <a href="https://www.djangoproject.com/foundation/" class="link-readmore">More about the DSF</a>
      
      </div>


      

    </div>

     
     

    
    
  


    
      
    <div role="contentinfo">
      <div class="subfooter">
        <div class="container">
      <h1 class="visuallyhidden">Django Links</h1>

      <div class="col learn">
        <h2>Learn More</h2>
        <ul>
          <li><a href="https://www.djangoproject.com/start/overview/">About Django</a></li>
          
          <li><a href="https://www.djangoproject.com/start/">Getting Started with Django</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/organization/">Team Organization</a></li>
          <li><a href="https://www.djangoproject.com/foundation/">Django Software Foundation</a></li>
          <li><a href="https://www.djangoproject.com/conduct/">Code of Conduct</a></li>
          <li><a href="https://www.djangoproject.com/diversity/">Diversity statement</a></li>
        </ul>
      </div>

      <div class="col involved">
        <h2>Get Involved</h2>
        <ul>
          <li><a href="https://www.djangoproject.com/community/">Join a Group</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/">Contribute to Django</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/">Submit a Bug</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues">Report a Security Issue</a></li>
        </ul>
      </div>

      <div class="col follow last-child">
        <h2>Follow Us</h2>
        <ul>
          <li><a href="https://github.com/django">GitHub</a></li>
          <li><a href="https://twitter.com/djangoproject">Twitter</a></li>
          <li><a href="https://www.djangoproject.com/rss/weblog/">News RSS</a></li>
          <li><a href="https://groups.google.com/forum/#!forum/django-users">Django Users Mailing List</a></li>
        </ul>
      </div>

    </div>
      </div>

      <div class="footer">
    <div class="container">
      <div class="footer-logo">
        <a class="logo" href="https://www.djangoproject.com/">Django</a>
      </div>
      <ul class="thanks">
        <li>
          <span>Hosting by</span> <a class="rackspace" href="http://rackspace.com">Rackspace</a>
          <span>Search by</span> <a class="elastic" href="https://www.elastic.co">Elastic Search</a>
        </li>
        <li class="design"><span>Design by</span> <a class="threespot" href="http://www.threespot.com">Threespot</a> <span class="ampersand">&amp;</span> <a class="andrevv" href="http://andrevv.com/"></a></li>
      </ul>
      <p class="copyright">© 2005-2016
        <a href="https://www.djangoproject.com/foundation/"> Django Software
        Foundation</a> and individual contributors. Django is a
        <a href="https://www.djangoproject.com/trademarks/">registered
        trademark</a> of the Django Software Foundation.
      </p>
    </div>
      </div>

    </div>

    

    
    <script>
    function extless(input) {
        return input.replace(/(.*)\.[^.]+$/, '$1');
    }
    var require = {
        shim: {
            'jquery': [],
            'jquery.inview': ["jquery"],
            'jquery.payment': ["jquery"],
            'jquery.flot': ["jquery"],
            'jquery.unveil': ["jquery"],
            'stripe': {
              exports: 'Stripe'
            }
        },
        paths: {
            "jquery": extless("https://www.djangoproject.com/s/js/lib/jquery/dist/jquery.min.87e69028f78d.js"),
            "jquery.inview": extless("https://www.djangoproject.com/s/js/lib/jquery.inview/jquery.inview.min.4edba1c65592.js"),
            "jquery.payment": extless("https://www.djangoproject.com/s/js/lib/jquery.payment/lib/jquery.payment.e99c05ca79ae.js"),
            "jquery.unveil": extless("https://www.djangoproject.com/s/js/lib/unveil/jquery.unveil.min.ac79eb277093.js"),
            "jquery.flot": extless("https://www.djangoproject.com/s/js/lib/jquery-flot/jquery.flot.min.9964206e9d7f.js"),
            "mod/floating-warning": extless("https://www.djangoproject.com/s/js/mod/floating-warning.a21b2abd2884.js"),
            "mod/list-collapsing": extless("https://www.djangoproject.com/s/js/mod/list-collapsing.c1a08d3ef9e9.js"),
            "mod/list-feature": extless("https://www.djangoproject.com/s/js/mod/list-feature.73529480f25b.js"),
            "mod/mobile-menu": extless("https://www.djangoproject.com/s/js/mod/mobile-menu.841726ee903a.js"),
            "mod/version-switcher": extless("https://www.djangoproject.com/s/js/mod/version-switcher.c28bb83972bb.js"),
            "mod/search-key": extless("https://www.djangoproject.com/s/js/mod/search-key.f3c0a6fcfedd.js"),
            "mod/stripe-custom-checkout": extless("https://www.djangoproject.com/s/js/mod/stripe-custom-checkout.e299868f75aa.js"),
            "mod/stripe-change-card": extless("https://www.djangoproject.com/s/js/mod/stripe-change-card.c9e3d05f7a91.js"),
            "stripe-checkout": "https://checkout.stripe.com/checkout",
            "stripe": "https://js.stripe.com/v2/?"  // ? needed due to require.js
        }
    };
    </script>
    <script data-main="https://www.djangoproject.com/s/js/main.e3fa98aeaa99.js" src="https://www.djangoproject.com/s/js/lib/require.177879fbe7dd.js"></script>
    </body></html>"""
    
    return HttpResponse( htmlstring )