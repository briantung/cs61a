
(define (deep-map fn s)
	(if (null? s) '() 
		(if (list? s) ( cons (deep-map fn (car s)) (deep-map fn (cdr s))) (fn  s)) 
))

(define (substitute s old new)
 	(if (null? s) '() 
		(if (list? s) (cons (substitute (car s) old new) (substitute (cdr s) old new)) (if (equal? s old) new s)) 
	)
)

(define (sub-all s olds news)
 	
	(define (inlist? word news olds) 
		(if (null? news) word (if (equal? word (car news)) (car olds) (inlist? word (cdr news) (cdr olds))))	
	)

	(if (null? s) '() 
		(if (list? s) 
			(cons (sub-all (car s) olds news) (sub-all (cdr s) olds news)) 
			(inlist? s olds news)) 
	)
)


