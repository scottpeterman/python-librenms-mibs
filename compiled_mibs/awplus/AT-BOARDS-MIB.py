# SNMP MIB module (AT-BOARDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-BOARDS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:22 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(objects,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "objects")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

boards = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    boards.setRevisions(
        ("2021-04-22 00:00",
         "2021-03-25 00:00",
         "2021-02-25 00:00",
         "2021-02-11 00:00",
         "2021-01-18 00:00",
         "2020-10-14 00:00",
         "2020-06-24 00:00",
         "2020-06-22 00:00",
         "2020-06-18 00:00",
         "2020-06-02 00:00",
         "2019-12-04 00:00",
         "2019-07-30 00:00",
         "2019-06-05 00:00",
         "2019-05-29 00:00",
         "2019-05-28 00:00",
         "2019-05-22 00:00",
         "2019-03-11 00:00",
         "2019-03-08 00:00",
         "2018-10-03 00:00",
         "2018-09-04 00:00",
         "2018-08-30 00:00",
         "2018-08-22 00:00",
         "2018-08-17 00:00",
         "2018-07-19 00:00",
         "2018-05-29 00:00",
         "2018-04-06 00:00",
         "2018-03-20 00:00",
         "2018-01-18 00:00",
         "2017-12-08 00:00",
         "2017-11-14 00:00",
         "2017-10-19 00:00",
         "2017-05-11 00:00",
         "2017-04-26 00:00",
         "2017-03-31 00:00",
         "2017-02-01 00:00",
         "2017-01-18 00:00",
         "2016-10-03 00:00",
         "2016-05-06 00:00",
         "2016-01-08 00:00",
         "2016-01-06 00:00",
         "2015-12-17 00:00",
         "2015-11-10 00:00",
         "2015-08-09 00:00",
         "2015-08-05 00:00",
         "2015-07-27 00:00",
         "2015-07-22 00:00",
         "2015-06-30 00:00",
         "2015-06-19 00:00",
         "2015-05-06 00:00",
         "2015-04-03 00:00",
         "2015-03-16 00:00",
         "2015-03-12 00:00",
         "2015-02-19 00:00",
         "2015-01-14 00:00",
         "2014-11-19 00:00",
         "2014-11-18 00:00",
         "2014-10-22 00:00",
         "2014-09-23 00:00",
         "2014-08-28 00:00",
         "2014-08-20 00:00",
         "2014-07-30 00:00",
         "2014-06-09 00:00",
         "2014-06-03 00:00",
         "2014-05-16 00:00",
         "2014-03-25 00:00",
         "2013-08-01 00:00",
         "2013-07-09 00:00",
         "2012-06-07 00:00",
         "2012-05-21 00:00",
         "2012-05-15 00:00",
         "2012-03-16 00:00",
         "2011-12-18 05:00",
         "2011-10-25 00:00",
         "2011-09-20 00:00",
         "2011-09-15 00:00",
         "2011-09-14 00:00",
         "2011-09-05 00:00",
         "2011-05-10 00:00",
         "2011-04-28 00:00",
         "2011-04-04 00:00",
         "2011-03-08 00:00",
         "2010-12-01 00:00",
         "2010-10-12 00:00",
         "2010-09-07 00:00",
         "2010-08-19 00:00",
         "2010-07-22 00:00",
         "2010-06-14 04:45",
         "2010-05-19 00:00",
         "2009-05-15 00:00",
         "2008-12-11 00:00",
         "2008-11-24 00:00",
         "2008-03-03 15:00",
         "2007-03-21 00:00",
         "2007-02-07 00:00",
         "2006-06-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PprIcmAr023_ObjectIdentity = ObjectIdentity
pprIcmAr023 = _PprIcmAr023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 39)
)
_PprIcmAr021s_ObjectIdentity = ObjectIdentity
pprIcmAr021s = _PprIcmAr021s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 40)
)
_PprIcmAr022_ObjectIdentity = ObjectIdentity
pprIcmAr022 = _PprIcmAr022_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 41)
)
_PprIcmAr025_ObjectIdentity = ObjectIdentity
pprIcmAr025 = _PprIcmAr025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 45)
)
_PprIcmAr024_ObjectIdentity = ObjectIdentity
pprIcmAr024 = _PprIcmAr024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 46)
)
_PprAr300_ObjectIdentity = ObjectIdentity
pprAr300 = _PprAr300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 49)
)
_PprAr300L_ObjectIdentity = ObjectIdentity
pprAr300L = _PprAr300L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 52)
)
_PprAr310_ObjectIdentity = ObjectIdentity
pprAr310 = _PprAr310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 53)
)
_PprAr120_ObjectIdentity = ObjectIdentity
pprAr120 = _PprAr120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 54)
)
_PprAr300Lu_ObjectIdentity = ObjectIdentity
pprAr300Lu = _PprAr300Lu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 55)
)
_PprAr300u_ObjectIdentity = ObjectIdentity
pprAr300u = _PprAr300u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 56)
)
_PprAr310u_ObjectIdentity = ObjectIdentity
pprAr310u = _PprAr310u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 57)
)
_PprAr350_ObjectIdentity = ObjectIdentity
pprAr350 = _PprAr350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 58)
)
_PprIcmAr021u_ObjectIdentity = ObjectIdentity
pprIcmAr021u = _PprIcmAr021u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 59)
)
_PprAr720_ObjectIdentity = ObjectIdentity
pprAr720 = _PprAr720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 63)
)
_PprAr010_ObjectIdentity = ObjectIdentity
pprAr010 = _PprAr010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 67)
)
_PprAr012_ObjectIdentity = ObjectIdentity
pprAr012 = _PprAr012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 68)
)
_PprAr011_ObjectIdentity = ObjectIdentity
pprAr011 = _PprAr011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 69)
)
_PprAr370_ObjectIdentity = ObjectIdentity
pprAr370 = _PprAr370_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 70)
)
_PprAr330_ObjectIdentity = ObjectIdentity
pprAr330 = _PprAr330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 71)
)
_PprAr395_ObjectIdentity = ObjectIdentity
pprAr395 = _PprAr395_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 72)
)
_PprAr390_ObjectIdentity = ObjectIdentity
pprAr390 = _PprAr390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 73)
)
_PprAr370u_ObjectIdentity = ObjectIdentity
pprAr370u = _PprAr370u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 75)
)
_PprIcmAr020_ObjectIdentity = ObjectIdentity
pprIcmAr020 = _PprIcmAr020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 76)
)
_PprAr740_ObjectIdentity = ObjectIdentity
pprAr740 = _PprAr740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 79)
)
_PprAr140s_ObjectIdentity = ObjectIdentity
pprAr140s = _PprAr140s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 80)
)
_PprAr140u_ObjectIdentity = ObjectIdentity
pprAr140u = _PprAr140u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 81)
)
_PprAr160su_ObjectIdentity = ObjectIdentity
pprAr160su = _PprAr160su_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 82)
)
_PprAr320_ObjectIdentity = ObjectIdentity
pprAr320 = _PprAr320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 83)
)
_PprAr130s_ObjectIdentity = ObjectIdentity
pprAr130s = _PprAr130s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 85)
)
_PprAr130u_ObjectIdentity = ObjectIdentity
pprAr130u = _PprAr130u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 86)
)
_PprRapier24_ObjectIdentity = ObjectIdentity
pprRapier24 = _PprRapier24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 87)
)
_PprNsm0404Pic_ObjectIdentity = ObjectIdentity
pprNsm0404Pic = _PprNsm0404Pic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 88)
)
_PprA35SXSC_ObjectIdentity = ObjectIdentity
pprA35SXSC = _PprA35SXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 89)
)
_PprA35LXSC_ObjectIdentity = ObjectIdentity
pprA35LXSC = _PprA35LXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 90)
)
_PprA36MTRJ_ObjectIdentity = ObjectIdentity
pprA36MTRJ = _PprA36MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 91)
)
_PprA37VF45_ObjectIdentity = ObjectIdentity
pprA37VF45 = _PprA37VF45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 92)
)
_PprA38LC_ObjectIdentity = ObjectIdentity
pprA38LC = _PprA38LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 93)
)
_PprA39Tx_ObjectIdentity = ObjectIdentity
pprA39Tx = _PprA39Tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 94)
)
_PprAr740DC_ObjectIdentity = ObjectIdentity
pprAr740DC = _PprAr740DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 95)
)
_PprNsm0418BRI_ObjectIdentity = ObjectIdentity
pprNsm0418BRI = _PprNsm0418BRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 96)
)
_PprRapier16fSC_ObjectIdentity = ObjectIdentity
pprRapier16fSC = _PprRapier16fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 97)
)
_Ppr8624xl80_ObjectIdentity = ObjectIdentity
ppr8624xl80 = _Ppr8624xl80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 98)
)
_PprRapier16fMT_ObjectIdentity = ObjectIdentity
pprRapier16fMT = _PprRapier16fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 99)
)
_PprRapier16fMTi_ObjectIdentity = ObjectIdentity
pprRapier16fMTi = _PprRapier16fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 100)
)
_PprRapier8t8fSC_ObjectIdentity = ObjectIdentity
pprRapier8t8fSC = _PprRapier8t8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 101)
)
_PprRapier8t8fSCi_ObjectIdentity = ObjectIdentity
pprRapier8t8fSCi = _PprRapier8t8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 102)
)
_PprRapier8t8fMT_ObjectIdentity = ObjectIdentity
pprRapier8t8fMT = _PprRapier8t8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 103)
)
_PprRapier8t8fMTi_ObjectIdentity = ObjectIdentity
pprRapier8t8fMTi = _PprRapier8t8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 104)
)
_PprRapier8fSC_ObjectIdentity = ObjectIdentity
pprRapier8fSC = _PprRapier8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 105)
)
_PprRapier8fSCi_ObjectIdentity = ObjectIdentity
pprRapier8fSCi = _PprRapier8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 106)
)
_PprRapier8fMT_ObjectIdentity = ObjectIdentity
pprRapier8fMT = _PprRapier8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 107)
)
_PprRapier8fMTi_ObjectIdentity = ObjectIdentity
pprRapier8fMTi = _PprRapier8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 108)
)
_PprRapierG6_ObjectIdentity = ObjectIdentity
pprRapierG6 = _PprRapierG6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 110)
)
_PprRapierG6SX_ObjectIdentity = ObjectIdentity
pprRapierG6SX = _PprRapierG6SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 111)
)
_PprRapierG6LX_ObjectIdentity = ObjectIdentity
pprRapierG6LX = _PprRapierG6LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 112)
)
_PprRapierG6MT_ObjectIdentity = ObjectIdentity
pprRapierG6MT = _PprRapierG6MT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 113)
)
_PprRapier16fSCi_ObjectIdentity = ObjectIdentity
pprRapier16fSCi = _PprRapier16fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 114)
)
_PprRapier24i_ObjectIdentity = ObjectIdentity
pprRapier24i = _PprRapier24i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 115)
)
_PprAr824_ObjectIdentity = ObjectIdentity
pprAr824 = _PprAr824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 116)
)
_PprAr816fSC_ObjectIdentity = ObjectIdentity
pprAr816fSC = _PprAr816fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 117)
)
_PprAr816fSCi_ObjectIdentity = ObjectIdentity
pprAr816fSCi = _PprAr816fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 118)
)
_PprAr816fMT_ObjectIdentity = ObjectIdentity
pprAr816fMT = _PprAr816fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 119)
)
_PprAr816fMTi_ObjectIdentity = ObjectIdentity
pprAr816fMTi = _PprAr816fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 120)
)
_PprAr88t8fSC_ObjectIdentity = ObjectIdentity
pprAr88t8fSC = _PprAr88t8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 121)
)
_PprAr88t8fSCi_ObjectIdentity = ObjectIdentity
pprAr88t8fSCi = _PprAr88t8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 122)
)
_PprAr88t8fMT_ObjectIdentity = ObjectIdentity
pprAr88t8fMT = _PprAr88t8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 123)
)
_PprAr88t8fMTi_ObjectIdentity = ObjectIdentity
pprAr88t8fMTi = _PprAr88t8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 124)
)
_PprAr88fSC_ObjectIdentity = ObjectIdentity
pprAr88fSC = _PprAr88fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 125)
)
_PprAr88fSCi_ObjectIdentity = ObjectIdentity
pprAr88fSCi = _PprAr88fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 126)
)
_PprAr88fMT_ObjectIdentity = ObjectIdentity
pprAr88fMT = _PprAr88fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 127)
)
_PprAr88fMTi_ObjectIdentity = ObjectIdentity
pprAr88fMTi = _PprAr88fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 128)
)
_PprAr824i_ObjectIdentity = ObjectIdentity
pprAr824i = _PprAr824i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 129)
)
_PprAt8724XL_ObjectIdentity = ObjectIdentity
pprAt8724XL = _PprAt8724XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 130)
)
_PprAt8748XL_ObjectIdentity = ObjectIdentity
pprAt8748XL = _PprAt8748XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 131)
)
_PprAt8724XLDC_ObjectIdentity = ObjectIdentity
pprAt8724XLDC = _PprAt8724XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 132)
)
_PprAt8748XLDC_ObjectIdentity = ObjectIdentity
pprAt8748XLDC = _PprAt8748XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 133)
)
_PprAt8824_ObjectIdentity = ObjectIdentity
pprAt8824 = _PprAt8824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 134)
)
_PprAt8824DC_ObjectIdentity = ObjectIdentity
pprAt8824DC = _PprAt8824DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 135)
)
_Ppr8724XLDC_ObjectIdentity = ObjectIdentity
ppr8724XLDC = _Ppr8724XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 141)
)
_Ppr8748XLDC_ObjectIdentity = ObjectIdentity
ppr8748XLDC = _Ppr8748XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 142)
)
_PprRapier24iDcNEBS_ObjectIdentity = ObjectIdentity
pprRapier24iDcNEBS = _PprRapier24iDcNEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 144)
)
_PprAt8724XLDcNEBS_ObjectIdentity = ObjectIdentity
pprAt8724XLDcNEBS = _PprAt8724XLDcNEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 146)
)
_PprAt8848DC_ObjectIdentity = ObjectIdentity
pprAt8848DC = _PprAt8848DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 147)
)
_PprRapier48_ObjectIdentity = ObjectIdentity
pprRapier48 = _PprRapier48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 148)
)
_PprAt8848_ObjectIdentity = ObjectIdentity
pprAt8848 = _PprAt8848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 149)
)
_PprRapier48i_ObjectIdentity = ObjectIdentity
pprRapier48i = _PprRapier48i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 150)
)
_PprNsm0424BRI_ObjectIdentity = ObjectIdentity
pprNsm0424BRI = _PprNsm0424BRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 151)
)
_PprIcmAR026_ObjectIdentity = ObjectIdentity
pprIcmAR026 = _PprIcmAR026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 153)
)
_Ppr9816GF_ObjectIdentity = ObjectIdentity
ppr9816GF = _Ppr9816GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 157)
)
_Ppr9812TF_ObjectIdentity = ObjectIdentity
ppr9812TF = _Ppr9812TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 158)
)
_PprSbChassis4AC_ObjectIdentity = ObjectIdentity
pprSbChassis4AC = _PprSbChassis4AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 159)
)
_PprSbChassis4DC_ObjectIdentity = ObjectIdentity
pprSbChassis4DC = _PprSbChassis4DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 160)
)
_PprSbChassis8AC_ObjectIdentity = ObjectIdentity
pprSbChassis8AC = _PprSbChassis8AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 161)
)
_PprSbChassis8DC_ObjectIdentity = ObjectIdentity
pprSbChassis8DC = _PprSbChassis8DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 162)
)
_PprSbChassis16AC_ObjectIdentity = ObjectIdentity
pprSbChassis16AC = _PprSbChassis16AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 163)
)
_PprSbChassis16DC_ObjectIdentity = ObjectIdentity
pprSbChassis16DC = _PprSbChassis16DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 164)
)
_PprSbControl_ObjectIdentity = ObjectIdentity
pprSbControl = _PprSbControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 165)
)
_PprSbControlDTM_ObjectIdentity = ObjectIdentity
pprSbControlDTM = _PprSbControlDTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 166)
)
_PprSb48t_ObjectIdentity = ObjectIdentity
pprSb48t = _PprSb48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 167)
)
_PprSb96t_ObjectIdentity = ObjectIdentity
pprSb96t = _PprSb96t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 168)
)
_PprSb32fSC_ObjectIdentity = ObjectIdentity
pprSb32fSC = _PprSb32fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 169)
)
_PprSb32fMT_ObjectIdentity = ObjectIdentity
pprSb32fMT = _PprSb32fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 170)
)
_PprSb8fRJ_ObjectIdentity = ObjectIdentity
pprSb8fRJ = _PprSb8fRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 172)
)
_PprSb8fSXSC_ObjectIdentity = ObjectIdentity
pprSb8fSXSC = _PprSb8fSXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 173)
)
_PprSb8fSXMT_ObjectIdentity = ObjectIdentity
pprSb8fSXMT = _PprSb8fSXMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 174)
)
_PprSb8fLXSC_ObjectIdentity = ObjectIdentity
pprSb8fLXSC = _PprSb8fLXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 175)
)
_PprSb8fLXMT_ObjectIdentity = ObjectIdentity
pprSb8fLXMT = _PprSb8fLXMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 176)
)
_PprAr410_ObjectIdentity = ObjectIdentity
pprAr410 = _PprAr410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 177)
)
_PprA40SC_ObjectIdentity = ObjectIdentity
pprA40SC = _PprA40SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 178)
)
_PprA40MTRJ_ObjectIdentity = ObjectIdentity
pprA40MTRJ = _PprA40MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 179)
)
_PprA41SC_ObjectIdentity = ObjectIdentity
pprA41SC = _PprA41SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 180)
)
_PprA41MTRJ_ObjectIdentity = ObjectIdentity
pprA41MTRJ = _PprA41MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 181)
)
_PprAr725_ObjectIdentity = ObjectIdentity
pprAr725 = _PprAr725_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 182)
)
_PprAr745_ObjectIdentity = ObjectIdentity
pprAr745 = _PprAr745_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 183)
)
_PprSb8GBIC_ObjectIdentity = ObjectIdentity
pprSb8GBIC = _PprSb8GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 184)
)
_PprA42GBIC_ObjectIdentity = ObjectIdentity
pprA42GBIC = _PprA42GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 185)
)
_Ppr9816GB_ObjectIdentity = ObjectIdentity
ppr9816GB = _Ppr9816GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 186)
)
_Ppr9812T_ObjectIdentity = ObjectIdentity
ppr9812T = _Ppr9812T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 187)
)
_PprNsm048DS3_ObjectIdentity = ObjectIdentity
pprNsm048DS3 = _PprNsm048DS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 188)
)
_PprAr450_ObjectIdentity = ObjectIdentity
pprAr450 = _PprAr450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 191)
)
_PprAr450Dual_ObjectIdentity = ObjectIdentity
pprAr450Dual = _PprAr450Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 192)
)
_PprSbExpander_ObjectIdentity = ObjectIdentity
pprSbExpander = _PprSbExpander_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 193)
)
_PprAr725DC_ObjectIdentity = ObjectIdentity
pprAr725DC = _PprAr725DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 194)
)
_PprAr745DC_ObjectIdentity = ObjectIdentity
pprAr745DC = _PprAr745DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 195)
)
_PprAr410v2_ObjectIdentity = ObjectIdentity
pprAr410v2 = _PprAr410v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 196)
)
_PprAr410v3_ObjectIdentity = ObjectIdentity
pprAr410v3 = _PprAr410v3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 197)
)
_PprIcmAr027_ObjectIdentity = ObjectIdentity
pprIcmAr027 = _PprIcmAr027_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 198)
)
_Ppr8948EX_ObjectIdentity = ObjectIdentity
ppr8948EX = _Ppr8948EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 202)
)
_Ppr8948i_ObjectIdentity = ObjectIdentity
ppr8948i = _Ppr8948i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 203)
)
_Ppr9816GBDC_ObjectIdentity = ObjectIdentity
ppr9816GBDC = _Ppr9816GBDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 204)
)
_Ppr9812TDC_ObjectIdentity = ObjectIdentity
ppr9812TDC = _Ppr9812TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 205)
)
_PprIcmAr021v2s_ObjectIdentity = ObjectIdentity
pprIcmAr021v2s = _PprIcmAr021v2s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 206)
)
_PprA50_ObjectIdentity = ObjectIdentity
pprA50 = _PprA50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 207)
)
_PprA51_ObjectIdentity = ObjectIdentity
pprA51 = _PprA51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 208)
)
_PprA52_ObjectIdentity = ObjectIdentity
pprA52 = _PprA52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 209)
)
_PprA53_ObjectIdentity = ObjectIdentity
pprA53 = _PprA53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 210)
)
_PprFanA01_ObjectIdentity = ObjectIdentity
pprFanA01 = _PprFanA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 212)
)
_PprAtPwr01AC_ObjectIdentity = ObjectIdentity
pprAtPwr01AC = _PprAtPwr01AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 213)
)
_PprAtPwr01DC_ObjectIdentity = ObjectIdentity
pprAtPwr01DC = _PprAtPwr01DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 214)
)
_PprAtFan01_ObjectIdentity = ObjectIdentity
pprAtFan01 = _PprAtFan01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 215)
)
_PprSb24RJ_ObjectIdentity = ObjectIdentity
pprSb24RJ = _PprSb24RJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 216)
)
_PprSb1XFP_ObjectIdentity = ObjectIdentity
pprSb1XFP = _PprSb1XFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 217)
)
_Ppr9924T_ObjectIdentity = ObjectIdentity
ppr9924T = _Ppr9924T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 218)
)
_Ppr9924SP_ObjectIdentity = ObjectIdentity
ppr9924SP = _Ppr9924SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 219)
)
_Ppr9924TEMC_ObjectIdentity = ObjectIdentity
ppr9924TEMC = _Ppr9924TEMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 220)
)
_Ppr9924T4SP_ObjectIdentity = ObjectIdentity
ppr9924T4SP = _Ppr9924T4SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 221)
)
_PprAR440_ObjectIdentity = ObjectIdentity
pprAR440 = _PprAR440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 227)
)
_PprAR441_ObjectIdentity = ObjectIdentity
pprAR441 = _PprAR441_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 228)
)
_PprAR442_ObjectIdentity = ObjectIdentity
pprAR442 = _PprAR442_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 229)
)
_PprAR443_ObjectIdentity = ObjectIdentity
pprAR443 = _PprAR443_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 230)
)
_PprAR444_ObjectIdentity = ObjectIdentity
pprAR444 = _PprAR444_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 231)
)
_PprAR420_ObjectIdentity = ObjectIdentity
pprAR420 = _PprAR420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 232)
)
_PprAt8624T2M_ObjectIdentity = ObjectIdentity
pprAt8624T2M = _PprAt8624T2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 239)
)
_PprA46Tx_ObjectIdentity = ObjectIdentity
pprA46Tx = _PprA46Tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 240)
)
_PprAR550_ObjectIdentity = ObjectIdentity
pprAR550 = _PprAR550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 241)
)
_PprAR551_ObjectIdentity = ObjectIdentity
pprAR551 = _PprAR551_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 242)
)
_PprAR552_ObjectIdentity = ObjectIdentity
pprAR552 = _PprAR552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 243)
)
_PprC8724MLB_ObjectIdentity = ObjectIdentity
pprC8724MLB = _PprC8724MLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 248)
)
_PprAt86482SP_ObjectIdentity = ObjectIdentity
pprAt86482SP = _PprAt86482SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 252)
)
_PprAt8624POE_ObjectIdentity = ObjectIdentity
pprAt8624POE = _PprAt8624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 253)
)
_PprAtPwr01RAC_ObjectIdentity = ObjectIdentity
pprAtPwr01RAC = _PprAtPwr01RAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 254)
)
_PprAtFan01R_ObjectIdentity = ObjectIdentity
pprAtFan01R = _PprAtFan01R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 255)
)
_Ppr9924Ts_ObjectIdentity = ObjectIdentity
ppr9924Ts = _Ppr9924Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 256)
)
_PprAR570_ObjectIdentity = ObjectIdentity
pprAR570 = _PprAR570_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 258)
)
_PprAtPwr02AC_ObjectIdentity = ObjectIdentity
pprAtPwr02AC = _PprAtPwr02AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 264)
)
_PprAtPwr02RAC_ObjectIdentity = ObjectIdentity
pprAtPwr02RAC = _PprAtPwr02RAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 265)
)
_PprAtXum10G_ObjectIdentity = ObjectIdentity
pprAtXum10G = _PprAtXum10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 266)
)
_PprAtXum12T_ObjectIdentity = ObjectIdentity
pprAtXum12T = _PprAtXum12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 267)
)
_PprAtXum12SFP_ObjectIdentity = ObjectIdentity
pprAtXum12SFP = _PprAtXum12SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 268)
)
_PprSb24SFP_ObjectIdentity = ObjectIdentity
pprSb24SFP = _PprSb24SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 269)
)
_PprAR770_ObjectIdentity = ObjectIdentity
pprAR770 = _PprAR770_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 270)
)
_Pprx90024XT_ObjectIdentity = ObjectIdentity
pprx90024XT = _Pprx90024XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 271)
)
_Pprx90024XS_ObjectIdentity = ObjectIdentity
pprx90024XS = _Pprx90024XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 272)
)
_PprAtXum10Gi_ObjectIdentity = ObjectIdentity
pprAtXum10Gi = _PprAtXum10Gi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 273)
)
_PprAtXum12SFPi_ObjectIdentity = ObjectIdentity
pprAtXum12SFPi = _PprAtXum12SFPi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 274)
)
_PprAtXum12Ti_ObjectIdentity = ObjectIdentity
pprAtXum12Ti = _PprAtXum12Ti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 275)
)
_PprAR415S_ObjectIdentity = ObjectIdentity
pprAR415S = _PprAR415S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 276)
)
_PprAR415SDC_ObjectIdentity = ObjectIdentity
pprAR415SDC = _PprAR415SDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 277)
)
_PprAR550SDP_ObjectIdentity = ObjectIdentity
pprAR550SDP = _PprAR550SDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 278)
)
_Ppr8948iN_ObjectIdentity = ObjectIdentity
ppr8948iN = _Ppr8948iN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 279)
)
_PprAtXum12TiN_ObjectIdentity = ObjectIdentity
pprAtXum12TiN = _PprAtXum12TiN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 280)
)
_Pprx90024XTN_ObjectIdentity = ObjectIdentity
pprx90024XTN = _Pprx90024XTN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 281)
)
_PprSwitchBladex908_ObjectIdentity = ObjectIdentity
pprSwitchBladex908 = _PprSwitchBladex908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 282)
)
_PprRapier48w_ObjectIdentity = ObjectIdentity
pprRapier48w = _PprRapier48w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 283)
)
_PprAt8316XLCR_ObjectIdentity = ObjectIdentity
pprAt8316XLCR = _PprAt8316XLCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 284)
)
_PprAt8324XLCR_ObjectIdentity = ObjectIdentity
pprAt8324XLCR = _PprAt8324XLCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 285)
)
_PprXemStk_ObjectIdentity = ObjectIdentity
pprXemStk = _PprXemStk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 286)
)
_PprAt8824R_ObjectIdentity = ObjectIdentity
pprAt8824R = _PprAt8824R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 287)
)
_Pprx90012XTS_ObjectIdentity = ObjectIdentity
pprx90012XTS = _Pprx90012XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 288)
)
_PprX90048FS_ObjectIdentity = ObjectIdentity
pprX90048FS = _PprX90048FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 289)
)
_Pprx60024TS_ObjectIdentity = ObjectIdentity
pprx60024TS = _Pprx60024TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 290)
)
_Pprx60024TSXP_ObjectIdentity = ObjectIdentity
pprx60024TSXP = _Pprx60024TSXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 291)
)
_PprAt9724TS_ObjectIdentity = ObjectIdentity
pprAt9724TS = _PprAt9724TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 292)
)
_PprAt9724TSXP_ObjectIdentity = ObjectIdentity
pprAt9724TSXP = _PprAt9724TSXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 293)
)
_Pprx60048TS_ObjectIdentity = ObjectIdentity
pprx60048TS = _Pprx60048TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 294)
)
_Pprx60048TSXP_ObjectIdentity = ObjectIdentity
pprx60048TSXP = _Pprx60048TSXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 295)
)
_PprAt9748TS_ObjectIdentity = ObjectIdentity
pprAt9748TS = _PprAt9748TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 296)
)
_PprAt9748TSXP_ObjectIdentity = ObjectIdentity
pprAt9748TSXP = _PprAt9748TSXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 297)
)
_PprXum100M_ObjectIdentity = ObjectIdentity
pprXum100M = _PprXum100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 298)
)
_PprAtPWR05AC_ObjectIdentity = ObjectIdentity
pprAtPWR05AC = _PprAtPWR05AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 299)
)
_PprIcmAr021v3s_ObjectIdentity = ObjectIdentity
pprIcmAr021v3s = _PprIcmAr021v3s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 300)
)
_PprRapier48wb_ObjectIdentity = ObjectIdentity
pprRapier48wb = _PprRapier48wb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 301)
)
_PprRapier48wAC_ObjectIdentity = ObjectIdentity
pprRapier48wAC = _PprRapier48wAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 302)
)
_PprRapier48wbAC_ObjectIdentity = ObjectIdentity
pprRapier48wbAC = _PprRapier48wbAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 303)
)
_PprX30024TS_ObjectIdentity = ObjectIdentity
pprX30024TS = _PprX30024TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 304)
)
_PprXemPOE_ObjectIdentity = ObjectIdentity
pprXemPOE = _PprXemPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 305)
)
_PprXem2XP_ObjectIdentity = ObjectIdentity
pprXem2XP = _PprXem2XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 306)
)
_PprATStackXG_ObjectIdentity = ObjectIdentity
pprATStackXG = _PprATStackXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 307)
)
_PprATEMXP_ObjectIdentity = ObjectIdentity
pprATEMXP = _PprATEMXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 308)
)
_PprATLBM_ObjectIdentity = ObjectIdentity
pprATLBM = _PprATLBM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 309)
)
_PprAt8624TCR_ObjectIdentity = ObjectIdentity
pprAt8624TCR = _PprAt8624TCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 310)
)
_PprAt8624POECR_ObjectIdentity = ObjectIdentity
pprAt8624POECR = _PprAt8624POECR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 311)
)
_PprAtSBx8112_ObjectIdentity = ObjectIdentity
pprAtSBx8112 = _PprAtSBx8112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 316)
)
_PprAtSBx81CFC400_ObjectIdentity = ObjectIdentity
pprAtSBx81CFC400 = _PprAtSBx81CFC400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 317)
)
_PprAtSBx81GP24_ObjectIdentity = ObjectIdentity
pprAtSBx81GP24 = _PprAtSBx81GP24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 318)
)
_PprAtSBx81XZ4_ObjectIdentity = ObjectIdentity
pprAtSBx81XZ4 = _PprAtSBx81XZ4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 319)
)
_PprAtSBx8161SYSAC_ObjectIdentity = ObjectIdentity
pprAtSBx8161SYSAC = _PprAtSBx8161SYSAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 320)
)
_PprAtSBx8165POEAC_ObjectIdentity = ObjectIdentity
pprAtSBx8165POEAC = _PprAtSBx8165POEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 321)
)
_PprAtSBx81FAN_ObjectIdentity = ObjectIdentity
pprAtSBx81FAN = _PprAtSBx81FAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 322)
)
_PprAtPWR05DC_ObjectIdentity = ObjectIdentity
pprAtPWR05DC = _PprAtPWR05DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 323)
)
_PprXem2XT_ObjectIdentity = ObjectIdentity
pprXem2XT = _PprXem2XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 325)
)
_Pprx60024TSPOE_ObjectIdentity = ObjectIdentity
pprx60024TSPOE = _Pprx60024TSPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 326)
)
_Pprx60024TSPOEPLUS_ObjectIdentity = ObjectIdentity
pprx60024TSPOEPLUS = _Pprx60024TSPOEPLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 327)
)
_PprAR560_ObjectIdentity = ObjectIdentity
pprAR560 = _PprAR560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 330)
)
_Pprx61048TsXPOEPlus_ObjectIdentity = ObjectIdentity
pprx61048TsXPOEPlus = _Pprx61048TsXPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 331)
)
_Pprx61048TsPOEPlus_ObjectIdentity = ObjectIdentity
pprx61048TsPOEPlus = _Pprx61048TsPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 332)
)
_Pprx61024TsXPOEPlus_ObjectIdentity = ObjectIdentity
pprx61024TsXPOEPlus = _Pprx61024TsXPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 333)
)
_Pprx61024TsPOEPlus_ObjectIdentity = ObjectIdentity
pprx61024TsPOEPlus = _Pprx61024TsPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 334)
)
_PprPWR800_ObjectIdentity = ObjectIdentity
pprPWR800 = _PprPWR800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 336)
)
_PprPWR1200_ObjectIdentity = ObjectIdentity
pprPWR1200 = _PprPWR1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 337)
)
_PprPWR250_ObjectIdentity = ObjectIdentity
pprPWR250 = _PprPWR250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 338)
)
_Pprx61048TsX_ObjectIdentity = ObjectIdentity
pprx61048TsX = _Pprx61048TsX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 339)
)
_Pprx61048Ts_ObjectIdentity = ObjectIdentity
pprx61048Ts = _Pprx61048Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 340)
)
_Pprx61024TsX_ObjectIdentity = ObjectIdentity
pprx61024TsX = _Pprx61024TsX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 341)
)
_Pprx61024Ts_ObjectIdentity = ObjectIdentity
pprx61024Ts = _Pprx61024Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 342)
)
_Pprx61024SPX_ObjectIdentity = ObjectIdentity
pprx61024SPX = _Pprx61024SPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 343)
)
_PprRapier48xDC_ObjectIdentity = ObjectIdentity
pprRapier48xDC = _PprRapier48xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 345)
)
_PprAR030_ObjectIdentity = ObjectIdentity
pprAR030 = _PprAR030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 347)
)
_Pprx200GE52T_ObjectIdentity = ObjectIdentity
pprx200GE52T = _Pprx200GE52T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 348)
)
_Pprx200GE28T_ObjectIdentity = ObjectIdentity
pprx200GE28T = _Pprx200GE28T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 349)
)
_PprXem2XS_ObjectIdentity = ObjectIdentity
pprXem2XS = _PprXem2XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 350)
)
_PprPWR250DC_ObjectIdentity = ObjectIdentity
pprPWR250DC = _PprPWR250DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 351)
)
_PprAtSBx81GT24_ObjectIdentity = ObjectIdentity
pprAtSBx81GT24 = _PprAtSBx81GT24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 352)
)
_PprAtSBx81GS24a_ObjectIdentity = ObjectIdentity
pprAtSBx81GS24a = _PprAtSBx81GS24a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 353)
)
_PprAtSBx81XS6_ObjectIdentity = ObjectIdentity
pprAtSBx81XS6 = _PprAtSBx81XS6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 354)
)
_PprXem24T_ObjectIdentity = ObjectIdentity
pprXem24T = _PprXem24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 356)
)
_PprAR031_ObjectIdentity = ObjectIdentity
pprAR031 = _PprAR031_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 357)
)
_PprXem12Tv2_ObjectIdentity = ObjectIdentity
pprXem12Tv2 = _PprXem12Tv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 358)
)
_PprXem12Sv2_ObjectIdentity = ObjectIdentity
pprXem12Sv2 = _PprXem12Sv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 359)
)
_Pprx2109GT_ObjectIdentity = ObjectIdentity
pprx2109GT = _Pprx2109GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 367)
)
_Pprx21016GT_ObjectIdentity = ObjectIdentity
pprx21016GT = _Pprx21016GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 368)
)
_Pprx21024GT_ObjectIdentity = ObjectIdentity
pprx21024GT = _Pprx21024GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 369)
)
_Pprx51028GTX_ObjectIdentity = ObjectIdentity
pprx51028GTX = _Pprx51028GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 370)
)
_Pprx51028GPX_ObjectIdentity = ObjectIdentity
pprx51028GPX = _Pprx51028GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 371)
)
_Pprx51028GSX_ObjectIdentity = ObjectIdentity
pprx51028GSX = _Pprx51028GSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 372)
)
_Pprx51052GTX_ObjectIdentity = ObjectIdentity
pprx51052GTX = _Pprx51052GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 373)
)
_Pprx51052GPX_ObjectIdentity = ObjectIdentity
pprx51052GPX = _Pprx51052GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 374)
)
_PprAtSBx8106_ObjectIdentity = ObjectIdentity
pprAtSBx8106 = _PprAtSBx8106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 375)
)
_PprAtSBx81FAN06_ObjectIdentity = ObjectIdentity
pprAtSBx81FAN06 = _PprAtSBx81FAN06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 376)
)
_PprSBx81CFC960_ObjectIdentity = ObjectIdentity
pprSBx81CFC960 = _PprSBx81CFC960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 377)
)
_PprSBx81GT24a_ObjectIdentity = ObjectIdentity
pprSBx81GT24a = _PprSBx81GT24a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 378)
)
_PprSBx81GP24a_ObjectIdentity = ObjectIdentity
pprSBx81GP24a = _PprSBx81GP24a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 379)
)
_PprSBx81CFC960v2_ObjectIdentity = ObjectIdentity
pprSBx81CFC960v2 = _PprSBx81CFC960v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 380)
)
_PprSBx81GT40_ObjectIdentity = ObjectIdentity
pprSBx81GT40 = _PprSBx81GT40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 381)
)
_PprSBx81XS16_ObjectIdentity = ObjectIdentity
pprSBx81XS16 = _PprSBx81XS16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 382)
)
_PprAtSBxPWRSYS1DC_ObjectIdentity = ObjectIdentity
pprAtSBxPWRSYS1DC = _PprAtSBxPWRSYS1DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 383)
)
_PprPWR100R_ObjectIdentity = ObjectIdentity
pprPWR100R = _PprPWR100R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 384)
)
_PprPWR250DCR_ObjectIdentity = ObjectIdentity
pprPWR250DCR = _PprPWR250DCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 385)
)
_Pprx510DP52GTX_ObjectIdentity = ObjectIdentity
pprx510DP52GTX = _Pprx510DP52GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 386)
)
_PprIX528GPX_ObjectIdentity = ObjectIdentity
pprIX528GPX = _PprIX528GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 387)
)
_Pprx93028GTX_ObjectIdentity = ObjectIdentity
pprx93028GTX = _Pprx93028GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 388)
)
_Pprx93028GPX_ObjectIdentity = ObjectIdentity
pprx93028GPX = _Pprx93028GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 389)
)
_Pprx93028GSTX_ObjectIdentity = ObjectIdentity
pprx93028GSTX = _Pprx93028GSTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 390)
)
_Pprx93052GTX_ObjectIdentity = ObjectIdentity
pprx93052GTX = _Pprx93052GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 391)
)
_Pprx93052GPX_ObjectIdentity = ObjectIdentity
pprx93052GPX = _Pprx93052GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 392)
)
_Pprx31026FT_ObjectIdentity = ObjectIdentity
pprx31026FT = _Pprx31026FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 393)
)
_Pprx31050FT_ObjectIdentity = ObjectIdentity
pprx31050FT = _Pprx31050FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 394)
)
_Pprx31026FP_ObjectIdentity = ObjectIdentity
pprx31026FP = _Pprx31026FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 395)
)
_Pprx31050FP_ObjectIdentity = ObjectIdentity
pprx31050FP = _Pprx31050FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 396)
)
_Pprx31026GT_ObjectIdentity = ObjectIdentity
pprx31026GT = _Pprx31026GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 397)
)
_Pprx31050GT_ObjectIdentity = ObjectIdentity
pprx31050GT = _Pprx31050GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 398)
)
_Pprx31026GP_ObjectIdentity = ObjectIdentity
pprx31026GP = _Pprx31026GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 399)
)
_Pprx31050GP_ObjectIdentity = ObjectIdentity
pprx31050GP = _Pprx31050GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 400)
)
_Pprx23010GT_ObjectIdentity = ObjectIdentity
pprx23010GT = _Pprx23010GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 401)
)
_Pprx23018GT_ObjectIdentity = ObjectIdentity
pprx23018GT = _Pprx23018GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 402)
)
_Pprx23028GT_ObjectIdentity = ObjectIdentity
pprx23028GT = _Pprx23028GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 403)
)
_Pprx23052GT_ObjectIdentity = ObjectIdentity
pprx23052GT = _Pprx23052GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 404)
)
_Pprx23010GP_ObjectIdentity = ObjectIdentity
pprx23010GP = _Pprx23010GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 405)
)
_Pprx23018GP_ObjectIdentity = ObjectIdentity
pprx23018GP = _Pprx23018GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 406)
)
_Pprx23028GP_ObjectIdentity = ObjectIdentity
pprx23028GP = _Pprx23028GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 407)
)
_Pprx23052GP_ObjectIdentity = ObjectIdentity
pprx23052GP = _Pprx23052GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 408)
)
_Pprx35010GPT_ObjectIdentity = ObjectIdentity
pprx35010GPT = _Pprx35010GPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 409)
)
_PprIE2006GT_ObjectIdentity = ObjectIdentity
pprIE2006GT = _PprIE2006GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 410)
)
_PprIE2006GP_ObjectIdentity = ObjectIdentity
pprIE2006GP = _PprIE2006GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 411)
)
_PprIE2006GPW_ObjectIdentity = ObjectIdentity
pprIE2006GPW = _PprIE2006GPW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 412)
)
_Pprdc2552xs_ObjectIdentity = ObjectIdentity
pprdc2552xs = _Pprdc2552xs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 414)
)
_PprATStackQS_ObjectIdentity = ObjectIdentity
pprATStackQS = _PprATStackQS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 419)
)
_PprATx9emXT4_ObjectIdentity = ObjectIdentity
pprATx9emXT4 = _PprATx9emXT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 420)
)
_Pprx51028GSXDC_ObjectIdentity = ObjectIdentity
pprx51028GSXDC = _Pprx51028GSXDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 421)
)
_PprIE51028GSX_ObjectIdentity = ObjectIdentity
pprIE51028GSX = _PprIE51028GSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 422)
)
_PprAR3050S_ObjectIdentity = ObjectIdentity
pprAR3050S = _PprAR3050S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 423)
)
_PprAR4050S_ObjectIdentity = ObjectIdentity
pprAR4050S = _PprAR4050S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 426)
)
_PprIE2006FT_ObjectIdentity = ObjectIdentity
pprIE2006FT = _PprIE2006FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 429)
)
_PprIE2006FP_ObjectIdentity = ObjectIdentity
pprIE2006FP = _PprIE2006FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 430)
)
_Pprx510DP28GTX_ObjectIdentity = ObjectIdentity
pprx510DP28GTX = _Pprx510DP28GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 431)
)
_Pprx510L28GT_ObjectIdentity = ObjectIdentity
pprx510L28GT = _Pprx510L28GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 432)
)
_Pprx510L52GT_ObjectIdentity = ObjectIdentity
pprx510L52GT = _Pprx510L52GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 433)
)
_Pprx510L28GP_ObjectIdentity = ObjectIdentity
pprx510L28GP = _Pprx510L28GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 434)
)
_Pprx510L52GP_ObjectIdentity = ObjectIdentity
pprx510L52GP = _Pprx510L52GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 435)
)
_Pprx51028GTXR_ObjectIdentity = ObjectIdentity
pprx51028GTXR = _Pprx51028GTXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 436)
)
_Pprx51052GTXR_ObjectIdentity = ObjectIdentity
pprx51052GTXR = _Pprx51052GTXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 437)
)
_PprIE30012GT_ObjectIdentity = ObjectIdentity
pprIE30012GT = _PprIE30012GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 438)
)
_PprIE30012GP_ObjectIdentity = ObjectIdentity
pprIE30012GP = _PprIE30012GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 439)
)
_PprIE30012GS_ObjectIdentity = ObjectIdentity
pprIE30012GS = _PprIE30012GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 440)
)
_PprIE30020GST_ObjectIdentity = ObjectIdentity
pprIE30020GST = _PprIE30020GST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 441)
)
_PprVAA_ObjectIdentity = ObjectIdentity
pprVAA = _PprVAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 442)
)
_PprAtGS924MX_ObjectIdentity = ObjectIdentity
pprAtGS924MX = _PprAtGS924MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 443)
)
_PprAtGS924MPX_ObjectIdentity = ObjectIdentity
pprAtGS924MPX = _PprAtGS924MPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 444)
)
_PprAtGS948MX_ObjectIdentity = ObjectIdentity
pprAtGS948MX = _PprAtGS948MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 445)
)
_PprAtGS948MPX_ObjectIdentity = ObjectIdentity
pprAtGS948MPX = _PprAtGS948MPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 446)
)
_PprAtSBx81XLEM_ObjectIdentity = ObjectIdentity
pprAtSBx81XLEM = _PprAtSBx81XLEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 447)
)
_PprAtSBx81XLEMemXS8_ObjectIdentity = ObjectIdentity
pprAtSBx81XLEMemXS8 = _PprAtSBx81XLEMemXS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 448)
)
_PprAtSBx81XLEMemQ2_ObjectIdentity = ObjectIdentity
pprAtSBx81XLEMemQ2 = _PprAtSBx81XLEMemQ2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 449)
)
_PprAtSBx81XLEMemXT4_ObjectIdentity = ObjectIdentity
pprAtSBx81XLEMemXT4 = _PprAtSBx81XLEMemXT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 450)
)
_PprAtSBx81XLEMemGT8_ObjectIdentity = ObjectIdentity
pprAtSBx81XLEMemGT8 = _PprAtSBx81XLEMemGT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 451)
)
_PprAtSBxPWRSYS2AC_ObjectIdentity = ObjectIdentity
pprAtSBxPWRSYS2AC = _PprAtSBxPWRSYS2AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 452)
)
_PprPWR150_ObjectIdentity = ObjectIdentity
pprPWR150 = _PprPWR150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 453)
)
_PprAR2050V_ObjectIdentity = ObjectIdentity
pprAR2050V = _PprAR2050V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 454)
)
_PprAR2010V_ObjectIdentity = ObjectIdentity
pprAR2010V = _PprAR2010V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 455)
)
_PprAtXS916MXT_ObjectIdentity = ObjectIdentity
pprAtXS916MXT = _PprAtXS916MXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 456)
)
_PprAtXS916MXS_ObjectIdentity = ObjectIdentity
pprAtXS916MXS = _PprAtXS916MXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 457)
)
_PprAtXS916MXP_ObjectIdentity = ObjectIdentity
pprAtXS916MXP = _PprAtXS916MXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 458)
)
_PprSH51028GTX_ObjectIdentity = ObjectIdentity
pprSH51028GTX = _PprSH51028GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 459)
)
_PprSH51052GTX_ObjectIdentity = ObjectIdentity
pprSH51052GTX = _PprSH51052GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 460)
)
_PprSH51028GPX_ObjectIdentity = ObjectIdentity
pprSH51028GPX = _PprSH51028GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 461)
)
_PprSH51052GPX_ObjectIdentity = ObjectIdentity
pprSH51052GPX = _PprSH51052GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 462)
)
_PprSH23010GP_ObjectIdentity = ObjectIdentity
pprSH23010GP = _PprSH23010GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 463)
)
_PprSH23018GP_ObjectIdentity = ObjectIdentity
pprSH23018GP = _PprSH23018GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 464)
)
_PprSH23028GP_ObjectIdentity = ObjectIdentity
pprSH23028GP = _PprSH23028GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 465)
)
_PprSH2109GT_ObjectIdentity = ObjectIdentity
pprSH2109GT = _PprSH2109GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 466)
)
_PprSH21016GT_ObjectIdentity = ObjectIdentity
pprSH21016GT = _PprSH21016GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 467)
)
_PprSH21024GT_ObjectIdentity = ObjectIdentity
pprSH21024GT = _PprSH21024GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 468)
)
_PprSH31026FT_ObjectIdentity = ObjectIdentity
pprSH31026FT = _PprSH31026FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 469)
)
_PprSH31050FT_ObjectIdentity = ObjectIdentity
pprSH31050FT = _PprSH31050FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 470)
)
_PprSH31026FP_ObjectIdentity = ObjectIdentity
pprSH31026FP = _PprSH31026FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 471)
)
_PprSH31050FP_ObjectIdentity = ObjectIdentity
pprSH31050FP = _PprSH31050FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 472)
)
_PprSH23010GT_ObjectIdentity = ObjectIdentity
pprSH23010GT = _PprSH23010GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 473)
)
_PprSH23018GT_ObjectIdentity = ObjectIdentity
pprSH23018GT = _PprSH23018GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 474)
)
_PprSH23028GT_ObjectIdentity = ObjectIdentity
pprSH23028GT = _PprSH23028GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 475)
)
_PprAtFS980M9_ObjectIdentity = ObjectIdentity
pprAtFS980M9 = _PprAtFS980M9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 476)
)
_PprAtFS980M9PS_ObjectIdentity = ObjectIdentity
pprAtFS980M9PS = _PprAtFS980M9PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 477)
)
_PprAtFS980M18_ObjectIdentity = ObjectIdentity
pprAtFS980M18 = _PprAtFS980M18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 478)
)
_PprAtFS980M18PS_ObjectIdentity = ObjectIdentity
pprAtFS980M18PS = _PprAtFS980M18PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 479)
)
_PprAtFS980M28_ObjectIdentity = ObjectIdentity
pprAtFS980M28 = _PprAtFS980M28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 480)
)
_PprAtFS980M28PS_ObjectIdentity = ObjectIdentity
pprAtFS980M28PS = _PprAtFS980M28PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 481)
)
_PprAtFS980M52_ObjectIdentity = ObjectIdentity
pprAtFS980M52 = _PprAtFS980M52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 482)
)
_PprAtFS980M52PS_ObjectIdentity = ObjectIdentity
pprAtFS980M52PS = _PprAtFS980M52PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 483)
)
_PprSBx908G2_ObjectIdentity = ObjectIdentity
pprSBx908G2 = _PprSBx908G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 484)
)
_PprSBx908G3_ObjectIdentity = ObjectIdentity
pprSBx908G3 = _PprSBx908G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 485)
)
_PprAtFan08_ObjectIdentity = ObjectIdentity
pprAtFan08 = _PprAtFan08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 486)
)
_PprAtXem2QS4_ObjectIdentity = ObjectIdentity
pprAtXem2QS4 = _PprAtXem2QS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 487)
)
_PprAtXem2XS12_ObjectIdentity = ObjectIdentity
pprAtXem2XS12 = _PprAtXem2XS12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 488)
)
_PprAtXem2XT12_ObjectIdentity = ObjectIdentity
pprAtXem2XT12 = _PprAtXem2XT12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 489)
)
_PprAtXem3QS8_ObjectIdentity = ObjectIdentity
pprAtXem3QS8 = _PprAtXem3QS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 490)
)
_Pprx55018XTQ_ObjectIdentity = ObjectIdentity
pprx55018XTQ = _Pprx55018XTQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 491)
)
_Pprx55018XSQ_ObjectIdentity = ObjectIdentity
pprx55018XSQ = _Pprx55018XSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 492)
)
_Pprx55018XSPQm_ObjectIdentity = ObjectIdentity
pprx55018XSPQm = _Pprx55018XSPQm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 493)
)
_PprAtXem2CQ1_ObjectIdentity = ObjectIdentity
pprAtXem2CQ1 = _PprAtXem2CQ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 494)
)
_PprAtGS910M_ObjectIdentity = ObjectIdentity
pprAtGS910M = _PprAtGS910M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 496)
)
_PprAtGS910MP_ObjectIdentity = ObjectIdentity
pprAtGS910MP = _PprAtGS910MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 497)
)
_PprAtGS918M_ObjectIdentity = ObjectIdentity
pprAtGS918M = _PprAtGS918M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 498)
)
_PprAtGS918MP_ObjectIdentity = ObjectIdentity
pprAtGS918MP = _PprAtGS918MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 499)
)
_PprAtGS928M_ObjectIdentity = ObjectIdentity
pprAtGS928M = _PprAtGS928M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 500)
)
_PprAtGS928MP_ObjectIdentity = ObjectIdentity
pprAtGS928MP = _PprAtGS928MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 501)
)
_PprAtGS952M_ObjectIdentity = ObjectIdentity
pprAtGS952M = _PprAtGS952M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 502)
)
_PprAtGS952MP_ObjectIdentity = ObjectIdentity
pprAtGS952MP = _PprAtGS952MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 503)
)
_Pprx22052GT_ObjectIdentity = ObjectIdentity
pprx22052GT = _Pprx22052GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 505)
)
_Pprx22052GP_ObjectIdentity = ObjectIdentity
pprx22052GP = _Pprx22052GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 506)
)
_Pprx22028GS_ObjectIdentity = ObjectIdentity
pprx22028GS = _Pprx22028GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 509)
)
_PprAtGS980M52_ObjectIdentity = ObjectIdentity
pprAtGS980M52 = _PprAtGS980M52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 515)
)
_PprAtGS980M52PS_ObjectIdentity = ObjectIdentity
pprAtGS980M52PS = _PprAtGS980M52PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 516)
)
_Pprx53028GTXm_ObjectIdentity = ObjectIdentity
pprx53028GTXm = _Pprx53028GTXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 523)
)
_Pprx53028GPXm_ObjectIdentity = ObjectIdentity
pprx53028GPXm = _Pprx53028GPXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 524)
)
_Pprx530DP28GHXm_ObjectIdentity = ObjectIdentity
pprx530DP28GHXm = _Pprx530DP28GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 526)
)
_Pprx53052GTXm_ObjectIdentity = ObjectIdentity
pprx53052GTXm = _Pprx53052GTXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 527)
)
_Pprx53052GPXm_ObjectIdentity = ObjectIdentity
pprx53052GPXm = _Pprx53052GPXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 528)
)
_Pprx530DP52GHXm_ObjectIdentity = ObjectIdentity
pprx530DP52GHXm = _Pprx530DP52GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 529)
)
_PprAtGS980MX28_ObjectIdentity = ObjectIdentity
pprAtGS980MX28 = _PprAtGS980MX28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 530)
)
_PprAtGS980MX28PSm_ObjectIdentity = ObjectIdentity
pprAtGS980MX28PSm = _PprAtGS980MX28PSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 531)
)
_PprAtGS980MX52_ObjectIdentity = ObjectIdentity
pprAtGS980MX52 = _PprAtGS980MX52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 532)
)
_PprAtGS980MX52PSm_ObjectIdentity = ObjectIdentity
pprAtGS980MX52PSm = _PprAtGS980MX52PSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 533)
)
_PprAtGS970M28PS_ObjectIdentity = ObjectIdentity
pprAtGS970M28PS = _PprAtGS970M28PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 534)
)
_PprAtGS970M18PS_ObjectIdentity = ObjectIdentity
pprAtGS970M18PS = _PprAtGS970M18PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 535)
)
_PprAtGS970M10PS_ObjectIdentity = ObjectIdentity
pprAtGS970M10PS = _PprAtGS970M10PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 536)
)
_PprAtGS970M28_ObjectIdentity = ObjectIdentity
pprAtGS970M28 = _PprAtGS970M28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 537)
)
_PprAtGS970M18_ObjectIdentity = ObjectIdentity
pprAtGS970M18 = _PprAtGS970M18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 538)
)
_PprAtGS970M10_ObjectIdentity = ObjectIdentity
pprAtGS970M10 = _PprAtGS970M10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 539)
)
_PprAtIE34012GP_ObjectIdentity = ObjectIdentity
pprAtIE34012GP = _PprAtIE34012GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 540)
)
_PprAtIE340L18GP_ObjectIdentity = ObjectIdentity
pprAtIE340L18GP = _PprAtIE340L18GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 541)
)
_PprAtIE34012GT_ObjectIdentity = ObjectIdentity
pprAtIE34012GT = _PprAtIE34012GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 542)
)
_PprAtIE34020GP_ObjectIdentity = ObjectIdentity
pprAtIE34020GP = _PprAtIE34020GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 543)
)
_PprIE21010GP_ObjectIdentity = ObjectIdentity
pprIE21010GP = _PprIE21010GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 544)
)
_PprIE21018GP_ObjectIdentity = ObjectIdentity
pprIE21018GP = _PprIE21018GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 545)
)
_PprAtXem2XTm12_ObjectIdentity = ObjectIdentity
pprAtXem2XTm12 = _PprAtXem2XTm12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 546)
)
_PprAtXem2XSTm8_ObjectIdentity = ObjectIdentity
pprAtXem2XSTm8 = _PprAtXem2XSTm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 547)
)
_Pprx95028XTQm_ObjectIdentity = ObjectIdentity
pprx95028XTQm = _Pprx95028XTQm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 548)
)
_Pprx95028XSQ_ObjectIdentity = ObjectIdentity
pprx95028XSQ = _Pprx95028XSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 549)
)
_Pprx230L17GT_ObjectIdentity = ObjectIdentity
pprx230L17GT = _Pprx230L17GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 556)
)
_Pprx230L26GT_ObjectIdentity = ObjectIdentity
pprx230L26GT = _Pprx230L26GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 557)
)
_Pprx32010GH_ObjectIdentity = ObjectIdentity
pprx32010GH = _Pprx32010GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 558)
)
_Pprx32011GPT_ObjectIdentity = ObjectIdentity
pprx32011GPT = _Pprx32011GPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 559)
)
_PprAtXem2XS12V2_ObjectIdentity = ObjectIdentity
pprAtXem2XS12V2 = _PprAtXem2XS12V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 560)
)
_PprAR1050V_ObjectIdentity = ObjectIdentity
pprAR1050V = _PprAR1050V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 561)
)
_PprAtSBx81GC40_ObjectIdentity = ObjectIdentity
pprAtSBx81GC40 = _PprAtSBx81GC40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 562)
)
_Pprx55018XSQV2_ObjectIdentity = ObjectIdentity
pprx55018XSQV2 = _Pprx55018XSQV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 563)
)
_Pprx530L28GTX_ObjectIdentity = ObjectIdentity
pprx530L28GTX = _Pprx530L28GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 568)
)
_Pprx530L28GPX_ObjectIdentity = ObjectIdentity
pprx530L28GPX = _Pprx530L28GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 569)
)
_Pprx530L52GTX_ObjectIdentity = ObjectIdentity
pprx530L52GTX = _Pprx530L52GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 570)
)
_Pprx530L52GPX_ObjectIdentity = ObjectIdentity
pprx530L52GPX = _Pprx530L52GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 571)
)
_PprAtFS980M28DP_ObjectIdentity = ObjectIdentity
pprAtFS980M28DP = _PprAtFS980M28DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 573)
)
_PprAtSBx81FAN12v2_ObjectIdentity = ObjectIdentity
pprAtSBx81FAN12v2 = _PprAtSBx81FAN12v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 575)
)
_Pprx95052XTQm_ObjectIdentity = ObjectIdentity
pprx95052XTQm = _Pprx95052XTQm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 576)
)
_Pprx95052XSQ_ObjectIdentity = ObjectIdentity
pprx95052XSQ = _Pprx95052XSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 577)
)
_PprAtGS980EM10H_ObjectIdentity = ObjectIdentity
pprAtGS980EM10H = _PprAtGS980EM10H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 578)
)
_PprAtGS980EM11PT_ObjectIdentity = ObjectIdentity
pprAtGS980EM11PT = _PprAtGS980EM11PT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 579)
)
_PprAtSBx81GP24v2_ObjectIdentity = ObjectIdentity
pprAtSBx81GP24v2 = _PprAtSBx81GP24v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 581)
)
_Pprx530L10GHXm_ObjectIdentity = ObjectIdentity
pprx530L10GHXm = _Pprx530L10GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 582)
)
_Pprx53010GHXm_ObjectIdentity = ObjectIdentity
pprx53010GHXm = _Pprx53010GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 584)
)
_Pprx53018GHXm_ObjectIdentity = ObjectIdentity
pprx53018GHXm = _Pprx53018GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 585)
)
_PprAtGS980MX10HSm_ObjectIdentity = ObjectIdentity
pprAtGS980MX10HSm = _PprAtGS980MX10HSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 586)
)
_PprSBx81CFC960v2a_ObjectIdentity = ObjectIdentity
pprSBx81CFC960v2a = _PprSBx81CFC960v2a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 588)
)
_PprAR4050S5G_ObjectIdentity = ObjectIdentity
pprAR4050S5G = _PprAR4050S5G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 599)
)
_PprvFW_ObjectIdentity = ObjectIdentity
pprvFW = _PprvFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 601)
)
_Release_ObjectIdentity = ObjectIdentity
release = _Release_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 2)
)
_Iftypes_ObjectIdentity = ObjectIdentity
iftypes = _Iftypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3)
)
_IfaceEth_ObjectIdentity = ObjectIdentity
ifaceEth = _IfaceEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 1)
)
_IfaceSyn_ObjectIdentity = ObjectIdentity
ifaceSyn = _IfaceSyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 2)
)
_IfaceAsyn_ObjectIdentity = ObjectIdentity
ifaceAsyn = _IfaceAsyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 3)
)
_IfaceBri_ObjectIdentity = ObjectIdentity
ifaceBri = _IfaceBri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 4)
)
_IfacePri_ObjectIdentity = ObjectIdentity
ifacePri = _IfacePri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 5)
)
_IfacePots_ObjectIdentity = ObjectIdentity
ifacePots = _IfacePots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 6)
)
_IfaceGBIC_ObjectIdentity = ObjectIdentity
ifaceGBIC = _IfaceGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 7)
)
_Chips_ObjectIdentity = ObjectIdentity
chips = _Chips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4)
)
_Chip68020Cpu_ObjectIdentity = ObjectIdentity
chip68020Cpu = _Chip68020Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 1)
)
_Chip68340Cpu_ObjectIdentity = ObjectIdentity
chip68340Cpu = _Chip68340Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 2)
)
_Chip68302Cpu_ObjectIdentity = ObjectIdentity
chip68302Cpu = _Chip68302Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 3)
)
_Chip68360Cpu_ObjectIdentity = ObjectIdentity
chip68360Cpu = _Chip68360Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 4)
)
_Chip860TCpu_ObjectIdentity = ObjectIdentity
chip860TCpu = _Chip860TCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 5)
)
_ChipMips4kcCpu_ObjectIdentity = ObjectIdentity
chipMips4kcCpu = _ChipMips4kcCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 6)
)
_ChipRtc1_ObjectIdentity = ObjectIdentity
chipRtc1 = _ChipRtc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 21)
)
_ChipRtc2_ObjectIdentity = ObjectIdentity
chipRtc2 = _ChipRtc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 22)
)
_ChipRtc3_ObjectIdentity = ObjectIdentity
chipRtc3 = _ChipRtc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 23)
)
_ChipRtc4_ObjectIdentity = ObjectIdentity
chipRtc4 = _ChipRtc4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 24)
)
_ChipRam1mb_ObjectIdentity = ObjectIdentity
chipRam1mb = _ChipRam1mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 31)
)
_ChipRam2mb_ObjectIdentity = ObjectIdentity
chipRam2mb = _ChipRam2mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 32)
)
_ChipRam3mb_ObjectIdentity = ObjectIdentity
chipRam3mb = _ChipRam3mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 33)
)
_ChipRam4mb_ObjectIdentity = ObjectIdentity
chipRam4mb = _ChipRam4mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 34)
)
_ChipRam6mb_ObjectIdentity = ObjectIdentity
chipRam6mb = _ChipRam6mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 36)
)
_ChipRam8mb_ObjectIdentity = ObjectIdentity
chipRam8mb = _ChipRam8mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 38)
)
_ChipRam12mb_ObjectIdentity = ObjectIdentity
chipRam12mb = _ChipRam12mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 42)
)
_ChipRam16mb_ObjectIdentity = ObjectIdentity
chipRam16mb = _ChipRam16mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 46)
)
_ChipRam20mb_ObjectIdentity = ObjectIdentity
chipRam20mb = _ChipRam20mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 50)
)
_ChipRam32mb_ObjectIdentity = ObjectIdentity
chipRam32mb = _ChipRam32mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 62)
)
_ChipFlash1mb_ObjectIdentity = ObjectIdentity
chipFlash1mb = _ChipFlash1mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 71)
)
_ChipFlash2mb_ObjectIdentity = ObjectIdentity
chipFlash2mb = _ChipFlash2mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 72)
)
_ChipFlash3mb_ObjectIdentity = ObjectIdentity
chipFlash3mb = _ChipFlash3mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 73)
)
_ChipFlash4mb_ObjectIdentity = ObjectIdentity
chipFlash4mb = _ChipFlash4mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 74)
)
_ChipFlash6mb_ObjectIdentity = ObjectIdentity
chipFlash6mb = _ChipFlash6mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 76)
)
_ChipFlash8mb_ObjectIdentity = ObjectIdentity
chipFlash8mb = _ChipFlash8mb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 78)
)
_ChipPem_ObjectIdentity = ObjectIdentity
chipPem = _ChipPem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 120)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-BOARDS-MIB",
    **{"boards": boards,
       "pprIcmAr023": pprIcmAr023,
       "pprIcmAr021s": pprIcmAr021s,
       "pprIcmAr022": pprIcmAr022,
       "pprIcmAr025": pprIcmAr025,
       "pprIcmAr024": pprIcmAr024,
       "pprAr300": pprAr300,
       "pprAr300L": pprAr300L,
       "pprAr310": pprAr310,
       "pprAr120": pprAr120,
       "pprAr300Lu": pprAr300Lu,
       "pprAr300u": pprAr300u,
       "pprAr310u": pprAr310u,
       "pprAr350": pprAr350,
       "pprIcmAr021u": pprIcmAr021u,
       "pprAr720": pprAr720,
       "pprAr010": pprAr010,
       "pprAr012": pprAr012,
       "pprAr011": pprAr011,
       "pprAr370": pprAr370,
       "pprAr330": pprAr330,
       "pprAr395": pprAr395,
       "pprAr390": pprAr390,
       "pprAr370u": pprAr370u,
       "pprIcmAr020": pprIcmAr020,
       "pprAr740": pprAr740,
       "pprAr140s": pprAr140s,
       "pprAr140u": pprAr140u,
       "pprAr160su": pprAr160su,
       "pprAr320": pprAr320,
       "pprAr130s": pprAr130s,
       "pprAr130u": pprAr130u,
       "pprRapier24": pprRapier24,
       "pprNsm0404Pic": pprNsm0404Pic,
       "pprA35SXSC": pprA35SXSC,
       "pprA35LXSC": pprA35LXSC,
       "pprA36MTRJ": pprA36MTRJ,
       "pprA37VF45": pprA37VF45,
       "pprA38LC": pprA38LC,
       "pprA39Tx": pprA39Tx,
       "pprAr740DC": pprAr740DC,
       "pprNsm0418BRI": pprNsm0418BRI,
       "pprRapier16fSC": pprRapier16fSC,
       "ppr8624xl80": ppr8624xl80,
       "pprRapier16fMT": pprRapier16fMT,
       "pprRapier16fMTi": pprRapier16fMTi,
       "pprRapier8t8fSC": pprRapier8t8fSC,
       "pprRapier8t8fSCi": pprRapier8t8fSCi,
       "pprRapier8t8fMT": pprRapier8t8fMT,
       "pprRapier8t8fMTi": pprRapier8t8fMTi,
       "pprRapier8fSC": pprRapier8fSC,
       "pprRapier8fSCi": pprRapier8fSCi,
       "pprRapier8fMT": pprRapier8fMT,
       "pprRapier8fMTi": pprRapier8fMTi,
       "pprRapierG6": pprRapierG6,
       "pprRapierG6SX": pprRapierG6SX,
       "pprRapierG6LX": pprRapierG6LX,
       "pprRapierG6MT": pprRapierG6MT,
       "pprRapier16fSCi": pprRapier16fSCi,
       "pprRapier24i": pprRapier24i,
       "pprAr824": pprAr824,
       "pprAr816fSC": pprAr816fSC,
       "pprAr816fSCi": pprAr816fSCi,
       "pprAr816fMT": pprAr816fMT,
       "pprAr816fMTi": pprAr816fMTi,
       "pprAr88t8fSC": pprAr88t8fSC,
       "pprAr88t8fSCi": pprAr88t8fSCi,
       "pprAr88t8fMT": pprAr88t8fMT,
       "pprAr88t8fMTi": pprAr88t8fMTi,
       "pprAr88fSC": pprAr88fSC,
       "pprAr88fSCi": pprAr88fSCi,
       "pprAr88fMT": pprAr88fMT,
       "pprAr88fMTi": pprAr88fMTi,
       "pprAr824i": pprAr824i,
       "pprAt8724XL": pprAt8724XL,
       "pprAt8748XL": pprAt8748XL,
       "pprAt8724XLDC": pprAt8724XLDC,
       "pprAt8748XLDC": pprAt8748XLDC,
       "pprAt8824": pprAt8824,
       "pprAt8824DC": pprAt8824DC,
       "ppr8724XLDC": ppr8724XLDC,
       "ppr8748XLDC": ppr8748XLDC,
       "pprRapier24iDcNEBS": pprRapier24iDcNEBS,
       "pprAt8724XLDcNEBS": pprAt8724XLDcNEBS,
       "pprAt8848DC": pprAt8848DC,
       "pprRapier48": pprRapier48,
       "pprAt8848": pprAt8848,
       "pprRapier48i": pprRapier48i,
       "pprNsm0424BRI": pprNsm0424BRI,
       "pprIcmAR026": pprIcmAR026,
       "ppr9816GF": ppr9816GF,
       "ppr9812TF": ppr9812TF,
       "pprSbChassis4AC": pprSbChassis4AC,
       "pprSbChassis4DC": pprSbChassis4DC,
       "pprSbChassis8AC": pprSbChassis8AC,
       "pprSbChassis8DC": pprSbChassis8DC,
       "pprSbChassis16AC": pprSbChassis16AC,
       "pprSbChassis16DC": pprSbChassis16DC,
       "pprSbControl": pprSbControl,
       "pprSbControlDTM": pprSbControlDTM,
       "pprSb48t": pprSb48t,
       "pprSb96t": pprSb96t,
       "pprSb32fSC": pprSb32fSC,
       "pprSb32fMT": pprSb32fMT,
       "pprSb8fRJ": pprSb8fRJ,
       "pprSb8fSXSC": pprSb8fSXSC,
       "pprSb8fSXMT": pprSb8fSXMT,
       "pprSb8fLXSC": pprSb8fLXSC,
       "pprSb8fLXMT": pprSb8fLXMT,
       "pprAr410": pprAr410,
       "pprA40SC": pprA40SC,
       "pprA40MTRJ": pprA40MTRJ,
       "pprA41SC": pprA41SC,
       "pprA41MTRJ": pprA41MTRJ,
       "pprAr725": pprAr725,
       "pprAr745": pprAr745,
       "pprSb8GBIC": pprSb8GBIC,
       "pprA42GBIC": pprA42GBIC,
       "ppr9816GB": ppr9816GB,
       "ppr9812T": ppr9812T,
       "pprNsm048DS3": pprNsm048DS3,
       "pprAr450": pprAr450,
       "pprAr450Dual": pprAr450Dual,
       "pprSbExpander": pprSbExpander,
       "pprAr725DC": pprAr725DC,
       "pprAr745DC": pprAr745DC,
       "pprAr410v2": pprAr410v2,
       "pprAr410v3": pprAr410v3,
       "pprIcmAr027": pprIcmAr027,
       "ppr8948EX": ppr8948EX,
       "ppr8948i": ppr8948i,
       "ppr9816GBDC": ppr9816GBDC,
       "ppr9812TDC": ppr9812TDC,
       "pprIcmAr021v2s": pprIcmAr021v2s,
       "pprA50": pprA50,
       "pprA51": pprA51,
       "pprA52": pprA52,
       "pprA53": pprA53,
       "pprFanA01": pprFanA01,
       "pprAtPwr01AC": pprAtPwr01AC,
       "pprAtPwr01DC": pprAtPwr01DC,
       "pprAtFan01": pprAtFan01,
       "pprSb24RJ": pprSb24RJ,
       "pprSb1XFP": pprSb1XFP,
       "ppr9924T": ppr9924T,
       "ppr9924SP": ppr9924SP,
       "ppr9924TEMC": ppr9924TEMC,
       "ppr9924T4SP": ppr9924T4SP,
       "pprAR440": pprAR440,
       "pprAR441": pprAR441,
       "pprAR442": pprAR442,
       "pprAR443": pprAR443,
       "pprAR444": pprAR444,
       "pprAR420": pprAR420,
       "pprAt8624T2M": pprAt8624T2M,
       "pprA46Tx": pprA46Tx,
       "pprAR550": pprAR550,
       "pprAR551": pprAR551,
       "pprAR552": pprAR552,
       "pprC8724MLB": pprC8724MLB,
       "pprAt86482SP": pprAt86482SP,
       "pprAt8624POE": pprAt8624POE,
       "pprAtPwr01RAC": pprAtPwr01RAC,
       "pprAtFan01R": pprAtFan01R,
       "ppr9924Ts": ppr9924Ts,
       "pprAR570": pprAR570,
       "pprAtPwr02AC": pprAtPwr02AC,
       "pprAtPwr02RAC": pprAtPwr02RAC,
       "pprAtXum10G": pprAtXum10G,
       "pprAtXum12T": pprAtXum12T,
       "pprAtXum12SFP": pprAtXum12SFP,
       "pprSb24SFP": pprSb24SFP,
       "pprAR770": pprAR770,
       "pprx90024XT": pprx90024XT,
       "pprx90024XS": pprx90024XS,
       "pprAtXum10Gi": pprAtXum10Gi,
       "pprAtXum12SFPi": pprAtXum12SFPi,
       "pprAtXum12Ti": pprAtXum12Ti,
       "pprAR415S": pprAR415S,
       "pprAR415SDC": pprAR415SDC,
       "pprAR550SDP": pprAR550SDP,
       "ppr8948iN": ppr8948iN,
       "pprAtXum12TiN": pprAtXum12TiN,
       "pprx90024XTN": pprx90024XTN,
       "pprSwitchBladex908": pprSwitchBladex908,
       "pprRapier48w": pprRapier48w,
       "pprAt8316XLCR": pprAt8316XLCR,
       "pprAt8324XLCR": pprAt8324XLCR,
       "pprXemStk": pprXemStk,
       "pprAt8824R": pprAt8824R,
       "pprx90012XTS": pprx90012XTS,
       "pprX90048FS": pprX90048FS,
       "pprx60024TS": pprx60024TS,
       "pprx60024TSXP": pprx60024TSXP,
       "pprAt9724TS": pprAt9724TS,
       "pprAt9724TSXP": pprAt9724TSXP,
       "pprx60048TS": pprx60048TS,
       "pprx60048TSXP": pprx60048TSXP,
       "pprAt9748TS": pprAt9748TS,
       "pprAt9748TSXP": pprAt9748TSXP,
       "pprXum100M": pprXum100M,
       "pprAtPWR05AC": pprAtPWR05AC,
       "pprIcmAr021v3s": pprIcmAr021v3s,
       "pprRapier48wb": pprRapier48wb,
       "pprRapier48wAC": pprRapier48wAC,
       "pprRapier48wbAC": pprRapier48wbAC,
       "pprX30024TS": pprX30024TS,
       "pprXemPOE": pprXemPOE,
       "pprXem2XP": pprXem2XP,
       "pprATStackXG": pprATStackXG,
       "pprATEMXP": pprATEMXP,
       "pprATLBM": pprATLBM,
       "pprAt8624TCR": pprAt8624TCR,
       "pprAt8624POECR": pprAt8624POECR,
       "pprAtSBx8112": pprAtSBx8112,
       "pprAtSBx81CFC400": pprAtSBx81CFC400,
       "pprAtSBx81GP24": pprAtSBx81GP24,
       "pprAtSBx81XZ4": pprAtSBx81XZ4,
       "pprAtSBx8161SYSAC": pprAtSBx8161SYSAC,
       "pprAtSBx8165POEAC": pprAtSBx8165POEAC,
       "pprAtSBx81FAN": pprAtSBx81FAN,
       "pprAtPWR05DC": pprAtPWR05DC,
       "pprXem2XT": pprXem2XT,
       "pprx60024TSPOE": pprx60024TSPOE,
       "pprx60024TSPOEPLUS": pprx60024TSPOEPLUS,
       "pprAR560": pprAR560,
       "pprx61048TsXPOEPlus": pprx61048TsXPOEPlus,
       "pprx61048TsPOEPlus": pprx61048TsPOEPlus,
       "pprx61024TsXPOEPlus": pprx61024TsXPOEPlus,
       "pprx61024TsPOEPlus": pprx61024TsPOEPlus,
       "pprPWR800": pprPWR800,
       "pprPWR1200": pprPWR1200,
       "pprPWR250": pprPWR250,
       "pprx61048TsX": pprx61048TsX,
       "pprx61048Ts": pprx61048Ts,
       "pprx61024TsX": pprx61024TsX,
       "pprx61024Ts": pprx61024Ts,
       "pprx61024SPX": pprx61024SPX,
       "pprRapier48xDC": pprRapier48xDC,
       "pprAR030": pprAR030,
       "pprx200GE52T": pprx200GE52T,
       "pprx200GE28T": pprx200GE28T,
       "pprXem2XS": pprXem2XS,
       "pprPWR250DC": pprPWR250DC,
       "pprAtSBx81GT24": pprAtSBx81GT24,
       "pprAtSBx81GS24a": pprAtSBx81GS24a,
       "pprAtSBx81XS6": pprAtSBx81XS6,
       "pprXem24T": pprXem24T,
       "pprAR031": pprAR031,
       "pprXem12Tv2": pprXem12Tv2,
       "pprXem12Sv2": pprXem12Sv2,
       "pprx2109GT": pprx2109GT,
       "pprx21016GT": pprx21016GT,
       "pprx21024GT": pprx21024GT,
       "pprx51028GTX": pprx51028GTX,
       "pprx51028GPX": pprx51028GPX,
       "pprx51028GSX": pprx51028GSX,
       "pprx51052GTX": pprx51052GTX,
       "pprx51052GPX": pprx51052GPX,
       "pprAtSBx8106": pprAtSBx8106,
       "pprAtSBx81FAN06": pprAtSBx81FAN06,
       "pprSBx81CFC960": pprSBx81CFC960,
       "pprSBx81GT24a": pprSBx81GT24a,
       "pprSBx81GP24a": pprSBx81GP24a,
       "pprSBx81CFC960v2": pprSBx81CFC960v2,
       "pprSBx81GT40": pprSBx81GT40,
       "pprSBx81XS16": pprSBx81XS16,
       "pprAtSBxPWRSYS1DC": pprAtSBxPWRSYS1DC,
       "pprPWR100R": pprPWR100R,
       "pprPWR250DCR": pprPWR250DCR,
       "pprx510DP52GTX": pprx510DP52GTX,
       "pprIX528GPX": pprIX528GPX,
       "pprx93028GTX": pprx93028GTX,
       "pprx93028GPX": pprx93028GPX,
       "pprx93028GSTX": pprx93028GSTX,
       "pprx93052GTX": pprx93052GTX,
       "pprx93052GPX": pprx93052GPX,
       "pprx31026FT": pprx31026FT,
       "pprx31050FT": pprx31050FT,
       "pprx31026FP": pprx31026FP,
       "pprx31050FP": pprx31050FP,
       "pprx31026GT": pprx31026GT,
       "pprx31050GT": pprx31050GT,
       "pprx31026GP": pprx31026GP,
       "pprx31050GP": pprx31050GP,
       "pprx23010GT": pprx23010GT,
       "pprx23018GT": pprx23018GT,
       "pprx23028GT": pprx23028GT,
       "pprx23052GT": pprx23052GT,
       "pprx23010GP": pprx23010GP,
       "pprx23018GP": pprx23018GP,
       "pprx23028GP": pprx23028GP,
       "pprx23052GP": pprx23052GP,
       "pprx35010GPT": pprx35010GPT,
       "pprIE2006GT": pprIE2006GT,
       "pprIE2006GP": pprIE2006GP,
       "pprIE2006GPW": pprIE2006GPW,
       "pprdc2552xs": pprdc2552xs,
       "pprATStackQS": pprATStackQS,
       "pprATx9emXT4": pprATx9emXT4,
       "pprx51028GSXDC": pprx51028GSXDC,
       "pprIE51028GSX": pprIE51028GSX,
       "pprAR3050S": pprAR3050S,
       "pprAR4050S": pprAR4050S,
       "pprIE2006FT": pprIE2006FT,
       "pprIE2006FP": pprIE2006FP,
       "pprx510DP28GTX": pprx510DP28GTX,
       "pprx510L28GT": pprx510L28GT,
       "pprx510L52GT": pprx510L52GT,
       "pprx510L28GP": pprx510L28GP,
       "pprx510L52GP": pprx510L52GP,
       "pprx51028GTXR": pprx51028GTXR,
       "pprx51052GTXR": pprx51052GTXR,
       "pprIE30012GT": pprIE30012GT,
       "pprIE30012GP": pprIE30012GP,
       "pprIE30012GS": pprIE30012GS,
       "pprIE30020GST": pprIE30020GST,
       "pprVAA": pprVAA,
       "pprAtGS924MX": pprAtGS924MX,
       "pprAtGS924MPX": pprAtGS924MPX,
       "pprAtGS948MX": pprAtGS948MX,
       "pprAtGS948MPX": pprAtGS948MPX,
       "pprAtSBx81XLEM": pprAtSBx81XLEM,
       "pprAtSBx81XLEMemXS8": pprAtSBx81XLEMemXS8,
       "pprAtSBx81XLEMemQ2": pprAtSBx81XLEMemQ2,
       "pprAtSBx81XLEMemXT4": pprAtSBx81XLEMemXT4,
       "pprAtSBx81XLEMemGT8": pprAtSBx81XLEMemGT8,
       "pprAtSBxPWRSYS2AC": pprAtSBxPWRSYS2AC,
       "pprPWR150": pprPWR150,
       "pprAR2050V": pprAR2050V,
       "pprAR2010V": pprAR2010V,
       "pprAtXS916MXT": pprAtXS916MXT,
       "pprAtXS916MXS": pprAtXS916MXS,
       "pprAtXS916MXP": pprAtXS916MXP,
       "pprSH51028GTX": pprSH51028GTX,
       "pprSH51052GTX": pprSH51052GTX,
       "pprSH51028GPX": pprSH51028GPX,
       "pprSH51052GPX": pprSH51052GPX,
       "pprSH23010GP": pprSH23010GP,
       "pprSH23018GP": pprSH23018GP,
       "pprSH23028GP": pprSH23028GP,
       "pprSH2109GT": pprSH2109GT,
       "pprSH21016GT": pprSH21016GT,
       "pprSH21024GT": pprSH21024GT,
       "pprSH31026FT": pprSH31026FT,
       "pprSH31050FT": pprSH31050FT,
       "pprSH31026FP": pprSH31026FP,
       "pprSH31050FP": pprSH31050FP,
       "pprSH23010GT": pprSH23010GT,
       "pprSH23018GT": pprSH23018GT,
       "pprSH23028GT": pprSH23028GT,
       "pprAtFS980M9": pprAtFS980M9,
       "pprAtFS980M9PS": pprAtFS980M9PS,
       "pprAtFS980M18": pprAtFS980M18,
       "pprAtFS980M18PS": pprAtFS980M18PS,
       "pprAtFS980M28": pprAtFS980M28,
       "pprAtFS980M28PS": pprAtFS980M28PS,
       "pprAtFS980M52": pprAtFS980M52,
       "pprAtFS980M52PS": pprAtFS980M52PS,
       "pprSBx908G2": pprSBx908G2,
       "pprSBx908G3": pprSBx908G3,
       "pprAtFan08": pprAtFan08,
       "pprAtXem2QS4": pprAtXem2QS4,
       "pprAtXem2XS12": pprAtXem2XS12,
       "pprAtXem2XT12": pprAtXem2XT12,
       "pprAtXem3QS8": pprAtXem3QS8,
       "pprx55018XTQ": pprx55018XTQ,
       "pprx55018XSQ": pprx55018XSQ,
       "pprx55018XSPQm": pprx55018XSPQm,
       "pprAtXem2CQ1": pprAtXem2CQ1,
       "pprAtGS910M": pprAtGS910M,
       "pprAtGS910MP": pprAtGS910MP,
       "pprAtGS918M": pprAtGS918M,
       "pprAtGS918MP": pprAtGS918MP,
       "pprAtGS928M": pprAtGS928M,
       "pprAtGS928MP": pprAtGS928MP,
       "pprAtGS952M": pprAtGS952M,
       "pprAtGS952MP": pprAtGS952MP,
       "pprx22052GT": pprx22052GT,
       "pprx22052GP": pprx22052GP,
       "pprx22028GS": pprx22028GS,
       "pprAtGS980M52": pprAtGS980M52,
       "pprAtGS980M52PS": pprAtGS980M52PS,
       "pprx53028GTXm": pprx53028GTXm,
       "pprx53028GPXm": pprx53028GPXm,
       "pprx530DP28GHXm": pprx530DP28GHXm,
       "pprx53052GTXm": pprx53052GTXm,
       "pprx53052GPXm": pprx53052GPXm,
       "pprx530DP52GHXm": pprx530DP52GHXm,
       "pprAtGS980MX28": pprAtGS980MX28,
       "pprAtGS980MX28PSm": pprAtGS980MX28PSm,
       "pprAtGS980MX52": pprAtGS980MX52,
       "pprAtGS980MX52PSm": pprAtGS980MX52PSm,
       "pprAtGS970M28PS": pprAtGS970M28PS,
       "pprAtGS970M18PS": pprAtGS970M18PS,
       "pprAtGS970M10PS": pprAtGS970M10PS,
       "pprAtGS970M28": pprAtGS970M28,
       "pprAtGS970M18": pprAtGS970M18,
       "pprAtGS970M10": pprAtGS970M10,
       "pprAtIE34012GP": pprAtIE34012GP,
       "pprAtIE340L18GP": pprAtIE340L18GP,
       "pprAtIE34012GT": pprAtIE34012GT,
       "pprAtIE34020GP": pprAtIE34020GP,
       "pprIE21010GP": pprIE21010GP,
       "pprIE21018GP": pprIE21018GP,
       "pprAtXem2XTm12": pprAtXem2XTm12,
       "pprAtXem2XSTm8": pprAtXem2XSTm8,
       "pprx95028XTQm": pprx95028XTQm,
       "pprx95028XSQ": pprx95028XSQ,
       "pprx230L17GT": pprx230L17GT,
       "pprx230L26GT": pprx230L26GT,
       "pprx32010GH": pprx32010GH,
       "pprx32011GPT": pprx32011GPT,
       "pprAtXem2XS12V2": pprAtXem2XS12V2,
       "pprAR1050V": pprAR1050V,
       "pprAtSBx81GC40": pprAtSBx81GC40,
       "pprx55018XSQV2": pprx55018XSQV2,
       "pprx530L28GTX": pprx530L28GTX,
       "pprx530L28GPX": pprx530L28GPX,
       "pprx530L52GTX": pprx530L52GTX,
       "pprx530L52GPX": pprx530L52GPX,
       "pprAtFS980M28DP": pprAtFS980M28DP,
       "pprAtSBx81FAN12v2": pprAtSBx81FAN12v2,
       "pprx95052XTQm": pprx95052XTQm,
       "pprx95052XSQ": pprx95052XSQ,
       "pprAtGS980EM10H": pprAtGS980EM10H,
       "pprAtGS980EM11PT": pprAtGS980EM11PT,
       "pprAtSBx81GP24v2": pprAtSBx81GP24v2,
       "pprx530L10GHXm": pprx530L10GHXm,
       "pprx53010GHXm": pprx53010GHXm,
       "pprx53018GHXm": pprx53018GHXm,
       "pprAtGS980MX10HSm": pprAtGS980MX10HSm,
       "pprSBx81CFC960v2a": pprSBx81CFC960v2a,
       "pprAR4050S5G": pprAR4050S5G,
       "pprvFW": pprvFW,
       "release": release,
       "iftypes": iftypes,
       "ifaceEth": ifaceEth,
       "ifaceSyn": ifaceSyn,
       "ifaceAsyn": ifaceAsyn,
       "ifaceBri": ifaceBri,
       "ifacePri": ifacePri,
       "ifacePots": ifacePots,
       "ifaceGBIC": ifaceGBIC,
       "chips": chips,
       "chip68020Cpu": chip68020Cpu,
       "chip68340Cpu": chip68340Cpu,
       "chip68302Cpu": chip68302Cpu,
       "chip68360Cpu": chip68360Cpu,
       "chip860TCpu": chip860TCpu,
       "chipMips4kcCpu": chipMips4kcCpu,
       "chipRtc1": chipRtc1,
       "chipRtc2": chipRtc2,
       "chipRtc3": chipRtc3,
       "chipRtc4": chipRtc4,
       "chipRam1mb": chipRam1mb,
       "chipRam2mb": chipRam2mb,
       "chipRam3mb": chipRam3mb,
       "chipRam4mb": chipRam4mb,
       "chipRam6mb": chipRam6mb,
       "chipRam8mb": chipRam8mb,
       "chipRam12mb": chipRam12mb,
       "chipRam16mb": chipRam16mb,
       "chipRam20mb": chipRam20mb,
       "chipRam32mb": chipRam32mb,
       "chipFlash1mb": chipFlash1mb,
       "chipFlash2mb": chipFlash2mb,
       "chipFlash3mb": chipFlash3mb,
       "chipFlash4mb": chipFlash4mb,
       "chipFlash6mb": chipFlash6mb,
       "chipFlash8mb": chipFlash8mb,
       "chipPem": chipPem}
)
