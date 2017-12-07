checksum =. [: +/ @: ; (>./ - <./)&.> 
sanitize =. [: ([: ; [: ".&.> TAB cut ])&.> LF cut ]
answer =. checksum @: sanitize

NB. Something went wrong here -- see python answer
checksum_2 =. [: +/ ([: <./ [: (>./%<./)"1 (#~ 0 = |/~))"1
answer =. [: checksum_1 8 16 $ ; @: sanitize
