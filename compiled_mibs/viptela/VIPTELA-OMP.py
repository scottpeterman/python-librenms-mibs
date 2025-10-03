# SNMP MIB module (VIPTELA-OMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-OMP
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:03 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_omp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5)
)
if mibBuilder.loadTexts:
    viptela_omp.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class IpPrefix(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(17, 17),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Groups1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class ReceivedPrunes(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class AttributeTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("original", 0),
          ("installed", 1))
    )



class Groups(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class AdvertisedPrunes(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Route1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Route(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class ReceivedPrunes1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class AdvertisedPrunes1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class AfTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tloc-ipv4", 0),
          ("tloc-ipv6", 1),
          ("service", 2),
          ("route-ipv4", 3),
          ("route-ipv6", 4),
          ("mcast-ipv4", 5),
          ("mcast-ipv6", 6))
    )



class BfdStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("inactive", 2))
    )



class PathStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chosen", 0),
          ("backup", 1))
    )



class RibInStatusType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("c", 0),
          ("i", 1),
          ("red", 2),
          ("rej", 3),
          ("l", 4),
          ("r", 5),
          ("s", 6),
          ("ext", 7),
          ("inv", 8),
          ("u", 9),
          ("stg", 10),
          ("ia", 11))
    )


class AddrFamilyEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )



class LossReasonEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("invalid", 1),
          ("personality", 2),
          ("distance", 3),
          ("preference", 4),
          ("tloc-preference", 5),
          ("origin-protocol", 6),
          ("origin-protocol-subtype", 7),
          ("origin-metric", 8),
          ("peer-id", 9),
          ("tloc-id", 10),
          ("stale-entry", 11),
          ("site-id", 12),
          ("omp-version", 13),
          ("tloc-gen-id", 14),
          ("tloc-spi", 15),
          ("ultimate-tloc-id", 16),
          ("tloc-action", 17))
    )



class McastRouteEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starGroup", 0),
          ("sourceGroup", 1),
          ("sourceActive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Omp_ObjectIdentity = ObjectIdentity
omp = _Omp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 1)
)
_OmpSummaryTable_ObjectIdentity = ObjectIdentity
ompSummaryTable = _OmpSummaryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2)
)
_OmpSummary_ObjectIdentity = ObjectIdentity
ompSummary = _OmpSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1)
)


class _OmpSummaryOperstate_Type(Integer32):
    """Custom type ompSummaryOperstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dOWN", 1),
          ("uP", 2))
    )


_OmpSummaryOperstate_Type.__name__ = "Integer32"
_OmpSummaryOperstate_Object = MibScalar
ompSummaryOperstate = _OmpSummaryOperstate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 1),
    _OmpSummaryOperstate_Type()
)
ompSummaryOperstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryOperstate.setStatus("current")


class _OmpSummaryAdminstate_Type(Integer32):
    """Custom type ompSummaryAdminstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dOWN", 1),
          ("uP", 2))
    )


_OmpSummaryAdminstate_Type.__name__ = "Integer32"
_OmpSummaryAdminstate_Object = MibScalar
ompSummaryAdminstate = _OmpSummaryAdminstate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 2),
    _OmpSummaryAdminstate_Type()
)
ompSummaryAdminstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryAdminstate.setStatus("current")


class _OmpSummaryDevicetype_Type(Integer32):
    """Custom type ompSummaryDevicetype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_OmpSummaryDevicetype_Type.__name__ = "Integer32"
_OmpSummaryDevicetype_Object = MibScalar
ompSummaryDevicetype = _OmpSummaryDevicetype_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 3),
    _OmpSummaryDevicetype_Type()
)
ompSummaryDevicetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryDevicetype.setStatus("current")
_OmpSummaryOmpuptime_Type = String
_OmpSummaryOmpuptime_Object = MibScalar
ompSummaryOmpuptime = _OmpSummaryOmpuptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 4),
    _OmpSummaryOmpuptime_Type()
)
ompSummaryOmpuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryOmpuptime.setStatus("current")
_OmpSummaryOmpdowntime_Type = String
_OmpSummaryOmpdowntime_Object = MibScalar
ompSummaryOmpdowntime = _OmpSummaryOmpdowntime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 5),
    _OmpSummaryOmpdowntime_Type()
)
ompSummaryOmpdowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryOmpdowntime.setStatus("current")
_OmpSummaryRoutesReceived_Type = Unsigned32
_OmpSummaryRoutesReceived_Object = MibScalar
ompSummaryRoutesReceived = _OmpSummaryRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 6),
    _OmpSummaryRoutesReceived_Type()
)
ompSummaryRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryRoutesReceived.setStatus("current")
_OmpSummaryRoutesInstalled_Type = Unsigned32
_OmpSummaryRoutesInstalled_Object = MibScalar
ompSummaryRoutesInstalled = _OmpSummaryRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 7),
    _OmpSummaryRoutesInstalled_Type()
)
ompSummaryRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryRoutesInstalled.setStatus("current")
_OmpSummaryRoutesSent_Type = Unsigned32
_OmpSummaryRoutesSent_Object = MibScalar
ompSummaryRoutesSent = _OmpSummaryRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 8),
    _OmpSummaryRoutesSent_Type()
)
ompSummaryRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryRoutesSent.setStatus("current")
_OmpSummaryTlocsReceived_Type = Unsigned32
_OmpSummaryTlocsReceived_Object = MibScalar
ompSummaryTlocsReceived = _OmpSummaryTlocsReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 9),
    _OmpSummaryTlocsReceived_Type()
)
ompSummaryTlocsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryTlocsReceived.setStatus("current")
_OmpSummaryTlocsInstalled_Type = Unsigned32
_OmpSummaryTlocsInstalled_Object = MibScalar
ompSummaryTlocsInstalled = _OmpSummaryTlocsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 10),
    _OmpSummaryTlocsInstalled_Type()
)
ompSummaryTlocsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryTlocsInstalled.setStatus("current")
_OmpSummaryTlocsSent_Type = Unsigned32
_OmpSummaryTlocsSent_Object = MibScalar
ompSummaryTlocsSent = _OmpSummaryTlocsSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 11),
    _OmpSummaryTlocsSent_Type()
)
ompSummaryTlocsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryTlocsSent.setStatus("current")
_OmpSummaryServicesReceived_Type = Unsigned32
_OmpSummaryServicesReceived_Object = MibScalar
ompSummaryServicesReceived = _OmpSummaryServicesReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 12),
    _OmpSummaryServicesReceived_Type()
)
ompSummaryServicesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryServicesReceived.setStatus("current")
_OmpSummaryServicesInstalled_Type = Unsigned32
_OmpSummaryServicesInstalled_Object = MibScalar
ompSummaryServicesInstalled = _OmpSummaryServicesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 13),
    _OmpSummaryServicesInstalled_Type()
)
ompSummaryServicesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryServicesInstalled.setStatus("current")
_OmpSummaryServicesSent_Type = Unsigned32
_OmpSummaryServicesSent_Object = MibScalar
ompSummaryServicesSent = _OmpSummaryServicesSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 14),
    _OmpSummaryServicesSent_Type()
)
ompSummaryServicesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryServicesSent.setStatus("current")
_OmpSummaryMcastRoutesReceived_Type = Unsigned32
_OmpSummaryMcastRoutesReceived_Object = MibScalar
ompSummaryMcastRoutesReceived = _OmpSummaryMcastRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 15),
    _OmpSummaryMcastRoutesReceived_Type()
)
ompSummaryMcastRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMcastRoutesReceived.setStatus("current")
_OmpSummaryMcastRoutesInstalled_Type = Unsigned32
_OmpSummaryMcastRoutesInstalled_Object = MibScalar
ompSummaryMcastRoutesInstalled = _OmpSummaryMcastRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 16),
    _OmpSummaryMcastRoutesInstalled_Type()
)
ompSummaryMcastRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMcastRoutesInstalled.setStatus("current")
_OmpSummaryMcastRoutesSent_Type = Unsigned32
_OmpSummaryMcastRoutesSent_Object = MibScalar
ompSummaryMcastRoutesSent = _OmpSummaryMcastRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 17),
    _OmpSummaryMcastRoutesSent_Type()
)
ompSummaryMcastRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryMcastRoutesSent.setStatus("current")
_OmpSummaryHelloReceived_Type = Unsigned32
_OmpSummaryHelloReceived_Object = MibScalar
ompSummaryHelloReceived = _OmpSummaryHelloReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 18),
    _OmpSummaryHelloReceived_Type()
)
ompSummaryHelloReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHelloReceived.setStatus("current")
_OmpSummaryHelloSent_Type = Unsigned32
_OmpSummaryHelloSent_Object = MibScalar
ompSummaryHelloSent = _OmpSummaryHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 19),
    _OmpSummaryHelloSent_Type()
)
ompSummaryHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHelloSent.setStatus("current")
_OmpSummaryHandshakeReceived_Type = Unsigned32
_OmpSummaryHandshakeReceived_Object = MibScalar
ompSummaryHandshakeReceived = _OmpSummaryHandshakeReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 20),
    _OmpSummaryHandshakeReceived_Type()
)
ompSummaryHandshakeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHandshakeReceived.setStatus("current")
_OmpSummaryHandshakeSent_Type = Unsigned32
_OmpSummaryHandshakeSent_Object = MibScalar
ompSummaryHandshakeSent = _OmpSummaryHandshakeSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 21),
    _OmpSummaryHandshakeSent_Type()
)
ompSummaryHandshakeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryHandshakeSent.setStatus("current")
_OmpSummaryAlertReceived_Type = Unsigned32
_OmpSummaryAlertReceived_Object = MibScalar
ompSummaryAlertReceived = _OmpSummaryAlertReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 22),
    _OmpSummaryAlertReceived_Type()
)
ompSummaryAlertReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryAlertReceived.setStatus("current")
_OmpSummaryAlertSent_Type = Unsigned32
_OmpSummaryAlertSent_Object = MibScalar
ompSummaryAlertSent = _OmpSummaryAlertSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 23),
    _OmpSummaryAlertSent_Type()
)
ompSummaryAlertSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryAlertSent.setStatus("current")
_OmpSummaryInformReceived_Type = Unsigned32
_OmpSummaryInformReceived_Object = MibScalar
ompSummaryInformReceived = _OmpSummaryInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 24),
    _OmpSummaryInformReceived_Type()
)
ompSummaryInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryInformReceived.setStatus("current")
_OmpSummaryInformSent_Type = Unsigned32
_OmpSummaryInformSent_Object = MibScalar
ompSummaryInformSent = _OmpSummaryInformSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 25),
    _OmpSummaryInformSent_Type()
)
ompSummaryInformSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryInformSent.setStatus("current")
_OmpSummaryUpdateReceived_Type = Unsigned32
_OmpSummaryUpdateReceived_Object = MibScalar
ompSummaryUpdateReceived = _OmpSummaryUpdateReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 26),
    _OmpSummaryUpdateReceived_Type()
)
ompSummaryUpdateReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryUpdateReceived.setStatus("current")
_OmpSummaryUpdateSent_Type = Unsigned32
_OmpSummaryUpdateSent_Object = MibScalar
ompSummaryUpdateSent = _OmpSummaryUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 27),
    _OmpSummaryUpdateSent_Type()
)
ompSummaryUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryUpdateSent.setStatus("current")
_OmpSummaryPolicyReceived_Type = Unsigned32
_OmpSummaryPolicyReceived_Object = MibScalar
ompSummaryPolicyReceived = _OmpSummaryPolicyReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 28),
    _OmpSummaryPolicyReceived_Type()
)
ompSummaryPolicyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPolicyReceived.setStatus("current")
_OmpSummaryPolicySent_Type = Unsigned32
_OmpSummaryPolicySent_Object = MibScalar
ompSummaryPolicySent = _OmpSummaryPolicySent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 29),
    _OmpSummaryPolicySent_Type()
)
ompSummaryPolicySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPolicySent.setStatus("current")
_OmpSummaryPacketsReceived_Type = Unsigned32
_OmpSummaryPacketsReceived_Object = MibScalar
ompSummaryPacketsReceived = _OmpSummaryPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 30),
    _OmpSummaryPacketsReceived_Type()
)
ompSummaryPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPacketsReceived.setStatus("current")
_OmpSummaryPacketsSent_Type = Unsigned32
_OmpSummaryPacketsSent_Object = MibScalar
ompSummaryPacketsSent = _OmpSummaryPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 31),
    _OmpSummaryPacketsSent_Type()
)
ompSummaryPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPacketsSent.setStatus("current")
_OmpSummaryVsmartPeers_Type = Unsigned32
_OmpSummaryVsmartPeers_Object = MibScalar
ompSummaryVsmartPeers = _OmpSummaryVsmartPeers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 32),
    _OmpSummaryVsmartPeers_Type()
)
ompSummaryVsmartPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryVsmartPeers.setStatus("current")
_OmpSummaryVedgePeers_Type = Unsigned32
_OmpSummaryVedgePeers_Object = MibScalar
ompSummaryVedgePeers = _OmpSummaryVedgePeers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 33),
    _OmpSummaryVedgePeers_Type()
)
ompSummaryVedgePeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryVedgePeers.setStatus("current")
_OmpSummaryPolicyQueue_Type = String
_OmpSummaryPolicyQueue_Object = MibScalar
ompSummaryPolicyQueue = _OmpSummaryPolicyQueue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 1, 34),
    _OmpSummaryPolicyQueue_Type()
)
ompSummaryPolicyQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPolicyQueue.setStatus("current")
_OmpSummaryPeersTable_Object = MibTable
ompSummaryPeersTable = _OmpSummaryPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2)
)
if mibBuilder.loadTexts:
    ompSummaryPeersTable.setStatus("current")
_OmpSummaryPeersEntry_Object = MibTableRow
ompSummaryPeersEntry = _OmpSummaryPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1)
)
ompSummaryPeersEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompSummaryPeersPeer"),
)
if mibBuilder.loadTexts:
    ompSummaryPeersEntry.setStatus("current")
_OmpSummaryPeersPeer_Type = InetAddressIP
_OmpSummaryPeersPeer_Object = MibTableColumn
ompSummaryPeersPeer = _OmpSummaryPeersPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 1),
    _OmpSummaryPeersPeer_Type()
)
ompSummaryPeersPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompSummaryPeersPeer.setStatus("current")


class _OmpSummaryPeersType_Type(Integer32):
    """Custom type ompSummaryPeersType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_OmpSummaryPeersType_Type.__name__ = "Integer32"
_OmpSummaryPeersType_Object = MibTableColumn
ompSummaryPeersType = _OmpSummaryPeersType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 2),
    _OmpSummaryPeersType_Type()
)
ompSummaryPeersType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersType.setStatus("current")


class _OmpSummaryPeersDomainId_Type(Unsigned32):
    """Custom type ompSummaryPeersDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpSummaryPeersDomainId_Type.__name__ = "Unsigned32"
_OmpSummaryPeersDomainId_Object = MibTableColumn
ompSummaryPeersDomainId = _OmpSummaryPeersDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 3),
    _OmpSummaryPeersDomainId_Type()
)
ompSummaryPeersDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersDomainId.setStatus("current")
_OmpSummaryPeersSiteId_Type = Unsigned32
_OmpSummaryPeersSiteId_Object = MibTableColumn
ompSummaryPeersSiteId = _OmpSummaryPeersSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 4),
    _OmpSummaryPeersSiteId_Type()
)
ompSummaryPeersSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersSiteId.setStatus("current")


class _OmpSummaryPeersState_Type(Integer32):
    """Custom type ompSummaryPeersState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("init", 1),
          ("handshake", 2),
          ("up", 3),
          ("down", 4),
          ("init-in-gr", 5),
          ("down-in-gr", 6),
          ("handshake-in-gr", 7))
    )


_OmpSummaryPeersState_Type.__name__ = "Integer32"
_OmpSummaryPeersState_Object = MibTableColumn
ompSummaryPeersState = _OmpSummaryPeersState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 5),
    _OmpSummaryPeersState_Type()
)
ompSummaryPeersState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersState.setStatus("current")
_OmpSummaryPeersVersion_Type = UnsignedByte
_OmpSummaryPeersVersion_Object = MibTableColumn
ompSummaryPeersVersion = _OmpSummaryPeersVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 6),
    _OmpSummaryPeersVersion_Type()
)
ompSummaryPeersVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersVersion.setStatus("current")


class _OmpSummaryPeersLegit_Type(Integer32):
    """Custom type ompSummaryPeersLegit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OmpSummaryPeersLegit_Type.__name__ = "Integer32"
_OmpSummaryPeersLegit_Object = MibTableColumn
ompSummaryPeersLegit = _OmpSummaryPeersLegit_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 7),
    _OmpSummaryPeersLegit_Type()
)
ompSummaryPeersLegit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersLegit.setStatus("current")
_OmpSummaryPeersUpcount_Type = Unsigned32
_OmpSummaryPeersUpcount_Object = MibTableColumn
ompSummaryPeersUpcount = _OmpSummaryPeersUpcount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 8),
    _OmpSummaryPeersUpcount_Type()
)
ompSummaryPeersUpcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersUpcount.setStatus("current")
_OmpSummaryPeersDowncount_Type = Unsigned32
_OmpSummaryPeersDowncount_Object = MibTableColumn
ompSummaryPeersDowncount = _OmpSummaryPeersDowncount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 9),
    _OmpSummaryPeersDowncount_Type()
)
ompSummaryPeersDowncount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersDowncount.setStatus("current")
_OmpSummaryPeersLastuptime_Type = DateAndTime
_OmpSummaryPeersLastuptime_Object = MibTableColumn
ompSummaryPeersLastuptime = _OmpSummaryPeersLastuptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 10),
    _OmpSummaryPeersLastuptime_Type()
)
ompSummaryPeersLastuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersLastuptime.setStatus("current")
_OmpSummaryPeersLastdowntime_Type = DateAndTime
_OmpSummaryPeersLastdowntime_Object = MibTableColumn
ompSummaryPeersLastdowntime = _OmpSummaryPeersLastdowntime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 11),
    _OmpSummaryPeersLastdowntime_Type()
)
ompSummaryPeersLastdowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersLastdowntime.setStatus("current")
_OmpSummaryPeersUpTime_Type = String
_OmpSummaryPeersUpTime_Object = MibTableColumn
ompSummaryPeersUpTime = _OmpSummaryPeersUpTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 12),
    _OmpSummaryPeersUpTime_Type()
)
ompSummaryPeersUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersUpTime.setStatus("current")
_OmpSummaryPeersDownTime_Type = String
_OmpSummaryPeersDownTime_Object = MibTableColumn
ompSummaryPeersDownTime = _OmpSummaryPeersDownTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 13),
    _OmpSummaryPeersDownTime_Type()
)
ompSummaryPeersDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersDownTime.setStatus("current")
_OmpSummaryPeersHoldtime_Type = Unsigned32
_OmpSummaryPeersHoldtime_Object = MibTableColumn
ompSummaryPeersHoldtime = _OmpSummaryPeersHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 14),
    _OmpSummaryPeersHoldtime_Type()
)
ompSummaryPeersHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersHoldtime.setStatus("current")
_OmpSummaryPeersSitepolicy_Type = String
_OmpSummaryPeersSitepolicy_Object = MibTableColumn
ompSummaryPeersSitepolicy = _OmpSummaryPeersSitepolicy_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 15),
    _OmpSummaryPeersSitepolicy_Type()
)
ompSummaryPeersSitepolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersSitepolicy.setStatus("current")
_OmpSummaryPeersPolicyin_Type = String
_OmpSummaryPeersPolicyin_Object = MibTableColumn
ompSummaryPeersPolicyin = _OmpSummaryPeersPolicyin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 16),
    _OmpSummaryPeersPolicyin_Type()
)
ompSummaryPeersPolicyin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersPolicyin.setStatus("current")
_OmpSummaryPeersPolicyout_Type = String
_OmpSummaryPeersPolicyout_Object = MibTableColumn
ompSummaryPeersPolicyout = _OmpSummaryPeersPolicyout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 17),
    _OmpSummaryPeersPolicyout_Type()
)
ompSummaryPeersPolicyout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersPolicyout.setStatus("current")


class _OmpSummaryPeersGracefulRestart_Type(Integer32):
    """Custom type ompSummaryPeersGracefulRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 0),
          ("not-supported", 1),
          ("in-progress", 2))
    )


_OmpSummaryPeersGracefulRestart_Type.__name__ = "Integer32"
_OmpSummaryPeersGracefulRestart_Object = MibTableColumn
ompSummaryPeersGracefulRestart = _OmpSummaryPeersGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 18),
    _OmpSummaryPeersGracefulRestart_Type()
)
ompSummaryPeersGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersGracefulRestart.setStatus("current")
_OmpSummaryPeersGracefulRestartInterval_Type = Unsigned32
_OmpSummaryPeersGracefulRestartInterval_Object = MibTableColumn
ompSummaryPeersGracefulRestartInterval = _OmpSummaryPeersGracefulRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 19),
    _OmpSummaryPeersGracefulRestartInterval_Type()
)
ompSummaryPeersGracefulRestartInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersGracefulRestartInterval.setStatus("current")
_OmpSummaryPeersHelloReceived_Type = Unsigned32
_OmpSummaryPeersHelloReceived_Object = MibTableColumn
ompSummaryPeersHelloReceived = _OmpSummaryPeersHelloReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 20),
    _OmpSummaryPeersHelloReceived_Type()
)
ompSummaryPeersHelloReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersHelloReceived.setStatus("current")
_OmpSummaryPeersHelloSent_Type = Unsigned32
_OmpSummaryPeersHelloSent_Object = MibTableColumn
ompSummaryPeersHelloSent = _OmpSummaryPeersHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 21),
    _OmpSummaryPeersHelloSent_Type()
)
ompSummaryPeersHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersHelloSent.setStatus("current")
_OmpSummaryPeersHandshakeReceived_Type = Unsigned32
_OmpSummaryPeersHandshakeReceived_Object = MibTableColumn
ompSummaryPeersHandshakeReceived = _OmpSummaryPeersHandshakeReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 22),
    _OmpSummaryPeersHandshakeReceived_Type()
)
ompSummaryPeersHandshakeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersHandshakeReceived.setStatus("current")
_OmpSummaryPeersHandshakeSent_Type = Unsigned32
_OmpSummaryPeersHandshakeSent_Object = MibTableColumn
ompSummaryPeersHandshakeSent = _OmpSummaryPeersHandshakeSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 23),
    _OmpSummaryPeersHandshakeSent_Type()
)
ompSummaryPeersHandshakeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersHandshakeSent.setStatus("current")
_OmpSummaryPeersAlertReceived_Type = Unsigned32
_OmpSummaryPeersAlertReceived_Object = MibTableColumn
ompSummaryPeersAlertReceived = _OmpSummaryPeersAlertReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 24),
    _OmpSummaryPeersAlertReceived_Type()
)
ompSummaryPeersAlertReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersAlertReceived.setStatus("current")
_OmpSummaryPeersAlertSent_Type = Unsigned32
_OmpSummaryPeersAlertSent_Object = MibTableColumn
ompSummaryPeersAlertSent = _OmpSummaryPeersAlertSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 25),
    _OmpSummaryPeersAlertSent_Type()
)
ompSummaryPeersAlertSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersAlertSent.setStatus("current")
_OmpSummaryPeersInformReceived_Type = Unsigned32
_OmpSummaryPeersInformReceived_Object = MibTableColumn
ompSummaryPeersInformReceived = _OmpSummaryPeersInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 26),
    _OmpSummaryPeersInformReceived_Type()
)
ompSummaryPeersInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersInformReceived.setStatus("current")
_OmpSummaryPeersInformSent_Type = Unsigned32
_OmpSummaryPeersInformSent_Object = MibTableColumn
ompSummaryPeersInformSent = _OmpSummaryPeersInformSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 27),
    _OmpSummaryPeersInformSent_Type()
)
ompSummaryPeersInformSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersInformSent.setStatus("current")
_OmpSummaryPeersUpdateReceived_Type = Unsigned32
_OmpSummaryPeersUpdateReceived_Object = MibTableColumn
ompSummaryPeersUpdateReceived = _OmpSummaryPeersUpdateReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 28),
    _OmpSummaryPeersUpdateReceived_Type()
)
ompSummaryPeersUpdateReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersUpdateReceived.setStatus("current")
_OmpSummaryPeersUpdateSent_Type = Unsigned32
_OmpSummaryPeersUpdateSent_Object = MibTableColumn
ompSummaryPeersUpdateSent = _OmpSummaryPeersUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 29),
    _OmpSummaryPeersUpdateSent_Type()
)
ompSummaryPeersUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersUpdateSent.setStatus("current")
_OmpSummaryPeersPolicyReceived_Type = Unsigned32
_OmpSummaryPeersPolicyReceived_Object = MibTableColumn
ompSummaryPeersPolicyReceived = _OmpSummaryPeersPolicyReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 30),
    _OmpSummaryPeersPolicyReceived_Type()
)
ompSummaryPeersPolicyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersPolicyReceived.setStatus("current")
_OmpSummaryPeersPolicySent_Type = Unsigned32
_OmpSummaryPeersPolicySent_Object = MibTableColumn
ompSummaryPeersPolicySent = _OmpSummaryPeersPolicySent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 31),
    _OmpSummaryPeersPolicySent_Type()
)
ompSummaryPeersPolicySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersPolicySent.setStatus("current")
_OmpSummaryPeersPacketsReceived_Type = Unsigned32
_OmpSummaryPeersPacketsReceived_Object = MibTableColumn
ompSummaryPeersPacketsReceived = _OmpSummaryPeersPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 32),
    _OmpSummaryPeersPacketsReceived_Type()
)
ompSummaryPeersPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersPacketsReceived.setStatus("current")
_OmpSummaryPeersPacketsSent_Type = Unsigned32
_OmpSummaryPeersPacketsSent_Object = MibTableColumn
ompSummaryPeersPacketsSent = _OmpSummaryPeersPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 33),
    _OmpSummaryPeersPacketsSent_Type()
)
ompSummaryPeersPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersPacketsSent.setStatus("current")
_OmpSummaryPeersRoutesReceived_Type = Unsigned32
_OmpSummaryPeersRoutesReceived_Object = MibTableColumn
ompSummaryPeersRoutesReceived = _OmpSummaryPeersRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 34),
    _OmpSummaryPeersRoutesReceived_Type()
)
ompSummaryPeersRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesReceived.setStatus("current")
_OmpSummaryPeersRoutesInstalled_Type = Unsigned32
_OmpSummaryPeersRoutesInstalled_Object = MibTableColumn
ompSummaryPeersRoutesInstalled = _OmpSummaryPeersRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 35),
    _OmpSummaryPeersRoutesInstalled_Type()
)
ompSummaryPeersRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesInstalled.setStatus("current")
_OmpSummaryPeersRoutesSent_Type = Unsigned32
_OmpSummaryPeersRoutesSent_Object = MibTableColumn
ompSummaryPeersRoutesSent = _OmpSummaryPeersRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 36),
    _OmpSummaryPeersRoutesSent_Type()
)
ompSummaryPeersRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesSent.setStatus("current")
_OmpSummaryPeersTlocsReceived_Type = Unsigned32
_OmpSummaryPeersTlocsReceived_Object = MibTableColumn
ompSummaryPeersTlocsReceived = _OmpSummaryPeersTlocsReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 37),
    _OmpSummaryPeersTlocsReceived_Type()
)
ompSummaryPeersTlocsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersTlocsReceived.setStatus("current")
_OmpSummaryPeersTlocsInstalled_Type = Unsigned32
_OmpSummaryPeersTlocsInstalled_Object = MibTableColumn
ompSummaryPeersTlocsInstalled = _OmpSummaryPeersTlocsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 38),
    _OmpSummaryPeersTlocsInstalled_Type()
)
ompSummaryPeersTlocsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersTlocsInstalled.setStatus("current")
_OmpSummaryPeersTlocsSent_Type = Unsigned32
_OmpSummaryPeersTlocsSent_Object = MibTableColumn
ompSummaryPeersTlocsSent = _OmpSummaryPeersTlocsSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 39),
    _OmpSummaryPeersTlocsSent_Type()
)
ompSummaryPeersTlocsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersTlocsSent.setStatus("current")
_OmpSummaryPeersServicesReceived_Type = Unsigned32
_OmpSummaryPeersServicesReceived_Object = MibTableColumn
ompSummaryPeersServicesReceived = _OmpSummaryPeersServicesReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 40),
    _OmpSummaryPeersServicesReceived_Type()
)
ompSummaryPeersServicesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersServicesReceived.setStatus("current")
_OmpSummaryPeersServicesInstalled_Type = Unsigned32
_OmpSummaryPeersServicesInstalled_Object = MibTableColumn
ompSummaryPeersServicesInstalled = _OmpSummaryPeersServicesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 41),
    _OmpSummaryPeersServicesInstalled_Type()
)
ompSummaryPeersServicesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersServicesInstalled.setStatus("current")
_OmpSummaryPeersServicesSent_Type = Unsigned32
_OmpSummaryPeersServicesSent_Object = MibTableColumn
ompSummaryPeersServicesSent = _OmpSummaryPeersServicesSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 42),
    _OmpSummaryPeersServicesSent_Type()
)
ompSummaryPeersServicesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersServicesSent.setStatus("current")
_OmpSummaryPeersMcastRoutesReceived_Type = Unsigned32
_OmpSummaryPeersMcastRoutesReceived_Object = MibTableColumn
ompSummaryPeersMcastRoutesReceived = _OmpSummaryPeersMcastRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 43),
    _OmpSummaryPeersMcastRoutesReceived_Type()
)
ompSummaryPeersMcastRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersMcastRoutesReceived.setStatus("current")
_OmpSummaryPeersMcastRoutesInstalled_Type = Unsigned32
_OmpSummaryPeersMcastRoutesInstalled_Object = MibTableColumn
ompSummaryPeersMcastRoutesInstalled = _OmpSummaryPeersMcastRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 44),
    _OmpSummaryPeersMcastRoutesInstalled_Type()
)
ompSummaryPeersMcastRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersMcastRoutesInstalled.setStatus("current")
_OmpSummaryPeersMcastRoutesSent_Type = Unsigned32
_OmpSummaryPeersMcastRoutesSent_Object = MibTableColumn
ompSummaryPeersMcastRoutesSent = _OmpSummaryPeersMcastRoutesSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 45),
    _OmpSummaryPeersMcastRoutesSent_Type()
)
ompSummaryPeersMcastRoutesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersMcastRoutesSent.setStatus("current")


class _OmpSummaryPeersControlUp_Type(Integer32):
    """Custom type ompSummaryPeersControlUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OmpSummaryPeersControlUp_Type.__name__ = "Integer32"
_OmpSummaryPeersControlUp_Object = MibTableColumn
ompSummaryPeersControlUp = _OmpSummaryPeersControlUp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 46),
    _OmpSummaryPeersControlUp_Type()
)
ompSummaryPeersControlUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersControlUp.setStatus("current")


class _OmpSummaryPeersStaging_Type(Integer32):
    """Custom type ompSummaryPeersStaging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OmpSummaryPeersStaging_Type.__name__ = "Integer32"
_OmpSummaryPeersStaging_Object = MibTableColumn
ompSummaryPeersStaging = _OmpSummaryPeersStaging_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 47),
    _OmpSummaryPeersStaging_Type()
)
ompSummaryPeersStaging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersStaging.setStatus("current")


class _OmpSummaryPeersRefresh_Type(Integer32):
    """Custom type ompSummaryPeersRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("supported", 0),
          ("not-supported", 1))
    )


_OmpSummaryPeersRefresh_Type.__name__ = "Integer32"
_OmpSummaryPeersRefresh_Object = MibTableColumn
ompSummaryPeersRefresh = _OmpSummaryPeersRefresh_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 48),
    _OmpSummaryPeersRefresh_Type()
)
ompSummaryPeersRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRefresh.setStatus("current")
_OmpSummaryPeersOverlayId_Type = Unsigned32
_OmpSummaryPeersOverlayId_Object = MibTableColumn
ompSummaryPeersOverlayId = _OmpSummaryPeersOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 49),
    _OmpSummaryPeersOverlayId_Type()
)
ompSummaryPeersOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersOverlayId.setStatus("current")
_OmpSummaryPeersRoutesReceivedIPv6_Type = Unsigned32
_OmpSummaryPeersRoutesReceivedIPv6_Object = MibTableColumn
ompSummaryPeersRoutesReceivedIPv6 = _OmpSummaryPeersRoutesReceivedIPv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 50),
    _OmpSummaryPeersRoutesReceivedIPv6_Type()
)
ompSummaryPeersRoutesReceivedIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesReceivedIPv6.setStatus("current")
_OmpSummaryPeersRoutesInstalledIPv6_Type = Unsigned32
_OmpSummaryPeersRoutesInstalledIPv6_Object = MibTableColumn
ompSummaryPeersRoutesInstalledIPv6 = _OmpSummaryPeersRoutesInstalledIPv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 51),
    _OmpSummaryPeersRoutesInstalledIPv6_Type()
)
ompSummaryPeersRoutesInstalledIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesInstalledIPv6.setStatus("current")
_OmpSummaryPeersRoutesSentIPv6_Type = Unsigned32
_OmpSummaryPeersRoutesSentIPv6_Object = MibTableColumn
ompSummaryPeersRoutesSentIPv6 = _OmpSummaryPeersRoutesSentIPv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 52),
    _OmpSummaryPeersRoutesSentIPv6_Type()
)
ompSummaryPeersRoutesSentIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesSentIPv6.setStatus("current")
_OmpSummaryPeersRoutesReceivedTotal_Type = Unsigned32
_OmpSummaryPeersRoutesReceivedTotal_Object = MibTableColumn
ompSummaryPeersRoutesReceivedTotal = _OmpSummaryPeersRoutesReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 53),
    _OmpSummaryPeersRoutesReceivedTotal_Type()
)
ompSummaryPeersRoutesReceivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesReceivedTotal.setStatus("current")
_OmpSummaryPeersRoutesInstalledTotal_Type = Unsigned32
_OmpSummaryPeersRoutesInstalledTotal_Object = MibTableColumn
ompSummaryPeersRoutesInstalledTotal = _OmpSummaryPeersRoutesInstalledTotal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 54),
    _OmpSummaryPeersRoutesInstalledTotal_Type()
)
ompSummaryPeersRoutesInstalledTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesInstalledTotal.setStatus("current")
_OmpSummaryPeersRoutesSentTotal_Type = Unsigned32
_OmpSummaryPeersRoutesSentTotal_Object = MibTableColumn
ompSummaryPeersRoutesSentTotal = _OmpSummaryPeersRoutesSentTotal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 55),
    _OmpSummaryPeersRoutesSentTotal_Type()
)
ompSummaryPeersRoutesSentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersRoutesSentTotal.setStatus("current")
_OmpSummaryPeersServicesReceivedIPv6_Type = Unsigned32
_OmpSummaryPeersServicesReceivedIPv6_Object = MibTableColumn
ompSummaryPeersServicesReceivedIPv6 = _OmpSummaryPeersServicesReceivedIPv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 56),
    _OmpSummaryPeersServicesReceivedIPv6_Type()
)
ompSummaryPeersServicesReceivedIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersServicesReceivedIPv6.setStatus("current")
_OmpSummaryPeersServicesInstalledIPv6_Type = Unsigned32
_OmpSummaryPeersServicesInstalledIPv6_Object = MibTableColumn
ompSummaryPeersServicesInstalledIPv6 = _OmpSummaryPeersServicesInstalledIPv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 57),
    _OmpSummaryPeersServicesInstalledIPv6_Type()
)
ompSummaryPeersServicesInstalledIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersServicesInstalledIPv6.setStatus("current")
_OmpSummaryPeersServicesSentIPv6_Type = Unsigned32
_OmpSummaryPeersServicesSentIPv6_Object = MibTableColumn
ompSummaryPeersServicesSentIPv6 = _OmpSummaryPeersServicesSentIPv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 2, 2, 1, 58),
    _OmpSummaryPeersServicesSentIPv6_Type()
)
ompSummaryPeersServicesSentIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompSummaryPeersServicesSentIPv6.setStatus("current")
_OmpRoutesTable_ObjectIdentity = ObjectIdentity
ompRoutesTable = _OmpRoutesTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3)
)
_OmpRoutesTableFamilyTable_Object = MibTable
ompRoutesTableFamilyTable = _OmpRoutesTableFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 1)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyTable.setStatus("current")
_OmpRoutesTableFamilyEntry_Object = MibTableRow
ompRoutesTableFamilyEntry = _OmpRoutesTableFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 1, 1)
)
ompRoutesTableFamilyEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntry.setStatus("current")
_OmpRoutesTableFamilyAddressFamily_Type = AddrFamilyEnum
_OmpRoutesTableFamilyAddressFamily_Object = MibTableColumn
ompRoutesTableFamilyAddressFamily = _OmpRoutesTableFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 1, 1, 1),
    _OmpRoutesTableFamilyAddressFamily_Type()
)
ompRoutesTableFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyAddressFamily.setStatus("current")
_OmpRoutesTableFamilyEntriesTable_Object = MibTable
ompRoutesTableFamilyEntriesTable = _OmpRoutesTableFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesTable.setStatus("current")
_OmpRoutesTableFamilyEntriesEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesEntry = _OmpRoutesTableFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 2, 1)
)
ompRoutesTableFamilyEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesPrefix"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesEntry.setStatus("current")


class _OmpRoutesTableFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompRoutesTableFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpRoutesTableFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpRoutesTableFamilyEntriesVpnId_Object = MibTableColumn
ompRoutesTableFamilyEntriesVpnId = _OmpRoutesTableFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 2, 1, 1),
    _OmpRoutesTableFamilyEntriesVpnId_Type()
)
ompRoutesTableFamilyEntriesVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesVpnId.setStatus("current")
_OmpRoutesTableFamilyEntriesPrefix_Type = IpPrefix
_OmpRoutesTableFamilyEntriesPrefix_Object = MibTableColumn
ompRoutesTableFamilyEntriesPrefix = _OmpRoutesTableFamilyEntriesPrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 2, 1, 2),
    _OmpRoutesTableFamilyEntriesPrefix_Type()
)
ompRoutesTableFamilyEntriesPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesPrefix.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedTable_Object = MibTable
ompRoutesTableFamilyEntriesReceivedTable = _OmpRoutesTableFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedTable.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesReceivedEntry = _OmpRoutesTableFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1)
)
ompRoutesTableFamilyEntriesReceivedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesReceivedFromPeer"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesReceivedPathId"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedFromPeer = _OmpRoutesTableFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1, 1),
    _OmpRoutesTableFamilyEntriesReceivedFromPeer_Type()
)
ompRoutesTableFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedPathId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedPathId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedPathId = _OmpRoutesTableFamilyEntriesReceivedPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1, 2),
    _OmpRoutesTableFamilyEntriesReceivedPathId_Type()
)
ompRoutesTableFamilyEntriesReceivedPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedPathId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLabel_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedLabel_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLabel = _OmpRoutesTableFamilyEntriesReceivedLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1, 3),
    _OmpRoutesTableFamilyEntriesReceivedLabel_Type()
)
ompRoutesTableFamilyEntriesReceivedLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLabel.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpRoutesTableFamilyEntriesReceivedStatus_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedStatus = _OmpRoutesTableFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1, 4),
    _OmpRoutesTableFamilyEntriesReceivedStatus_Type()
)
ompRoutesTableFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedStatus.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpRoutesTableFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLossReason = _OmpRoutesTableFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1, 5),
    _OmpRoutesTableFamilyEntriesReceivedLossReason_Type()
)
ompRoutesTableFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLossReason.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLostToPeer_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedLostToPeer_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLostToPeer = _OmpRoutesTableFamilyEntriesReceivedLostToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1, 6),
    _OmpRoutesTableFamilyEntriesReceivedLostToPeer_Type()
)
ompRoutesTableFamilyEntriesReceivedLostToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLostToPeer.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedLostToPathId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedLostToPathId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedLostToPathId = _OmpRoutesTableFamilyEntriesReceivedLostToPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 3, 1, 7),
    _OmpRoutesTableFamilyEntriesReceivedLostToPathId_Type()
)
ompRoutesTableFamilyEntriesReceivedLostToPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedLostToPathId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTable_Object = MibTable
ompRoutesTableFamilyEntriesReceivedAttributesTable = _OmpRoutesTableFamilyEntriesReceivedAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTable.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesReceivedAttributesEntry = _OmpRoutesTableFamilyEntriesReceivedAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1)
)
ompRoutesTableFamilyEntriesReceivedAttributesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesReceivedFromPeer"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesReceivedPathId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesReceivedAttributesAttributeType"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Type = AttributeTypeEnum
_OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesAttributeType = _OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 1),
    _OmpRoutesTableFamilyEntriesReceivedAttributesAttributeType_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesAttributeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesAttributeType.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTlocIp = _OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 2),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTlocIp_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTlocIp.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTlocColor = _OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 3),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTlocColor_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTlocColor.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gre", 1),
          ("ipsec", 2))
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap = _OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 4),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTlocEncap_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("proto-invalid", 0),
          ("static", 1),
          ("connected", 2),
          ("eBGP", 3),
          ("iBGP", 4),
          ("oSPF-intra-area", 5),
          ("oSPF-inter-area", 6),
          ("oSPF-external-1", 7),
          ("oSPF-external-2", 8),
          ("aggregate", 9),
          ("natpoolInside", 10),
          ("eigrp-sum", 11),
          ("eigrp-int", 12),
          ("eigrp-ext", 13),
          ("lisp", 14),
          ("isis", 15))
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol = _OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 5),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOriginProtocol_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric = _OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 6),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOriginMetric_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Type(Unsigned32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesDomainId = _OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 7),
    _OmpRoutesTableFamilyEntriesReceivedAttributesDomainId_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesDomainId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesSiteId = _OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 8),
    _OmpRoutesTableFamilyEntriesReceivedAttributesSiteId_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesSiteId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesPreference = _OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 9),
    _OmpRoutesTableFamilyEntriesReceivedAttributesPreference_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesPreference.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesTag_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesTag_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesTag = _OmpRoutesTableFamilyEntriesReceivedAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 10),
    _OmpRoutesTableFamilyEntriesReceivedAttributesTag_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesTag.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Type = UnsignedShort
_OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen = _OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 11),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Type = IpAddress
_OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOriginator = _OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 12),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOriginator_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOriginator.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 13),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 14),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gre", 1),
          ("ipsec", 2))
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 15),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap.setStatus("current")


class _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("strict", 1),
          ("primary", 2),
          ("ecmp", 3),
          ("backup", 4))
    )


_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction = _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 16),
    _OmpRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesOverlayId = _OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 17),
    _OmpRoutesTableFamilyEntriesReceivedAttributesOverlayId_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesOverlayId.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Type = String
_OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesAsPath = _OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 18),
    _OmpRoutesTableFamilyEntriesReceivedAttributesAsPath_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesAsPath.setStatus("current")
_OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Type = String
_OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Object = MibTableColumn
ompRoutesTableFamilyEntriesReceivedAttributesCommunity = _OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 4, 1, 19),
    _OmpRoutesTableFamilyEntriesReceivedAttributesCommunity_Type()
)
ompRoutesTableFamilyEntriesReceivedAttributesCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesReceivedAttributesCommunity.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedTable_Object = MibTable
ompRoutesTableFamilyEntriesAdvertisedTable = _OmpRoutesTableFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 5)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedTable.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesAdvertisedEntry = _OmpRoutesTableFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 5, 1)
)
ompRoutesTableFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedToPeer = _OmpRoutesTableFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 5, 1, 1),
    _OmpRoutesTableFamilyEntriesAdvertisedToPeer_Type()
)
ompRoutesTableFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsTable_Object = MibTable
ompRoutesTableFamilyEntriesAdvertisedPathsTable = _OmpRoutesTableFamilyEntriesAdvertisedPathsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 6)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsTable.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesAdvertisedPathsEntry = _OmpRoutesTableFamilyEntriesAdvertisedPathsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 6, 1)
)
ompRoutesTableFamilyEntriesAdvertisedPathsEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesAdvertisedToPeer"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 6, 1, 1),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTable_Object = MibTable
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7)
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry_Object = MibTableRow
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1)
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesPrefix"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesAdvertisedToPeer"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId"),
    (0, "VIPTELA-OMP", "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId"),
)
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 1),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 2),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 3),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 4),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 5),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("proto-invalid", 0),
          ("static", 1),
          ("connected", 2),
          ("eBGP", 3),
          ("iBGP", 4),
          ("oSPF-intra-area", 5),
          ("oSPF-inter-area", 6),
          ("oSPF-external-1", 7),
          ("oSPF-external-2", 8),
          ("aggregate", 9),
          ("natpoolInside", 10),
          ("eigrp-sum", 11),
          ("eigrp-int", 12),
          ("eigrp-ext", 13),
          ("lisp", 14),
          ("isis", 15))
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 6),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 7),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Type(Unsigned32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 8),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 9),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 10),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 11),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesTag_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Type = UnsignedShort
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 12),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Type = IpAddress
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 13),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Type = InetAddressIP
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 14),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 15),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 16),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap.setStatus("current")


class _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Type(Integer32):
    """Custom type ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("strict", 1),
          ("primary", 2),
          ("ecmp", 3),
          ("backup", 4))
    )


_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Type.__name__ = "Integer32"
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 17),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Type = Unsigned32
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 18),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Type = String
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 19),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath.setStatus("current")
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Type = String
_OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Object = MibTableColumn
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity = _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 3, 7, 1, 20),
    _OmpRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity_Type()
)
ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity.setStatus("current")
_OmpBestMatchRoute_ObjectIdentity = ObjectIdentity
ompBestMatchRoute = _OmpBestMatchRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4)
)
_OmpBestMatchRouteFamilyTable_Object = MibTable
ompBestMatchRouteFamilyTable = _OmpBestMatchRouteFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 1)
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyTable.setStatus("current")
_OmpBestMatchRouteFamilyEntry_Object = MibTableRow
ompBestMatchRouteFamilyEntry = _OmpBestMatchRouteFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 1, 1)
)
ompBestMatchRouteFamilyEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntry.setStatus("current")
_OmpBestMatchRouteFamilyAddressFamily_Type = AddrFamilyEnum
_OmpBestMatchRouteFamilyAddressFamily_Object = MibTableColumn
ompBestMatchRouteFamilyAddressFamily = _OmpBestMatchRouteFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 1, 1, 1),
    _OmpBestMatchRouteFamilyAddressFamily_Type()
)
ompBestMatchRouteFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyAddressFamily.setStatus("current")
_OmpBestMatchRouteFamilyEntriesTable_Object = MibTable
ompBestMatchRouteFamilyEntriesTable = _OmpBestMatchRouteFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 2)
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesTable.setStatus("current")
_OmpBestMatchRouteFamilyEntriesEntry_Object = MibTableRow
ompBestMatchRouteFamilyEntriesEntry = _OmpBestMatchRouteFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 2, 1)
)
ompBestMatchRouteFamilyEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesRouteAddr"),
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesEntry.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompBestMatchRouteFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpBestMatchRouteFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpBestMatchRouteFamilyEntriesVpnId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesVpnId = _OmpBestMatchRouteFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 2, 1, 1),
    _OmpBestMatchRouteFamilyEntriesVpnId_Type()
)
ompBestMatchRouteFamilyEntriesVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesVpnId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesRouteAddr_Type = InetAddressIP
_OmpBestMatchRouteFamilyEntriesRouteAddr_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesRouteAddr = _OmpBestMatchRouteFamilyEntriesRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 2, 1, 2),
    _OmpBestMatchRouteFamilyEntriesRouteAddr_Type()
)
ompBestMatchRouteFamilyEntriesRouteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesRouteAddr.setStatus("current")
_OmpBestMatchRouteFamilyEntriesPrefix_Type = IpPrefix
_OmpBestMatchRouteFamilyEntriesPrefix_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesPrefix = _OmpBestMatchRouteFamilyEntriesPrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 2, 1, 3),
    _OmpBestMatchRouteFamilyEntriesPrefix_Type()
)
ompBestMatchRouteFamilyEntriesPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesPrefix.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedTable_Object = MibTable
ompBestMatchRouteFamilyEntriesReceivedTable = _OmpBestMatchRouteFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3)
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedTable.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedEntry_Object = MibTableRow
ompBestMatchRouteFamilyEntriesReceivedEntry = _OmpBestMatchRouteFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1)
)
ompBestMatchRouteFamilyEntriesReceivedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesRouteAddr"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesReceivedFromPeer"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesReceivedPathId"),
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedEntry.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpBestMatchRouteFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedFromPeer = _OmpBestMatchRouteFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1, 1),
    _OmpBestMatchRouteFamilyEntriesReceivedFromPeer_Type()
)
ompBestMatchRouteFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedPathId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedPathId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedPathId = _OmpBestMatchRouteFamilyEntriesReceivedPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1, 2),
    _OmpBestMatchRouteFamilyEntriesReceivedPathId_Type()
)
ompBestMatchRouteFamilyEntriesReceivedPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedPathId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedLabel_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedLabel_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedLabel = _OmpBestMatchRouteFamilyEntriesReceivedLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1, 3),
    _OmpBestMatchRouteFamilyEntriesReceivedLabel_Type()
)
ompBestMatchRouteFamilyEntriesReceivedLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedLabel.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpBestMatchRouteFamilyEntriesReceivedStatus_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedStatus = _OmpBestMatchRouteFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1, 4),
    _OmpBestMatchRouteFamilyEntriesReceivedStatus_Type()
)
ompBestMatchRouteFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedStatus.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpBestMatchRouteFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedLossReason = _OmpBestMatchRouteFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1, 5),
    _OmpBestMatchRouteFamilyEntriesReceivedLossReason_Type()
)
ompBestMatchRouteFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedLossReason.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedLostToPeer_Type = InetAddressIP
_OmpBestMatchRouteFamilyEntriesReceivedLostToPeer_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedLostToPeer = _OmpBestMatchRouteFamilyEntriesReceivedLostToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1, 6),
    _OmpBestMatchRouteFamilyEntriesReceivedLostToPeer_Type()
)
ompBestMatchRouteFamilyEntriesReceivedLostToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedLostToPeer.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedLostToPathId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedLostToPathId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedLostToPathId = _OmpBestMatchRouteFamilyEntriesReceivedLostToPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 3, 1, 7),
    _OmpBestMatchRouteFamilyEntriesReceivedLostToPathId_Type()
)
ompBestMatchRouteFamilyEntriesReceivedLostToPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedLostToPathId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesTable_Object = MibTable
ompBestMatchRouteFamilyEntriesReceivedAttributesTable = _OmpBestMatchRouteFamilyEntriesReceivedAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4)
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesTable.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesEntry_Object = MibTableRow
ompBestMatchRouteFamilyEntriesReceivedAttributesEntry = _OmpBestMatchRouteFamilyEntriesReceivedAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1)
)
ompBestMatchRouteFamilyEntriesReceivedAttributesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesRouteAddr"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesReceivedFromPeer"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesReceivedPathId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey"),
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesEntry.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey = _OmpBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 1),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesAttributeType_Type = AttributeTypeEnum
_OmpBestMatchRouteFamilyEntriesReceivedAttributesAttributeType_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesAttributeType = _OmpBestMatchRouteFamilyEntriesReceivedAttributesAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 2),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesAttributeType_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesAttributeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesAttributeType.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocIp_Type = InetAddressIP
_OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocIp_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesTlocIp = _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 3),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocIp_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesTlocIp.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocColor_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesReceivedAttributesTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocColor_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocColor_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesTlocColor = _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 4),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocColor_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesTlocColor.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap = _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 5),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("proto-invalid", 0),
          ("static", 1),
          ("connected", 2),
          ("eBGP", 3),
          ("iBGP", 4),
          ("oSPF-intra-area", 5),
          ("oSPF-inter-area", 6),
          ("oSPF-external-1", 7),
          ("oSPF-external-2", 8),
          ("aggregate", 9),
          ("natpoolInside", 10),
          ("eigrp-sum", 11),
          ("eigrp-int", 12),
          ("eigrp-ext", 13),
          ("lisp", 14),
          ("isis", 15))
    )


_OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol = _OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 6),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric = _OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 7),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesReceivedAttributesDomainId_Type(Unsigned32):
    """Custom type ompBestMatchRouteFamilyEntriesReceivedAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpBestMatchRouteFamilyEntriesReceivedAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpBestMatchRouteFamilyEntriesReceivedAttributesDomainId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesDomainId = _OmpBestMatchRouteFamilyEntriesReceivedAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 8),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesDomainId_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesDomainId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesSiteId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedAttributesSiteId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesSiteId = _OmpBestMatchRouteFamilyEntriesReceivedAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 9),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesSiteId_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesSiteId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesPreference_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedAttributesPreference_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesPreference = _OmpBestMatchRouteFamilyEntriesReceivedAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 10),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesPreference_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesPreference.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesTag_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedAttributesTag_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesTag = _OmpBestMatchRouteFamilyEntriesReceivedAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 11),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesTag_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesTag.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen_Type = UnsignedShort
_OmpBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen = _OmpBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 12),
    _OmpBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginator_Type = IpAddress
_OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginator_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesOriginator = _OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 13),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesOriginator_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesOriginator.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesOverlayId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesReceivedAttributesOverlayId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesOverlayId = _OmpBestMatchRouteFamilyEntriesReceivedAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 14),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesOverlayId_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesOverlayId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesAsPath_Type = String
_OmpBestMatchRouteFamilyEntriesReceivedAttributesAsPath_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesAsPath = _OmpBestMatchRouteFamilyEntriesReceivedAttributesAsPath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 15),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesAsPath_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesAsPath.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesCommunity_Type = String
_OmpBestMatchRouteFamilyEntriesReceivedAttributesCommunity_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesCommunity = _OmpBestMatchRouteFamilyEntriesReceivedAttributesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 16),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesCommunity_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesCommunity.setStatus("current")
_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp_Type = InetAddressIP
_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp = _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 17),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor = _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 18),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gre", 1),
          ("ipsec", 2))
    )


_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap = _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 19),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("strict", 1),
          ("primary", 2),
          ("ecmp", 3),
          ("backup", 4))
    )


_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction = _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 4, 1, 20),
    _OmpBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction_Type()
)
ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedTable_Object = MibTable
ompBestMatchRouteFamilyEntriesAdvertisedTable = _OmpBestMatchRouteFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 5)
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedTable.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompBestMatchRouteFamilyEntriesAdvertisedEntry = _OmpBestMatchRouteFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 5, 1)
)
ompBestMatchRouteFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesRouteAddr"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpBestMatchRouteFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedToPeer = _OmpBestMatchRouteFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 5, 1, 1),
    _OmpBestMatchRouteFamilyEntriesAdvertisedToPeer_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsTable_Object = MibTable
ompBestMatchRouteFamilyEntriesAdvertisedPathsTable = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 6)
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsTable.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsEntry_Object = MibTableRow
ompBestMatchRouteFamilyEntriesAdvertisedPathsEntry = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 6, 1)
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesRouteAddr"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesAdvertisedToPeer"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId"),
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsEntry.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 6, 1, 1),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTable_Object = MibTable
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTable = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7)
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTable.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesEntry_Object = MibTableRow
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesEntry = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1)
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesRouteAddr"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesAdvertisedToPeer"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId"),
    (0, "VIPTELA-OMP", "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId"),
)
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesEntry.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 1),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 2),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp_Type = InetAddressIP
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 3),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 4),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 5),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto_Type(Integer32):
    """Custom type ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("proto-invalid", 0),
          ("static", 1),
          ("connected", 2),
          ("eBGP", 3),
          ("iBGP", 4),
          ("oSPF-intra-area", 5),
          ("oSPF-inter-area", 6),
          ("oSPF-external-1", 7),
          ("oSPF-external-2", 8),
          ("aggregate", 9),
          ("natpoolInside", 10),
          ("eigrp-sum", 11),
          ("eigrp-int", 12),
          ("eigrp-ext", 13),
          ("lisp", 14),
          ("isis", 15))
    )


_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto_Type.__name__ = "Integer32"
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 6),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 7),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet.setStatus("current")


class _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId_Type(Unsigned32):
    """Custom type ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 8),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 9),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 10),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 11),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Type = UnsignedShort
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 12),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator_Type = IpAddress
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 13),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId_Type = Unsigned32
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 14),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath_Type = String
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 15),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath.setStatus("current")
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity_Type = String
_OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity_Object = MibTableColumn
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity = _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 4, 7, 1, 16),
    _OmpBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity_Type()
)
ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity.setStatus("current")
_OmpTlocPaths_ObjectIdentity = ObjectIdentity
ompTlocPaths = _OmpTlocPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5)
)
_OmpTlocPathsEntriesTable_Object = MibTable
ompTlocPathsEntriesTable = _OmpTlocPathsEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 1)
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesTable.setStatus("current")
_OmpTlocPathsEntriesEntry_Object = MibTableRow
ompTlocPathsEntriesEntry = _OmpTlocPathsEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 1, 1)
)
ompTlocPathsEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesEncap"),
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesEntry.setStatus("current")
_OmpTlocPathsEntriesIp_Type = InetAddressIP
_OmpTlocPathsEntriesIp_Object = MibTableColumn
ompTlocPathsEntriesIp = _OmpTlocPathsEntriesIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 1, 1, 1),
    _OmpTlocPathsEntriesIp_Type()
)
ompTlocPathsEntriesIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesIp.setStatus("current")


class _OmpTlocPathsEntriesColor_Type(Integer32):
    """Custom type ompTlocPathsEntriesColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpTlocPathsEntriesColor_Type.__name__ = "Integer32"
_OmpTlocPathsEntriesColor_Object = MibTableColumn
ompTlocPathsEntriesColor = _OmpTlocPathsEntriesColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 1, 1, 2),
    _OmpTlocPathsEntriesColor_Type()
)
ompTlocPathsEntriesColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesColor.setStatus("current")


class _OmpTlocPathsEntriesEncap_Type(Integer32):
    """Custom type ompTlocPathsEntriesEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpTlocPathsEntriesEncap_Type.__name__ = "Integer32"
_OmpTlocPathsEntriesEncap_Object = MibTableColumn
ompTlocPathsEntriesEncap = _OmpTlocPathsEntriesEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 1, 1, 3),
    _OmpTlocPathsEntriesEncap_Type()
)
ompTlocPathsEntriesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesEncap.setStatus("current")
_OmpTlocPathsEntriesPathsTable_Object = MibTable
ompTlocPathsEntriesPathsTable = _OmpTlocPathsEntriesPathsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2)
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsTable.setStatus("current")
_OmpTlocPathsEntriesPathsEntry_Object = MibTableRow
ompTlocPathsEntriesPathsEntry = _OmpTlocPathsEntriesPathsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2, 1)
)
ompTlocPathsEntriesPathsEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesEncap"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesPathsIndex"),
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsEntry.setStatus("current")
_OmpTlocPathsEntriesPathsIndex_Type = Unsigned32
_OmpTlocPathsEntriesPathsIndex_Object = MibTableColumn
ompTlocPathsEntriesPathsIndex = _OmpTlocPathsEntriesPathsIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2, 1, 1),
    _OmpTlocPathsEntriesPathsIndex_Type()
)
ompTlocPathsEntriesPathsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsIndex.setStatus("current")
_OmpTlocPathsEntriesPathsPreference_Type = Unsigned32
_OmpTlocPathsEntriesPathsPreference_Object = MibTableColumn
ompTlocPathsEntriesPathsPreference = _OmpTlocPathsEntriesPathsPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2, 1, 2),
    _OmpTlocPathsEntriesPathsPreference_Type()
)
ompTlocPathsEntriesPathsPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsPreference.setStatus("current")
_OmpTlocPathsEntriesPathsMtu_Type = Unsigned32
_OmpTlocPathsEntriesPathsMtu_Object = MibTableColumn
ompTlocPathsEntriesPathsMtu = _OmpTlocPathsEntriesPathsMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2, 1, 3),
    _OmpTlocPathsEntriesPathsMtu_Type()
)
ompTlocPathsEntriesPathsMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsMtu.setStatus("current")
_OmpTlocPathsEntriesPathsBfdStatus_Type = BfdStatusEnum
_OmpTlocPathsEntriesPathsBfdStatus_Object = MibTableColumn
ompTlocPathsEntriesPathsBfdStatus = _OmpTlocPathsEntriesPathsBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2, 1, 4),
    _OmpTlocPathsEntriesPathsBfdStatus_Type()
)
ompTlocPathsEntriesPathsBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsBfdStatus.setStatus("current")
_OmpTlocPathsEntriesPathsStatus_Type = PathStatusEnum
_OmpTlocPathsEntriesPathsStatus_Object = MibTableColumn
ompTlocPathsEntriesPathsStatus = _OmpTlocPathsEntriesPathsStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2, 1, 6),
    _OmpTlocPathsEntriesPathsStatus_Type()
)
ompTlocPathsEntriesPathsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsStatus.setStatus("current")
_OmpTlocPathsEntriesPathsStale_Type = TruthValue
_OmpTlocPathsEntriesPathsStale_Object = MibTableColumn
ompTlocPathsEntriesPathsStale = _OmpTlocPathsEntriesPathsStale_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 2, 1, 7),
    _OmpTlocPathsEntriesPathsStale_Type()
)
ompTlocPathsEntriesPathsStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsStale.setStatus("current")
_OmpTlocPathsEntriesPathsLinksTable_Object = MibTable
ompTlocPathsEntriesPathsLinksTable = _OmpTlocPathsEntriesPathsLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3)
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksTable.setStatus("current")
_OmpTlocPathsEntriesPathsLinksEntry_Object = MibTableRow
ompTlocPathsEntriesPathsLinksEntry = _OmpTlocPathsEntriesPathsLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1)
)
ompTlocPathsEntriesPathsLinksEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesEncap"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesPathsIndex"),
    (0, "VIPTELA-OMP", "ompTlocPathsEntriesPathsLinksLinkIndex"),
)
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksEntry.setStatus("current")
_OmpTlocPathsEntriesPathsLinksLinkIndex_Type = Unsigned32
_OmpTlocPathsEntriesPathsLinksLinkIndex_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksLinkIndex = _OmpTlocPathsEntriesPathsLinksLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 1),
    _OmpTlocPathsEntriesPathsLinksLinkIndex_Type()
)
ompTlocPathsEntriesPathsLinksLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksLinkIndex.setStatus("current")
_OmpTlocPathsEntriesPathsLinksFromTlocIp_Type = InetAddressIP
_OmpTlocPathsEntriesPathsLinksFromTlocIp_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksFromTlocIp = _OmpTlocPathsEntriesPathsLinksFromTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 2),
    _OmpTlocPathsEntriesPathsLinksFromTlocIp_Type()
)
ompTlocPathsEntriesPathsLinksFromTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksFromTlocIp.setStatus("current")


class _OmpTlocPathsEntriesPathsLinksFromTlocColor_Type(Integer32):
    """Custom type ompTlocPathsEntriesPathsLinksFromTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpTlocPathsEntriesPathsLinksFromTlocColor_Type.__name__ = "Integer32"
_OmpTlocPathsEntriesPathsLinksFromTlocColor_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksFromTlocColor = _OmpTlocPathsEntriesPathsLinksFromTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 3),
    _OmpTlocPathsEntriesPathsLinksFromTlocColor_Type()
)
ompTlocPathsEntriesPathsLinksFromTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksFromTlocColor.setStatus("current")


class _OmpTlocPathsEntriesPathsLinksFromTlocEncap_Type(Integer32):
    """Custom type ompTlocPathsEntriesPathsLinksFromTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpTlocPathsEntriesPathsLinksFromTlocEncap_Type.__name__ = "Integer32"
_OmpTlocPathsEntriesPathsLinksFromTlocEncap_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksFromTlocEncap = _OmpTlocPathsEntriesPathsLinksFromTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 4),
    _OmpTlocPathsEntriesPathsLinksFromTlocEncap_Type()
)
ompTlocPathsEntriesPathsLinksFromTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksFromTlocEncap.setStatus("current")
_OmpTlocPathsEntriesPathsLinksToTlocIp_Type = InetAddressIP
_OmpTlocPathsEntriesPathsLinksToTlocIp_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksToTlocIp = _OmpTlocPathsEntriesPathsLinksToTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 5),
    _OmpTlocPathsEntriesPathsLinksToTlocIp_Type()
)
ompTlocPathsEntriesPathsLinksToTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksToTlocIp.setStatus("current")


class _OmpTlocPathsEntriesPathsLinksToTlocColor_Type(Integer32):
    """Custom type ompTlocPathsEntriesPathsLinksToTlocColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpTlocPathsEntriesPathsLinksToTlocColor_Type.__name__ = "Integer32"
_OmpTlocPathsEntriesPathsLinksToTlocColor_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksToTlocColor = _OmpTlocPathsEntriesPathsLinksToTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 6),
    _OmpTlocPathsEntriesPathsLinksToTlocColor_Type()
)
ompTlocPathsEntriesPathsLinksToTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksToTlocColor.setStatus("current")


class _OmpTlocPathsEntriesPathsLinksToTlocEncap_Type(Integer32):
    """Custom type ompTlocPathsEntriesPathsLinksToTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpTlocPathsEntriesPathsLinksToTlocEncap_Type.__name__ = "Integer32"
_OmpTlocPathsEntriesPathsLinksToTlocEncap_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksToTlocEncap = _OmpTlocPathsEntriesPathsLinksToTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 7),
    _OmpTlocPathsEntriesPathsLinksToTlocEncap_Type()
)
ompTlocPathsEntriesPathsLinksToTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksToTlocEncap.setStatus("current")
_OmpTlocPathsEntriesPathsLinksLabel_Type = Unsigned32
_OmpTlocPathsEntriesPathsLinksLabel_Object = MibTableColumn
ompTlocPathsEntriesPathsLinksLabel = _OmpTlocPathsEntriesPathsLinksLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 5, 3, 1, 8),
    _OmpTlocPathsEntriesPathsLinksLabel_Type()
)
ompTlocPathsEntriesPathsLinksLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocPathsEntriesPathsLinksLabel.setStatus("current")
_OmpTlocs_ObjectIdentity = ObjectIdentity
ompTlocs = _OmpTlocs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6)
)
_OmpTlocsFamilyTable_Object = MibTable
ompTlocsFamilyTable = _OmpTlocsFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 1)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyTable.setStatus("current")
_OmpTlocsFamilyEntry_Object = MibTableRow
ompTlocsFamilyEntry = _OmpTlocsFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 1, 1)
)
ompTlocsFamilyEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocsFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntry.setStatus("current")
_OmpTlocsFamilyAddressFamily_Type = AddrFamilyEnum
_OmpTlocsFamilyAddressFamily_Object = MibTableColumn
ompTlocsFamilyAddressFamily = _OmpTlocsFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 1, 1, 1),
    _OmpTlocsFamilyAddressFamily_Type()
)
ompTlocsFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyAddressFamily.setStatus("current")
_OmpTlocsFamilyEntriesTable_Object = MibTable
ompTlocsFamilyEntriesTable = _OmpTlocsFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 2)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesTable.setStatus("current")
_OmpTlocsFamilyEntriesEntry_Object = MibTableRow
ompTlocsFamilyEntriesEntry = _OmpTlocsFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 2, 1)
)
ompTlocsFamilyEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocsFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesEncap"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesEntry.setStatus("current")
_OmpTlocsFamilyEntriesIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesIp_Object = MibTableColumn
ompTlocsFamilyEntriesIp = _OmpTlocsFamilyEntriesIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 2, 1, 1),
    _OmpTlocsFamilyEntriesIp_Type()
)
ompTlocsFamilyEntriesIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesIp.setStatus("current")


class _OmpTlocsFamilyEntriesColor_Type(Integer32):
    """Custom type ompTlocsFamilyEntriesColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OmpTlocsFamilyEntriesColor_Type.__name__ = "Integer32"
_OmpTlocsFamilyEntriesColor_Object = MibTableColumn
ompTlocsFamilyEntriesColor = _OmpTlocsFamilyEntriesColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 2, 1, 2),
    _OmpTlocsFamilyEntriesColor_Type()
)
ompTlocsFamilyEntriesColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesColor.setStatus("current")


class _OmpTlocsFamilyEntriesEncap_Type(Integer32):
    """Custom type ompTlocsFamilyEntriesEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_OmpTlocsFamilyEntriesEncap_Type.__name__ = "Integer32"
_OmpTlocsFamilyEntriesEncap_Object = MibTableColumn
ompTlocsFamilyEntriesEncap = _OmpTlocsFamilyEntriesEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 2, 1, 3),
    _OmpTlocsFamilyEntriesEncap_Type()
)
ompTlocsFamilyEntriesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesEncap.setStatus("current")
_OmpTlocsFamilyEntriesReceivedTable_Object = MibTable
ompTlocsFamilyEntriesReceivedTable = _OmpTlocsFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 5)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedTable.setStatus("current")
_OmpTlocsFamilyEntriesReceivedEntry_Object = MibTableRow
ompTlocsFamilyEntriesReceivedEntry = _OmpTlocsFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 5, 1)
)
ompTlocsFamilyEntriesReceivedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocsFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesEncap"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedEntry.setStatus("current")
_OmpTlocsFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedFromPeer = _OmpTlocsFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 5, 1, 1),
    _OmpTlocsFamilyEntriesReceivedFromPeer_Type()
)
ompTlocsFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpTlocsFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpTlocsFamilyEntriesReceivedStatus_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedStatus = _OmpTlocsFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 5, 1, 2),
    _OmpTlocsFamilyEntriesReceivedStatus_Type()
)
ompTlocsFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedStatus.setStatus("current")
_OmpTlocsFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpTlocsFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedLossReason = _OmpTlocsFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 5, 1, 3),
    _OmpTlocsFamilyEntriesReceivedLossReason_Type()
)
ompTlocsFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedLossReason.setStatus("current")
_OmpTlocsFamilyEntriesReceivedLostToPeer_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedLostToPeer_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedLostToPeer = _OmpTlocsFamilyEntriesReceivedLostToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 5, 1, 4),
    _OmpTlocsFamilyEntriesReceivedLostToPeer_Type()
)
ompTlocsFamilyEntriesReceivedLostToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedLostToPeer.setStatus("current")
_OmpTlocsFamilyEntriesReceivedLostToPathId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedLostToPathId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedLostToPathId = _OmpTlocsFamilyEntriesReceivedLostToPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 5, 1, 5),
    _OmpTlocsFamilyEntriesReceivedLostToPathId_Type()
)
ompTlocsFamilyEntriesReceivedLostToPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedLostToPathId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTable_Object = MibTable
ompTlocsFamilyEntriesReceivedAttributesTable = _OmpTlocsFamilyEntriesReceivedAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTable.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesEntry_Object = MibTableRow
ompTlocsFamilyEntriesReceivedAttributesEntry = _OmpTlocsFamilyEntriesReceivedAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1)
)
ompTlocsFamilyEntriesReceivedAttributesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocsFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesEncap"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesReceivedFromPeer"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesReceivedAttributesPseudoKey"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesEntry.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesPseudoKey = _OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 1),
    _OmpTlocsFamilyEntriesReceivedAttributesPseudoKey_Type()
)
ompTlocsFamilyEntriesReceivedAttributesPseudoKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesPseudoKey.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Type = AttributeTypeEnum
_OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesAttributeType = _OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 2),
    _OmpTlocsFamilyEntriesReceivedAttributesAttributeType_Type()
)
ompTlocsFamilyEntriesReceivedAttributesAttributeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesAttributeType.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 3),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapKey_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 4),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapProto_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 5),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapSpi_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi.setStatus("current")


class _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType_Type(Bits):
    """Custom type ompTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 1),
          ("sha1Hmac", 2),
          ("ahSha1Hmac", 3),
          ("aesXcbc", 4),
          ("sha256", 5),
          ("sha384", 6),
          ("sha512", 7),
          ("ghash8", 8),
          ("ghash12", 9),
          ("ghash16", 10))
    )

_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType_Type.__name__ = "Bits"
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 6),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType.setStatus("current")


class _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Type(Bits):
    """Custom type ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("des", 1),
          ("des3", 2),
          ("aes128", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("aes128Ctr", 6),
          ("aes192Ctr", 7),
          ("aes256Ctr", 8),
          ("aes128Gmac", 9),
          ("aes192Gmac", 10),
          ("aes256Gmac", 11))
    )

_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Type.__name__ = "Bits"
_OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType = _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 7),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 8),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 9),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 10),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 11),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 12),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 13),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 14),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort = _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 15),
    _OmpTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Type = BfdStatusEnum
_OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesBfdStatus = _OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 16),
    _OmpTlocsFamilyEntriesReceivedAttributesBfdStatus_Type()
)
ompTlocsFamilyEntriesReceivedAttributesBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesBfdStatus.setStatus("current")


class _OmpTlocsFamilyEntriesReceivedAttributesDomainId_Type(Unsigned32):
    """Custom type ompTlocsFamilyEntriesReceivedAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpTlocsFamilyEntriesReceivedAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpTlocsFamilyEntriesReceivedAttributesDomainId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesDomainId = _OmpTlocsFamilyEntriesReceivedAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 17),
    _OmpTlocsFamilyEntriesReceivedAttributesDomainId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesDomainId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesSiteId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesSiteId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesSiteId = _OmpTlocsFamilyEntriesReceivedAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 18),
    _OmpTlocsFamilyEntriesReceivedAttributesSiteId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesSiteId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesPreference_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesPreference_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesPreference = _OmpTlocsFamilyEntriesReceivedAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 19),
    _OmpTlocsFamilyEntriesReceivedAttributesPreference_Type()
)
ompTlocsFamilyEntriesReceivedAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesPreference.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesTag_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesTag_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesTag = _OmpTlocsFamilyEntriesReceivedAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 20),
    _OmpTlocsFamilyEntriesReceivedAttributesTag_Type()
)
ompTlocsFamilyEntriesReceivedAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesTag.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesStale_Type = UnsignedByte
_OmpTlocsFamilyEntriesReceivedAttributesStale_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesStale = _OmpTlocsFamilyEntriesReceivedAttributesStale_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 21),
    _OmpTlocsFamilyEntriesReceivedAttributesStale_Type()
)
ompTlocsFamilyEntriesReceivedAttributesStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesStale.setStatus("current")


class _OmpTlocsFamilyEntriesReceivedAttributesCarrier_Type(Integer32):
    """Custom type ompTlocsFamilyEntriesReceivedAttributesCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("carrier1", 2),
          ("carrier2", 3),
          ("carrier3", 4),
          ("carrier4", 5),
          ("carrier5", 6),
          ("carrier6", 7),
          ("carrier7", 8),
          ("carrier8", 9))
    )


_OmpTlocsFamilyEntriesReceivedAttributesCarrier_Type.__name__ = "Integer32"
_OmpTlocsFamilyEntriesReceivedAttributesCarrier_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesCarrier = _OmpTlocsFamilyEntriesReceivedAttributesCarrier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 22),
    _OmpTlocsFamilyEntriesReceivedAttributesCarrier_Type()
)
ompTlocsFamilyEntriesReceivedAttributesCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesCarrier.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesGroups_Type = Groups1
_OmpTlocsFamilyEntriesReceivedAttributesGroups_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesGroups = _OmpTlocsFamilyEntriesReceivedAttributesGroups_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 23),
    _OmpTlocsFamilyEntriesReceivedAttributesGroups_Type()
)
ompTlocsFamilyEntriesReceivedAttributesGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesGroups.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Type = UnsignedShort
_OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen = _OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 24),
    _OmpTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen_Type()
)
ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesWeight_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesWeight_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesWeight = _OmpTlocsFamilyEntriesReceivedAttributesWeight_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 25),
    _OmpTlocsFamilyEntriesReceivedAttributesWeight_Type()
)
ompTlocsFamilyEntriesReceivedAttributesWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesWeight.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesGenId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesGenId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesGenId = _OmpTlocsFamilyEntriesReceivedAttributesGenId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 26),
    _OmpTlocsFamilyEntriesReceivedAttributesGenId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesGenId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesVersion_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesVersion_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesVersion = _OmpTlocsFamilyEntriesReceivedAttributesVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 27),
    _OmpTlocsFamilyEntriesReceivedAttributesVersion_Type()
)
ompTlocsFamilyEntriesReceivedAttributesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesVersion.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesOriginator_Type = IpAddress
_OmpTlocsFamilyEntriesReceivedAttributesOriginator_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesOriginator = _OmpTlocsFamilyEntriesReceivedAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 28),
    _OmpTlocsFamilyEntriesReceivedAttributesOriginator_Type()
)
ompTlocsFamilyEntriesReceivedAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesOriginator.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesRestrict_Type = UnsignedByte
_OmpTlocsFamilyEntriesReceivedAttributesRestrict_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesRestrict = _OmpTlocsFamilyEntriesReceivedAttributesRestrict_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 29),
    _OmpTlocsFamilyEntriesReceivedAttributesRestrict_Type()
)
ompTlocsFamilyEntriesReceivedAttributesRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesRestrict.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesOverlayId = _OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 30),
    _OmpTlocsFamilyEntriesReceivedAttributesOverlayId_Type()
)
ompTlocsFamilyEntriesReceivedAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesOverlayId.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Type = Unsigned32
_OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesBandwidth = _OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 31),
    _OmpTlocsFamilyEntriesReceivedAttributesBandwidth_Type()
)
ompTlocsFamilyEntriesReceivedAttributesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesBandwidth.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Type = String
_OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesQosGroup = _OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 32),
    _OmpTlocsFamilyEntriesReceivedAttributesQosGroup_Type()
)
ompTlocsFamilyEntriesReceivedAttributesQosGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesQosGroup.setStatus("current")
_OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Type = UnsignedByte
_OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Object = MibTableColumn
ompTlocsFamilyEntriesReceivedAttributesOnDemand = _OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 6, 1, 33),
    _OmpTlocsFamilyEntriesReceivedAttributesOnDemand_Type()
)
ompTlocsFamilyEntriesReceivedAttributesOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesReceivedAttributesOnDemand.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedTable_Object = MibTable
ompTlocsFamilyEntriesAdvertisedTable = _OmpTlocsFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 7)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedTable.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompTlocsFamilyEntriesAdvertisedEntry = _OmpTlocsFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 7, 1)
)
ompTlocsFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocsFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesEncap"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedToPeer = _OmpTlocsFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 7, 1, 1),
    _OmpTlocsFamilyEntriesAdvertisedToPeer_Type()
)
ompTlocsFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTable_Object = MibTable
ompTlocsFamilyEntriesAdvertisedAttributesTable = _OmpTlocsFamilyEntriesAdvertisedAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8)
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTable.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesEntry_Object = MibTableRow
ompTlocsFamilyEntriesAdvertisedAttributesEntry = _OmpTlocsFamilyEntriesAdvertisedAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1)
)
ompTlocsFamilyEntriesAdvertisedAttributesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompTlocsFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesIp"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesColor"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesEncap"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesAdvertisedToPeer"),
    (0, "VIPTELA-OMP", "ompTlocsFamilyEntriesAdvertisedAttributesAttributeId"),
)
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesEntry.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesAttributeId = _OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 1),
    _OmpTlocsFamilyEntriesAdvertisedAttributesAttributeId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesAttributeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesAttributeId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 2),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 3),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 4),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi.setStatus("current")


class _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType_Type(Bits):
    """Custom type ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 1),
          ("sha1Hmac", 2),
          ("ahSha1Hmac", 3),
          ("aesXcbc", 4),
          ("sha256", 5),
          ("sha384", 6),
          ("sha512", 7),
          ("ghash8", 8),
          ("ghash12", 9),
          ("ghash16", 10))
    )

_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType_Type.__name__ = "Bits"
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 5),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType.setStatus("current")


class _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Type(Bits):
    """Custom type ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("des", 1),
          ("des3", 2),
          ("aes128", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("aes128Ctr", 6),
          ("aes192Ctr", 7),
          ("aes256Ctr", 8),
          ("aes128Gmac", 9),
          ("aes192Gmac", 10),
          ("aes256Gmac", 11))
    )

_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Type.__name__ = "Bits"
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 6),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 7),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 8),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 9),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 10),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 11),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 12),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Type = InetAddressIP
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 13),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort = _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 14),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort.setStatus("current")


class _OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Type(Unsigned32):
    """Custom type ompTlocsFamilyEntriesAdvertisedAttributesDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Type.__name__ = "Unsigned32"
_OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesDomainId = _OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 15),
    _OmpTlocsFamilyEntriesAdvertisedAttributesDomainId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesDomainId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesSiteId = _OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 16),
    _OmpTlocsFamilyEntriesAdvertisedAttributesSiteId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesSiteId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesPreference = _OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 17),
    _OmpTlocsFamilyEntriesAdvertisedAttributesPreference_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesPreference.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesTag_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesTag_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesTag = _OmpTlocsFamilyEntriesAdvertisedAttributesTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 18),
    _OmpTlocsFamilyEntriesAdvertisedAttributesTag_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesTag.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesStale_Type = UnsignedByte
_OmpTlocsFamilyEntriesAdvertisedAttributesStale_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesStale = _OmpTlocsFamilyEntriesAdvertisedAttributesStale_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 19),
    _OmpTlocsFamilyEntriesAdvertisedAttributesStale_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesStale.setStatus("current")


class _OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Type(Integer32):
    """Custom type ompTlocsFamilyEntriesAdvertisedAttributesCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("carrier1", 2),
          ("carrier2", 3),
          ("carrier3", 4),
          ("carrier4", 5),
          ("carrier5", 6),
          ("carrier6", 7),
          ("carrier7", 8),
          ("carrier8", 9))
    )


_OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Type.__name__ = "Integer32"
_OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesCarrier = _OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 20),
    _OmpTlocsFamilyEntriesAdvertisedAttributesCarrier_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesCarrier.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Type = Groups1
_OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesGroups = _OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 21),
    _OmpTlocsFamilyEntriesAdvertisedAttributesGroups_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesGroups.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Type = UnsignedShort
_OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen = _OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 22),
    _OmpTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesWeight = _OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 23),
    _OmpTlocsFamilyEntriesAdvertisedAttributesWeight_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesWeight.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesGenId = _OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 24),
    _OmpTlocsFamilyEntriesAdvertisedAttributesGenId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesGenId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesVersion = _OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 25),
    _OmpTlocsFamilyEntriesAdvertisedAttributesVersion_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesVersion.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Type = IpAddress
_OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesOriginator = _OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 26),
    _OmpTlocsFamilyEntriesAdvertisedAttributesOriginator_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesOriginator.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Type = UnsignedByte
_OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesRestrict = _OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 27),
    _OmpTlocsFamilyEntriesAdvertisedAttributesRestrict_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesRestrict.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesOverlayId = _OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 28),
    _OmpTlocsFamilyEntriesAdvertisedAttributesOverlayId_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesOverlayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesOverlayId.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Type = Unsigned32
_OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesBandwidth = _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 29),
    _OmpTlocsFamilyEntriesAdvertisedAttributesBandwidth_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesBandwidth.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Type = String
_OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesQosGroup = _OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 30),
    _OmpTlocsFamilyEntriesAdvertisedAttributesQosGroup_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesQosGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesQosGroup.setStatus("current")
_OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Type = UnsignedByte
_OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Object = MibTableColumn
ompTlocsFamilyEntriesAdvertisedAttributesOnDemand = _OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 6, 8, 1, 31),
    _OmpTlocsFamilyEntriesAdvertisedAttributesOnDemand_Type()
)
ompTlocsFamilyEntriesAdvertisedAttributesOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompTlocsFamilyEntriesAdvertisedAttributesOnDemand.setStatus("current")
_OmpServices_ObjectIdentity = ObjectIdentity
ompServices = _OmpServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7)
)
_OmpServicesFamilyTable_Object = MibTable
ompServicesFamilyTable = _OmpServicesFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 1)
)
if mibBuilder.loadTexts:
    ompServicesFamilyTable.setStatus("current")
_OmpServicesFamilyEntry_Object = MibTableRow
ompServicesFamilyEntry = _OmpServicesFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 1, 1)
)
ompServicesFamilyEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompServicesFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntry.setStatus("current")
_OmpServicesFamilyAddressFamily_Type = AddrFamilyEnum
_OmpServicesFamilyAddressFamily_Object = MibTableColumn
ompServicesFamilyAddressFamily = _OmpServicesFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 1, 1, 1),
    _OmpServicesFamilyAddressFamily_Type()
)
ompServicesFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyAddressFamily.setStatus("current")
_OmpServicesFamilyEntriesTable_Object = MibTable
ompServicesFamilyEntriesTable = _OmpServicesFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 2)
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesTable.setStatus("current")
_OmpServicesFamilyEntriesEntry_Object = MibTableRow
ompServicesFamilyEntriesEntry = _OmpServicesFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 2, 1)
)
ompServicesFamilyEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompServicesFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesService"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesOriginator"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesEntry.setStatus("current")


class _OmpServicesFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompServicesFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpServicesFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpServicesFamilyEntriesVpnId_Object = MibTableColumn
ompServicesFamilyEntriesVpnId = _OmpServicesFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 2, 1, 1),
    _OmpServicesFamilyEntriesVpnId_Type()
)
ompServicesFamilyEntriesVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesVpnId.setStatus("current")


class _OmpServicesFamilyEntriesService_Type(Integer32):
    """Custom type ompServicesFamilyEntriesService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("vPN", 0),
          ("fW", 1),
          ("iDS", 2),
          ("iDP", 3),
          ("netsvc1", 4),
          ("netsvc2", 5),
          ("netsvc3", 6),
          ("netsvc4", 7),
          ("tE", 8),
          ("sig", 9))
    )


_OmpServicesFamilyEntriesService_Type.__name__ = "Integer32"
_OmpServicesFamilyEntriesService_Object = MibTableColumn
ompServicesFamilyEntriesService = _OmpServicesFamilyEntriesService_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 2, 1, 2),
    _OmpServicesFamilyEntriesService_Type()
)
ompServicesFamilyEntriesService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesService.setStatus("current")
_OmpServicesFamilyEntriesOriginator_Type = InetAddressIP
_OmpServicesFamilyEntriesOriginator_Object = MibTableColumn
ompServicesFamilyEntriesOriginator = _OmpServicesFamilyEntriesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 2, 1, 3),
    _OmpServicesFamilyEntriesOriginator_Type()
)
ompServicesFamilyEntriesOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesOriginator.setStatus("current")
_OmpServicesFamilyEntriesReceivedTable_Object = MibTable
ompServicesFamilyEntriesReceivedTable = _OmpServicesFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3)
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedTable.setStatus("current")
_OmpServicesFamilyEntriesReceivedEntry_Object = MibTableRow
ompServicesFamilyEntriesReceivedEntry = _OmpServicesFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1)
)
ompServicesFamilyEntriesReceivedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompServicesFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesService"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesOriginator"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesReceivedFromPeer"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesReceivedPathId"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedEntry.setStatus("current")
_OmpServicesFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpServicesFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompServicesFamilyEntriesReceivedFromPeer = _OmpServicesFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1, 1),
    _OmpServicesFamilyEntriesReceivedFromPeer_Type()
)
ompServicesFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpServicesFamilyEntriesReceivedPathId_Type = Unsigned32
_OmpServicesFamilyEntriesReceivedPathId_Object = MibTableColumn
ompServicesFamilyEntriesReceivedPathId = _OmpServicesFamilyEntriesReceivedPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1, 2),
    _OmpServicesFamilyEntriesReceivedPathId_Type()
)
ompServicesFamilyEntriesReceivedPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedPathId.setStatus("current")
_OmpServicesFamilyEntriesReceivedLabel_Type = Unsigned32
_OmpServicesFamilyEntriesReceivedLabel_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLabel = _OmpServicesFamilyEntriesReceivedLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1, 3),
    _OmpServicesFamilyEntriesReceivedLabel_Type()
)
ompServicesFamilyEntriesReceivedLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLabel.setStatus("current")
_OmpServicesFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpServicesFamilyEntriesReceivedStatus_Object = MibTableColumn
ompServicesFamilyEntriesReceivedStatus = _OmpServicesFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1, 4),
    _OmpServicesFamilyEntriesReceivedStatus_Type()
)
ompServicesFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedStatus.setStatus("current")
_OmpServicesFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpServicesFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLossReason = _OmpServicesFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1, 5),
    _OmpServicesFamilyEntriesReceivedLossReason_Type()
)
ompServicesFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLossReason.setStatus("current")
_OmpServicesFamilyEntriesReceivedLostToPeer_Type = InetAddressIP
_OmpServicesFamilyEntriesReceivedLostToPeer_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLostToPeer = _OmpServicesFamilyEntriesReceivedLostToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1, 6),
    _OmpServicesFamilyEntriesReceivedLostToPeer_Type()
)
ompServicesFamilyEntriesReceivedLostToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLostToPeer.setStatus("current")
_OmpServicesFamilyEntriesReceivedLostToPathId_Type = Unsigned32
_OmpServicesFamilyEntriesReceivedLostToPathId_Object = MibTableColumn
ompServicesFamilyEntriesReceivedLostToPathId = _OmpServicesFamilyEntriesReceivedLostToPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 3, 1, 7),
    _OmpServicesFamilyEntriesReceivedLostToPathId_Type()
)
ompServicesFamilyEntriesReceivedLostToPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesReceivedLostToPathId.setStatus("current")
_OmpServicesFamilyEntriesAdvertisedTable_Object = MibTable
ompServicesFamilyEntriesAdvertisedTable = _OmpServicesFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 4)
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesAdvertisedTable.setStatus("current")
_OmpServicesFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompServicesFamilyEntriesAdvertisedEntry = _OmpServicesFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 4, 1)
)
ompServicesFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompServicesFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesService"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesOriginator"),
    (0, "VIPTELA-OMP", "ompServicesFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpServicesFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpServicesFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompServicesFamilyEntriesAdvertisedToPeer = _OmpServicesFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 7, 4, 1, 1),
    _OmpServicesFamilyEntriesAdvertisedToPeer_Type()
)
ompServicesFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompServicesFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpMulticastAutoDiscover_ObjectIdentity = ObjectIdentity
ompMulticastAutoDiscover = _OmpMulticastAutoDiscover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8)
)
_OmpMulticastAutoDiscoverFamilyTable_Object = MibTable
ompMulticastAutoDiscoverFamilyTable = _OmpMulticastAutoDiscoverFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 1)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntry = _OmpMulticastAutoDiscoverFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 1, 1)
)
ompMulticastAutoDiscoverFamilyEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntry.setStatus("current")
_OmpMulticastAutoDiscoverFamilyAddressFamily_Type = AddrFamilyEnum
_OmpMulticastAutoDiscoverFamilyAddressFamily_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyAddressFamily = _OmpMulticastAutoDiscoverFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 1, 1, 1),
    _OmpMulticastAutoDiscoverFamilyAddressFamily_Type()
)
ompMulticastAutoDiscoverFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyAddressFamily.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesTable_Object = MibTable
ompMulticastAutoDiscoverFamilyEntriesTable = _OmpMulticastAutoDiscoverFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 2)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntriesEntry = _OmpMulticastAutoDiscoverFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 2, 1)
)
ompMulticastAutoDiscoverFamilyEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesEntry.setStatus("current")


class _OmpMulticastAutoDiscoverFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompMulticastAutoDiscoverFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpMulticastAutoDiscoverFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpMulticastAutoDiscoverFamilyEntriesVpnId_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesVpnId = _OmpMulticastAutoDiscoverFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 2, 1, 1),
    _OmpMulticastAutoDiscoverFamilyEntriesVpnId_Type()
)
ompMulticastAutoDiscoverFamilyEntriesVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesVpnId.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Type = IpAddress
_OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesSourceOriginator = _OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 2, 1, 2),
    _OmpMulticastAutoDiscoverFamilyEntriesSourceOriginator_Type()
)
ompMulticastAutoDiscoverFamilyEntriesSourceOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesSourceOriginator.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedTable_Object = MibTable
ompMulticastAutoDiscoverFamilyEntriesReceivedTable = _OmpMulticastAutoDiscoverFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 3)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntriesReceivedEntry = _OmpMulticastAutoDiscoverFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 3, 1)
)
ompMulticastAutoDiscoverFamilyEntriesReceivedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedEntry.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer = _OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 3, 1, 1),
    _OmpMulticastAutoDiscoverFamilyEntriesReceivedFromPeer_Type()
)
ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesReceivedStatus = _OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 3, 1, 2),
    _OmpMulticastAutoDiscoverFamilyEntriesReceivedStatus_Type()
)
ompMulticastAutoDiscoverFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedStatus.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason = _OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 3, 1, 3),
    _OmpMulticastAutoDiscoverFamilyEntriesReceivedLossReason_Type()
)
ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedTable_Object = MibTable
ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable = _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 4)
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry = _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 4, 1)
)
ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator"),
    (0, "VIPTELA-OMP", "ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer = _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 8, 4, 1, 1),
    _OmpMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer_Type()
)
ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpMulticastRoutes_ObjectIdentity = ObjectIdentity
ompMulticastRoutes = _OmpMulticastRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9)
)
_OmpMulticastRoutesFamilyTable_Object = MibTable
ompMulticastRoutesFamilyTable = _OmpMulticastRoutesFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 1)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyTable.setStatus("current")
_OmpMulticastRoutesFamilyEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntry = _OmpMulticastRoutesFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 1, 1)
)
ompMulticastRoutesFamilyEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyAddressFamily"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntry.setStatus("current")
_OmpMulticastRoutesFamilyAddressFamily_Type = AddrFamilyEnum
_OmpMulticastRoutesFamilyAddressFamily_Object = MibTableColumn
ompMulticastRoutesFamilyAddressFamily = _OmpMulticastRoutesFamilyAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 1, 1, 1),
    _OmpMulticastRoutesFamilyAddressFamily_Type()
)
ompMulticastRoutesFamilyAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyAddressFamily.setStatus("current")
_OmpMulticastRoutesFamilyEntriesTable_Object = MibTable
ompMulticastRoutesFamilyEntriesTable = _OmpMulticastRoutesFamilyEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesTable.setStatus("current")
_OmpMulticastRoutesFamilyEntriesEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntriesEntry = _OmpMulticastRoutesFamilyEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2, 1)
)
ompMulticastRoutesFamilyEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesType"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesSourceOriginator"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesDestination"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesGroup"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesSource"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesEntry.setStatus("current")
_OmpMulticastRoutesFamilyEntriesType_Type = McastRouteEnum
_OmpMulticastRoutesFamilyEntriesType_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesType = _OmpMulticastRoutesFamilyEntriesType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2, 1, 1),
    _OmpMulticastRoutesFamilyEntriesType_Type()
)
ompMulticastRoutesFamilyEntriesType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesType.setStatus("current")


class _OmpMulticastRoutesFamilyEntriesVpnId_Type(Unsigned32):
    """Custom type ompMulticastRoutesFamilyEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpMulticastRoutesFamilyEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpMulticastRoutesFamilyEntriesVpnId_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesVpnId = _OmpMulticastRoutesFamilyEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2, 1, 2),
    _OmpMulticastRoutesFamilyEntriesVpnId_Type()
)
ompMulticastRoutesFamilyEntriesVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesVpnId.setStatus("current")
_OmpMulticastRoutesFamilyEntriesSourceOriginator_Type = IpAddress
_OmpMulticastRoutesFamilyEntriesSourceOriginator_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesSourceOriginator = _OmpMulticastRoutesFamilyEntriesSourceOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2, 1, 3),
    _OmpMulticastRoutesFamilyEntriesSourceOriginator_Type()
)
ompMulticastRoutesFamilyEntriesSourceOriginator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesSourceOriginator.setStatus("current")
_OmpMulticastRoutesFamilyEntriesDestination_Type = IpAddress
_OmpMulticastRoutesFamilyEntriesDestination_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesDestination = _OmpMulticastRoutesFamilyEntriesDestination_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2, 1, 4),
    _OmpMulticastRoutesFamilyEntriesDestination_Type()
)
ompMulticastRoutesFamilyEntriesDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesDestination.setStatus("current")
_OmpMulticastRoutesFamilyEntriesGroup_Type = IpAddress
_OmpMulticastRoutesFamilyEntriesGroup_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesGroup = _OmpMulticastRoutesFamilyEntriesGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2, 1, 5),
    _OmpMulticastRoutesFamilyEntriesGroup_Type()
)
ompMulticastRoutesFamilyEntriesGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesGroup.setStatus("current")
_OmpMulticastRoutesFamilyEntriesSource_Type = IpAddress
_OmpMulticastRoutesFamilyEntriesSource_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesSource = _OmpMulticastRoutesFamilyEntriesSource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 2, 1, 6),
    _OmpMulticastRoutesFamilyEntriesSource_Type()
)
ompMulticastRoutesFamilyEntriesSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesSource.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedTable_Object = MibTable
ompMulticastRoutesFamilyEntriesReceivedTable = _OmpMulticastRoutesFamilyEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 3)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedTable.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntriesReceivedEntry = _OmpMulticastRoutesFamilyEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 3, 1)
)
ompMulticastRoutesFamilyEntriesReceivedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesType"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesSourceOriginator"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesDestination"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesGroup"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesSource"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedEntry.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedFromPeer = _OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 3, 1, 1),
    _OmpMulticastRoutesFamilyEntriesReceivedFromPeer_Type()
)
ompMulticastRoutesFamilyEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedFromPeer.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedRp_Type = IpAddress
_OmpMulticastRoutesFamilyEntriesReceivedRp_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedRp = _OmpMulticastRoutesFamilyEntriesReceivedRp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 3, 1, 2),
    _OmpMulticastRoutesFamilyEntriesReceivedRp_Type()
)
ompMulticastRoutesFamilyEntriesReceivedRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedRp.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Type = ReceivedPrunes1
_OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes = _OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 3, 1, 3),
    _OmpMulticastRoutesFamilyEntriesReceivedReceivedPrunes_Type()
)
ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedStatus_Type = RibInStatusType
_OmpMulticastRoutesFamilyEntriesReceivedStatus_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedStatus = _OmpMulticastRoutesFamilyEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 3, 1, 4),
    _OmpMulticastRoutesFamilyEntriesReceivedStatus_Type()
)
ompMulticastRoutesFamilyEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedStatus.setStatus("current")
_OmpMulticastRoutesFamilyEntriesReceivedLossReason_Type = LossReasonEnum
_OmpMulticastRoutesFamilyEntriesReceivedLossReason_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesReceivedLossReason = _OmpMulticastRoutesFamilyEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 3, 1, 5),
    _OmpMulticastRoutesFamilyEntriesReceivedLossReason_Type()
)
ompMulticastRoutesFamilyEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesReceivedLossReason.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedTable_Object = MibTable
ompMulticastRoutesFamilyEntriesAdvertisedTable = _OmpMulticastRoutesFamilyEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 4)
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedTable.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedEntry_Object = MibTableRow
ompMulticastRoutesFamilyEntriesAdvertisedEntry = _OmpMulticastRoutesFamilyEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 4, 1)
)
ompMulticastRoutesFamilyEntriesAdvertisedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyAddressFamily"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesType"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesSourceOriginator"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesDestination"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesGroup"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesSource"),
    (0, "VIPTELA-OMP", "ompMulticastRoutesFamilyEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedEntry.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesAdvertisedToPeer = _OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 4, 1, 1),
    _OmpMulticastRoutesFamilyEntriesAdvertisedToPeer_Type()
)
ompMulticastRoutesFamilyEntriesAdvertisedToPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedToPeer.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedRp_Type = IpAddress
_OmpMulticastRoutesFamilyEntriesAdvertisedRp_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesAdvertisedRp = _OmpMulticastRoutesFamilyEntriesAdvertisedRp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 4, 1, 2),
    _OmpMulticastRoutesFamilyEntriesAdvertisedRp_Type()
)
ompMulticastRoutesFamilyEntriesAdvertisedRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedRp.setStatus("current")
_OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Type = AdvertisedPrunes1
_OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Object = MibTableColumn
ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes = _OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 9, 4, 1, 3),
    _OmpMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes_Type()
)
ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes.setStatus("current")
_OmpCloudexpressRoutes_ObjectIdentity = ObjectIdentity
ompCloudexpressRoutes = _OmpCloudexpressRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10)
)
_OmpCloudexpressEntriesTable_Object = MibTable
ompCloudexpressEntriesTable = _OmpCloudexpressEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 1)
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesTable.setStatus("current")
_OmpCloudexpressEntriesEntry_Object = MibTableRow
ompCloudexpressEntriesEntry = _OmpCloudexpressEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 1, 1)
)
ompCloudexpressEntriesEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesOriginator"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesAppid"),
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesEntry.setStatus("current")


class _OmpCloudexpressEntriesVpnId_Type(Unsigned32):
    """Custom type ompCloudexpressEntriesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OmpCloudexpressEntriesVpnId_Type.__name__ = "Unsigned32"
_OmpCloudexpressEntriesVpnId_Object = MibTableColumn
ompCloudexpressEntriesVpnId = _OmpCloudexpressEntriesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 1, 1, 1),
    _OmpCloudexpressEntriesVpnId_Type()
)
ompCloudexpressEntriesVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesVpnId.setStatus("current")
_OmpCloudexpressEntriesOriginator_Type = IpAddress
_OmpCloudexpressEntriesOriginator_Object = MibTableColumn
ompCloudexpressEntriesOriginator = _OmpCloudexpressEntriesOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 1, 1, 2),
    _OmpCloudexpressEntriesOriginator_Type()
)
ompCloudexpressEntriesOriginator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesOriginator.setStatus("current")
_OmpCloudexpressEntriesAppid_Type = Unsigned32
_OmpCloudexpressEntriesAppid_Object = MibTableColumn
ompCloudexpressEntriesAppid = _OmpCloudexpressEntriesAppid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 1, 1, 3),
    _OmpCloudexpressEntriesAppid_Type()
)
ompCloudexpressEntriesAppid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAppid.setStatus("current")
_OmpCloudexpressEntriesAppname_Type = String
_OmpCloudexpressEntriesAppname_Object = MibTableColumn
ompCloudexpressEntriesAppname = _OmpCloudexpressEntriesAppname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 1, 1, 4),
    _OmpCloudexpressEntriesAppname_Type()
)
ompCloudexpressEntriesAppname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAppname.setStatus("current")
_OmpCloudexpressEntriesReceivedTable_Object = MibTable
ompCloudexpressEntriesReceivedTable = _OmpCloudexpressEntriesReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 2)
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedTable.setStatus("current")
_OmpCloudexpressEntriesReceivedEntry_Object = MibTableRow
ompCloudexpressEntriesReceivedEntry = _OmpCloudexpressEntriesReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 2, 1)
)
ompCloudexpressEntriesReceivedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesOriginator"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesAppid"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesReceivedFromPeer"),
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedEntry.setStatus("current")
_OmpCloudexpressEntriesReceivedFromPeer_Type = InetAddressIP
_OmpCloudexpressEntriesReceivedFromPeer_Object = MibTableColumn
ompCloudexpressEntriesReceivedFromPeer = _OmpCloudexpressEntriesReceivedFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 2, 1, 1),
    _OmpCloudexpressEntriesReceivedFromPeer_Type()
)
ompCloudexpressEntriesReceivedFromPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedFromPeer.setStatus("current")
_OmpCloudexpressEntriesReceivedStatus_Type = RibInStatusType
_OmpCloudexpressEntriesReceivedStatus_Object = MibTableColumn
ompCloudexpressEntriesReceivedStatus = _OmpCloudexpressEntriesReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 2, 1, 2),
    _OmpCloudexpressEntriesReceivedStatus_Type()
)
ompCloudexpressEntriesReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedStatus.setStatus("current")
_OmpCloudexpressEntriesReceivedLossReason_Type = LossReasonEnum
_OmpCloudexpressEntriesReceivedLossReason_Object = MibTableColumn
ompCloudexpressEntriesReceivedLossReason = _OmpCloudexpressEntriesReceivedLossReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 2, 1, 3),
    _OmpCloudexpressEntriesReceivedLossReason_Type()
)
ompCloudexpressEntriesReceivedLossReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedLossReason.setStatus("current")
_OmpCloudexpressEntriesReceivedLatency_Type = Unsigned32
_OmpCloudexpressEntriesReceivedLatency_Object = MibTableColumn
ompCloudexpressEntriesReceivedLatency = _OmpCloudexpressEntriesReceivedLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 2, 1, 4),
    _OmpCloudexpressEntriesReceivedLatency_Type()
)
ompCloudexpressEntriesReceivedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedLatency.setStatus("current")
_OmpCloudexpressEntriesReceivedLoss_Type = Unsigned32
_OmpCloudexpressEntriesReceivedLoss_Object = MibTableColumn
ompCloudexpressEntriesReceivedLoss = _OmpCloudexpressEntriesReceivedLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 2, 1, 5),
    _OmpCloudexpressEntriesReceivedLoss_Type()
)
ompCloudexpressEntriesReceivedLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesReceivedLoss.setStatus("current")
_OmpCloudexpressEntriesAdvertisedTable_Object = MibTable
ompCloudexpressEntriesAdvertisedTable = _OmpCloudexpressEntriesAdvertisedTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 3)
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedTable.setStatus("current")
_OmpCloudexpressEntriesAdvertisedEntry_Object = MibTableRow
ompCloudexpressEntriesAdvertisedEntry = _OmpCloudexpressEntriesAdvertisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 3, 1)
)
ompCloudexpressEntriesAdvertisedEntry.setIndexNames(
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesVpnId"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesOriginator"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesAppid"),
    (0, "VIPTELA-OMP", "ompCloudexpressEntriesAdvertisedToPeer"),
)
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedEntry.setStatus("current")
_OmpCloudexpressEntriesAdvertisedToPeer_Type = InetAddressIP
_OmpCloudexpressEntriesAdvertisedToPeer_Object = MibTableColumn
ompCloudexpressEntriesAdvertisedToPeer = _OmpCloudexpressEntriesAdvertisedToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 3, 1, 1),
    _OmpCloudexpressEntriesAdvertisedToPeer_Type()
)
ompCloudexpressEntriesAdvertisedToPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedToPeer.setStatus("current")
_OmpCloudexpressEntriesAdvertisedLatency_Type = Unsigned32
_OmpCloudexpressEntriesAdvertisedLatency_Object = MibTableColumn
ompCloudexpressEntriesAdvertisedLatency = _OmpCloudexpressEntriesAdvertisedLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 3, 1, 2),
    _OmpCloudexpressEntriesAdvertisedLatency_Type()
)
ompCloudexpressEntriesAdvertisedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedLatency.setStatus("current")
_OmpCloudexpressEntriesAdvertisedLoss_Type = Unsigned32
_OmpCloudexpressEntriesAdvertisedLoss_Object = MibTableColumn
ompCloudexpressEntriesAdvertisedLoss = _OmpCloudexpressEntriesAdvertisedLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 5, 10, 3, 1, 3),
    _OmpCloudexpressEntriesAdvertisedLoss_Type()
)
ompCloudexpressEntriesAdvertisedLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ompCloudexpressEntriesAdvertisedLoss.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-OMP",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "InetAddressIP": InetAddressIP,
       "IpPrefix": IpPrefix,
       "String": String,
       "Groups1": Groups1,
       "ReceivedPrunes": ReceivedPrunes,
       "AttributeTypeEnum": AttributeTypeEnum,
       "Groups": Groups,
       "AdvertisedPrunes": AdvertisedPrunes,
       "Route1": Route1,
       "Route": Route,
       "ReceivedPrunes1": ReceivedPrunes1,
       "AdvertisedPrunes1": AdvertisedPrunes1,
       "AfTypeEnum": AfTypeEnum,
       "BfdStatusEnum": BfdStatusEnum,
       "PathStatusEnum": PathStatusEnum,
       "RibInStatusType": RibInStatusType,
       "AddrFamilyEnum": AddrFamilyEnum,
       "LossReasonEnum": LossReasonEnum,
       "McastRouteEnum": McastRouteEnum,
       "viptela-omp": viptela_omp,
       "omp": omp,
       "ompSummaryTable": ompSummaryTable,
       "ompSummary": ompSummary,
       "ompSummaryOperstate": ompSummaryOperstate,
       "ompSummaryAdminstate": ompSummaryAdminstate,
       "ompSummaryDevicetype": ompSummaryDevicetype,
       "ompSummaryOmpuptime": ompSummaryOmpuptime,
       "ompSummaryOmpdowntime": ompSummaryOmpdowntime,
       "ompSummaryRoutesReceived": ompSummaryRoutesReceived,
       "ompSummaryRoutesInstalled": ompSummaryRoutesInstalled,
       "ompSummaryRoutesSent": ompSummaryRoutesSent,
       "ompSummaryTlocsReceived": ompSummaryTlocsReceived,
       "ompSummaryTlocsInstalled": ompSummaryTlocsInstalled,
       "ompSummaryTlocsSent": ompSummaryTlocsSent,
       "ompSummaryServicesReceived": ompSummaryServicesReceived,
       "ompSummaryServicesInstalled": ompSummaryServicesInstalled,
       "ompSummaryServicesSent": ompSummaryServicesSent,
       "ompSummaryMcastRoutesReceived": ompSummaryMcastRoutesReceived,
       "ompSummaryMcastRoutesInstalled": ompSummaryMcastRoutesInstalled,
       "ompSummaryMcastRoutesSent": ompSummaryMcastRoutesSent,
       "ompSummaryHelloReceived": ompSummaryHelloReceived,
       "ompSummaryHelloSent": ompSummaryHelloSent,
       "ompSummaryHandshakeReceived": ompSummaryHandshakeReceived,
       "ompSummaryHandshakeSent": ompSummaryHandshakeSent,
       "ompSummaryAlertReceived": ompSummaryAlertReceived,
       "ompSummaryAlertSent": ompSummaryAlertSent,
       "ompSummaryInformReceived": ompSummaryInformReceived,
       "ompSummaryInformSent": ompSummaryInformSent,
       "ompSummaryUpdateReceived": ompSummaryUpdateReceived,
       "ompSummaryUpdateSent": ompSummaryUpdateSent,
       "ompSummaryPolicyReceived": ompSummaryPolicyReceived,
       "ompSummaryPolicySent": ompSummaryPolicySent,
       "ompSummaryPacketsReceived": ompSummaryPacketsReceived,
       "ompSummaryPacketsSent": ompSummaryPacketsSent,
       "ompSummaryVsmartPeers": ompSummaryVsmartPeers,
       "ompSummaryVedgePeers": ompSummaryVedgePeers,
       "ompSummaryPolicyQueue": ompSummaryPolicyQueue,
       "ompSummaryPeersTable": ompSummaryPeersTable,
       "ompSummaryPeersEntry": ompSummaryPeersEntry,
       "ompSummaryPeersPeer": ompSummaryPeersPeer,
       "ompSummaryPeersType": ompSummaryPeersType,
       "ompSummaryPeersDomainId": ompSummaryPeersDomainId,
       "ompSummaryPeersSiteId": ompSummaryPeersSiteId,
       "ompSummaryPeersState": ompSummaryPeersState,
       "ompSummaryPeersVersion": ompSummaryPeersVersion,
       "ompSummaryPeersLegit": ompSummaryPeersLegit,
       "ompSummaryPeersUpcount": ompSummaryPeersUpcount,
       "ompSummaryPeersDowncount": ompSummaryPeersDowncount,
       "ompSummaryPeersLastuptime": ompSummaryPeersLastuptime,
       "ompSummaryPeersLastdowntime": ompSummaryPeersLastdowntime,
       "ompSummaryPeersUpTime": ompSummaryPeersUpTime,
       "ompSummaryPeersDownTime": ompSummaryPeersDownTime,
       "ompSummaryPeersHoldtime": ompSummaryPeersHoldtime,
       "ompSummaryPeersSitepolicy": ompSummaryPeersSitepolicy,
       "ompSummaryPeersPolicyin": ompSummaryPeersPolicyin,
       "ompSummaryPeersPolicyout": ompSummaryPeersPolicyout,
       "ompSummaryPeersGracefulRestart": ompSummaryPeersGracefulRestart,
       "ompSummaryPeersGracefulRestartInterval": ompSummaryPeersGracefulRestartInterval,
       "ompSummaryPeersHelloReceived": ompSummaryPeersHelloReceived,
       "ompSummaryPeersHelloSent": ompSummaryPeersHelloSent,
       "ompSummaryPeersHandshakeReceived": ompSummaryPeersHandshakeReceived,
       "ompSummaryPeersHandshakeSent": ompSummaryPeersHandshakeSent,
       "ompSummaryPeersAlertReceived": ompSummaryPeersAlertReceived,
       "ompSummaryPeersAlertSent": ompSummaryPeersAlertSent,
       "ompSummaryPeersInformReceived": ompSummaryPeersInformReceived,
       "ompSummaryPeersInformSent": ompSummaryPeersInformSent,
       "ompSummaryPeersUpdateReceived": ompSummaryPeersUpdateReceived,
       "ompSummaryPeersUpdateSent": ompSummaryPeersUpdateSent,
       "ompSummaryPeersPolicyReceived": ompSummaryPeersPolicyReceived,
       "ompSummaryPeersPolicySent": ompSummaryPeersPolicySent,
       "ompSummaryPeersPacketsReceived": ompSummaryPeersPacketsReceived,
       "ompSummaryPeersPacketsSent": ompSummaryPeersPacketsSent,
       "ompSummaryPeersRoutesReceived": ompSummaryPeersRoutesReceived,
       "ompSummaryPeersRoutesInstalled": ompSummaryPeersRoutesInstalled,
       "ompSummaryPeersRoutesSent": ompSummaryPeersRoutesSent,
       "ompSummaryPeersTlocsReceived": ompSummaryPeersTlocsReceived,
       "ompSummaryPeersTlocsInstalled": ompSummaryPeersTlocsInstalled,
       "ompSummaryPeersTlocsSent": ompSummaryPeersTlocsSent,
       "ompSummaryPeersServicesReceived": ompSummaryPeersServicesReceived,
       "ompSummaryPeersServicesInstalled": ompSummaryPeersServicesInstalled,
       "ompSummaryPeersServicesSent": ompSummaryPeersServicesSent,
       "ompSummaryPeersMcastRoutesReceived": ompSummaryPeersMcastRoutesReceived,
       "ompSummaryPeersMcastRoutesInstalled": ompSummaryPeersMcastRoutesInstalled,
       "ompSummaryPeersMcastRoutesSent": ompSummaryPeersMcastRoutesSent,
       "ompSummaryPeersControlUp": ompSummaryPeersControlUp,
       "ompSummaryPeersStaging": ompSummaryPeersStaging,
       "ompSummaryPeersRefresh": ompSummaryPeersRefresh,
       "ompSummaryPeersOverlayId": ompSummaryPeersOverlayId,
       "ompSummaryPeersRoutesReceivedIPv6": ompSummaryPeersRoutesReceivedIPv6,
       "ompSummaryPeersRoutesInstalledIPv6": ompSummaryPeersRoutesInstalledIPv6,
       "ompSummaryPeersRoutesSentIPv6": ompSummaryPeersRoutesSentIPv6,
       "ompSummaryPeersRoutesReceivedTotal": ompSummaryPeersRoutesReceivedTotal,
       "ompSummaryPeersRoutesInstalledTotal": ompSummaryPeersRoutesInstalledTotal,
       "ompSummaryPeersRoutesSentTotal": ompSummaryPeersRoutesSentTotal,
       "ompSummaryPeersServicesReceivedIPv6": ompSummaryPeersServicesReceivedIPv6,
       "ompSummaryPeersServicesInstalledIPv6": ompSummaryPeersServicesInstalledIPv6,
       "ompSummaryPeersServicesSentIPv6": ompSummaryPeersServicesSentIPv6,
       "ompRoutesTable": ompRoutesTable,
       "ompRoutesTableFamilyTable": ompRoutesTableFamilyTable,
       "ompRoutesTableFamilyEntry": ompRoutesTableFamilyEntry,
       "ompRoutesTableFamilyAddressFamily": ompRoutesTableFamilyAddressFamily,
       "ompRoutesTableFamilyEntriesTable": ompRoutesTableFamilyEntriesTable,
       "ompRoutesTableFamilyEntriesEntry": ompRoutesTableFamilyEntriesEntry,
       "ompRoutesTableFamilyEntriesVpnId": ompRoutesTableFamilyEntriesVpnId,
       "ompRoutesTableFamilyEntriesPrefix": ompRoutesTableFamilyEntriesPrefix,
       "ompRoutesTableFamilyEntriesReceivedTable": ompRoutesTableFamilyEntriesReceivedTable,
       "ompRoutesTableFamilyEntriesReceivedEntry": ompRoutesTableFamilyEntriesReceivedEntry,
       "ompRoutesTableFamilyEntriesReceivedFromPeer": ompRoutesTableFamilyEntriesReceivedFromPeer,
       "ompRoutesTableFamilyEntriesReceivedPathId": ompRoutesTableFamilyEntriesReceivedPathId,
       "ompRoutesTableFamilyEntriesReceivedLabel": ompRoutesTableFamilyEntriesReceivedLabel,
       "ompRoutesTableFamilyEntriesReceivedStatus": ompRoutesTableFamilyEntriesReceivedStatus,
       "ompRoutesTableFamilyEntriesReceivedLossReason": ompRoutesTableFamilyEntriesReceivedLossReason,
       "ompRoutesTableFamilyEntriesReceivedLostToPeer": ompRoutesTableFamilyEntriesReceivedLostToPeer,
       "ompRoutesTableFamilyEntriesReceivedLostToPathId": ompRoutesTableFamilyEntriesReceivedLostToPathId,
       "ompRoutesTableFamilyEntriesReceivedAttributesTable": ompRoutesTableFamilyEntriesReceivedAttributesTable,
       "ompRoutesTableFamilyEntriesReceivedAttributesEntry": ompRoutesTableFamilyEntriesReceivedAttributesEntry,
       "ompRoutesTableFamilyEntriesReceivedAttributesAttributeType": ompRoutesTableFamilyEntriesReceivedAttributesAttributeType,
       "ompRoutesTableFamilyEntriesReceivedAttributesTlocIp": ompRoutesTableFamilyEntriesReceivedAttributesTlocIp,
       "ompRoutesTableFamilyEntriesReceivedAttributesTlocColor": ompRoutesTableFamilyEntriesReceivedAttributesTlocColor,
       "ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap": ompRoutesTableFamilyEntriesReceivedAttributesTlocEncap,
       "ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol": ompRoutesTableFamilyEntriesReceivedAttributesOriginProtocol,
       "ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric": ompRoutesTableFamilyEntriesReceivedAttributesOriginMetric,
       "ompRoutesTableFamilyEntriesReceivedAttributesDomainId": ompRoutesTableFamilyEntriesReceivedAttributesDomainId,
       "ompRoutesTableFamilyEntriesReceivedAttributesSiteId": ompRoutesTableFamilyEntriesReceivedAttributesSiteId,
       "ompRoutesTableFamilyEntriesReceivedAttributesPreference": ompRoutesTableFamilyEntriesReceivedAttributesPreference,
       "ompRoutesTableFamilyEntriesReceivedAttributesTag": ompRoutesTableFamilyEntriesReceivedAttributesTag,
       "ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen": ompRoutesTableFamilyEntriesReceivedAttributesUnknownAttributeLen,
       "ompRoutesTableFamilyEntriesReceivedAttributesOriginator": ompRoutesTableFamilyEntriesReceivedAttributesOriginator,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocIp,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocColor,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocEncap,
       "ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction": ompRoutesTableFamilyEntriesReceivedAttributesUltimateTlocAction,
       "ompRoutesTableFamilyEntriesReceivedAttributesOverlayId": ompRoutesTableFamilyEntriesReceivedAttributesOverlayId,
       "ompRoutesTableFamilyEntriesReceivedAttributesAsPath": ompRoutesTableFamilyEntriesReceivedAttributesAsPath,
       "ompRoutesTableFamilyEntriesReceivedAttributesCommunity": ompRoutesTableFamilyEntriesReceivedAttributesCommunity,
       "ompRoutesTableFamilyEntriesAdvertisedTable": ompRoutesTableFamilyEntriesAdvertisedTable,
       "ompRoutesTableFamilyEntriesAdvertisedEntry": ompRoutesTableFamilyEntriesAdvertisedEntry,
       "ompRoutesTableFamilyEntriesAdvertisedToPeer": ompRoutesTableFamilyEntriesAdvertisedToPeer,
       "ompRoutesTableFamilyEntriesAdvertisedPathsTable": ompRoutesTableFamilyEntriesAdvertisedPathsTable,
       "ompRoutesTableFamilyEntriesAdvertisedPathsEntry": ompRoutesTableFamilyEntriesAdvertisedPathsEntry,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId": ompRoutesTableFamilyEntriesAdvertisedPathsAdvertiseId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTable,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesEntry,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPathId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesLabel,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocIp,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocColor,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTlocEncap,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto": ompRoutesTableFamilyEntriesAdvertisedPathsAttrbOrgProto,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginMetric,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesDomainId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesSiteId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesPreference,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesTag,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen": ompRoutesTableFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOriginator,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocIp,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocColor,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocEncap,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction": ompRoutesTableFamilyEntriesAdvertisedPathsAttrUltTlocAction,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesOverlayId,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesAsPath,
       "ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity": ompRoutesTableFamilyEntriesAdvertisedPathsAttributesCommunity,
       "ompBestMatchRoute": ompBestMatchRoute,
       "ompBestMatchRouteFamilyTable": ompBestMatchRouteFamilyTable,
       "ompBestMatchRouteFamilyEntry": ompBestMatchRouteFamilyEntry,
       "ompBestMatchRouteFamilyAddressFamily": ompBestMatchRouteFamilyAddressFamily,
       "ompBestMatchRouteFamilyEntriesTable": ompBestMatchRouteFamilyEntriesTable,
       "ompBestMatchRouteFamilyEntriesEntry": ompBestMatchRouteFamilyEntriesEntry,
       "ompBestMatchRouteFamilyEntriesVpnId": ompBestMatchRouteFamilyEntriesVpnId,
       "ompBestMatchRouteFamilyEntriesRouteAddr": ompBestMatchRouteFamilyEntriesRouteAddr,
       "ompBestMatchRouteFamilyEntriesPrefix": ompBestMatchRouteFamilyEntriesPrefix,
       "ompBestMatchRouteFamilyEntriesReceivedTable": ompBestMatchRouteFamilyEntriesReceivedTable,
       "ompBestMatchRouteFamilyEntriesReceivedEntry": ompBestMatchRouteFamilyEntriesReceivedEntry,
       "ompBestMatchRouteFamilyEntriesReceivedFromPeer": ompBestMatchRouteFamilyEntriesReceivedFromPeer,
       "ompBestMatchRouteFamilyEntriesReceivedPathId": ompBestMatchRouteFamilyEntriesReceivedPathId,
       "ompBestMatchRouteFamilyEntriesReceivedLabel": ompBestMatchRouteFamilyEntriesReceivedLabel,
       "ompBestMatchRouteFamilyEntriesReceivedStatus": ompBestMatchRouteFamilyEntriesReceivedStatus,
       "ompBestMatchRouteFamilyEntriesReceivedLossReason": ompBestMatchRouteFamilyEntriesReceivedLossReason,
       "ompBestMatchRouteFamilyEntriesReceivedLostToPeer": ompBestMatchRouteFamilyEntriesReceivedLostToPeer,
       "ompBestMatchRouteFamilyEntriesReceivedLostToPathId": ompBestMatchRouteFamilyEntriesReceivedLostToPathId,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesTable": ompBestMatchRouteFamilyEntriesReceivedAttributesTable,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesEntry": ompBestMatchRouteFamilyEntriesReceivedAttributesEntry,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey": ompBestMatchRouteFamilyEntriesReceivedAttributesPseudoKey,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesAttributeType": ompBestMatchRouteFamilyEntriesReceivedAttributesAttributeType,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesTlocIp": ompBestMatchRouteFamilyEntriesReceivedAttributesTlocIp,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesTlocColor": ompBestMatchRouteFamilyEntriesReceivedAttributesTlocColor,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap": ompBestMatchRouteFamilyEntriesReceivedAttributesTlocEncap,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol": ompBestMatchRouteFamilyEntriesReceivedAttributesOriginProtocol,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric": ompBestMatchRouteFamilyEntriesReceivedAttributesOriginMetric,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesDomainId": ompBestMatchRouteFamilyEntriesReceivedAttributesDomainId,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesSiteId": ompBestMatchRouteFamilyEntriesReceivedAttributesSiteId,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesPreference": ompBestMatchRouteFamilyEntriesReceivedAttributesPreference,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesTag": ompBestMatchRouteFamilyEntriesReceivedAttributesTag,
       "ompBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen": ompBestMatchRouteFamilyEntriesReceivedAttrbUnkAttrbLen,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesOriginator": ompBestMatchRouteFamilyEntriesReceivedAttributesOriginator,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesOverlayId": ompBestMatchRouteFamilyEntriesReceivedAttributesOverlayId,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesAsPath": ompBestMatchRouteFamilyEntriesReceivedAttributesAsPath,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesCommunity": ompBestMatchRouteFamilyEntriesReceivedAttributesCommunity,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp": ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocIp,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor": ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocColor,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap": ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocEncap,
       "ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction": ompBestMatchRouteFamilyEntriesReceivedAttributesUltimateTlocAction,
       "ompBestMatchRouteFamilyEntriesAdvertisedTable": ompBestMatchRouteFamilyEntriesAdvertisedTable,
       "ompBestMatchRouteFamilyEntriesAdvertisedEntry": ompBestMatchRouteFamilyEntriesAdvertisedEntry,
       "ompBestMatchRouteFamilyEntriesAdvertisedToPeer": ompBestMatchRouteFamilyEntriesAdvertisedToPeer,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsTable": ompBestMatchRouteFamilyEntriesAdvertisedPathsTable,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsEntry": ompBestMatchRouteFamilyEntriesAdvertisedPathsEntry,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId": ompBestMatchRouteFamilyEntriesAdvertisedPathsAdvertiseId,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTable": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTable,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesEntry": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesEntry,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesPathId,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesLabel,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocIp,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocColor,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTlocEncap,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgProto,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOrgMet,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesDomainId,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesSiteId,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbPref,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesTag,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbUnkAttrbLen,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttrbOriginator,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesOverlayId,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesAsPath,
       "ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity": ompBestMatchRouteFamilyEntriesAdvertisedPathsAttributesCommunity,
       "ompTlocPaths": ompTlocPaths,
       "ompTlocPathsEntriesTable": ompTlocPathsEntriesTable,
       "ompTlocPathsEntriesEntry": ompTlocPathsEntriesEntry,
       "ompTlocPathsEntriesIp": ompTlocPathsEntriesIp,
       "ompTlocPathsEntriesColor": ompTlocPathsEntriesColor,
       "ompTlocPathsEntriesEncap": ompTlocPathsEntriesEncap,
       "ompTlocPathsEntriesPathsTable": ompTlocPathsEntriesPathsTable,
       "ompTlocPathsEntriesPathsEntry": ompTlocPathsEntriesPathsEntry,
       "ompTlocPathsEntriesPathsIndex": ompTlocPathsEntriesPathsIndex,
       "ompTlocPathsEntriesPathsPreference": ompTlocPathsEntriesPathsPreference,
       "ompTlocPathsEntriesPathsMtu": ompTlocPathsEntriesPathsMtu,
       "ompTlocPathsEntriesPathsBfdStatus": ompTlocPathsEntriesPathsBfdStatus,
       "ompTlocPathsEntriesPathsStatus": ompTlocPathsEntriesPathsStatus,
       "ompTlocPathsEntriesPathsStale": ompTlocPathsEntriesPathsStale,
       "ompTlocPathsEntriesPathsLinksTable": ompTlocPathsEntriesPathsLinksTable,
       "ompTlocPathsEntriesPathsLinksEntry": ompTlocPathsEntriesPathsLinksEntry,
       "ompTlocPathsEntriesPathsLinksLinkIndex": ompTlocPathsEntriesPathsLinksLinkIndex,
       "ompTlocPathsEntriesPathsLinksFromTlocIp": ompTlocPathsEntriesPathsLinksFromTlocIp,
       "ompTlocPathsEntriesPathsLinksFromTlocColor": ompTlocPathsEntriesPathsLinksFromTlocColor,
       "ompTlocPathsEntriesPathsLinksFromTlocEncap": ompTlocPathsEntriesPathsLinksFromTlocEncap,
       "ompTlocPathsEntriesPathsLinksToTlocIp": ompTlocPathsEntriesPathsLinksToTlocIp,
       "ompTlocPathsEntriesPathsLinksToTlocColor": ompTlocPathsEntriesPathsLinksToTlocColor,
       "ompTlocPathsEntriesPathsLinksToTlocEncap": ompTlocPathsEntriesPathsLinksToTlocEncap,
       "ompTlocPathsEntriesPathsLinksLabel": ompTlocPathsEntriesPathsLinksLabel,
       "ompTlocs": ompTlocs,
       "ompTlocsFamilyTable": ompTlocsFamilyTable,
       "ompTlocsFamilyEntry": ompTlocsFamilyEntry,
       "ompTlocsFamilyAddressFamily": ompTlocsFamilyAddressFamily,
       "ompTlocsFamilyEntriesTable": ompTlocsFamilyEntriesTable,
       "ompTlocsFamilyEntriesEntry": ompTlocsFamilyEntriesEntry,
       "ompTlocsFamilyEntriesIp": ompTlocsFamilyEntriesIp,
       "ompTlocsFamilyEntriesColor": ompTlocsFamilyEntriesColor,
       "ompTlocsFamilyEntriesEncap": ompTlocsFamilyEntriesEncap,
       "ompTlocsFamilyEntriesReceivedTable": ompTlocsFamilyEntriesReceivedTable,
       "ompTlocsFamilyEntriesReceivedEntry": ompTlocsFamilyEntriesReceivedEntry,
       "ompTlocsFamilyEntriesReceivedFromPeer": ompTlocsFamilyEntriesReceivedFromPeer,
       "ompTlocsFamilyEntriesReceivedStatus": ompTlocsFamilyEntriesReceivedStatus,
       "ompTlocsFamilyEntriesReceivedLossReason": ompTlocsFamilyEntriesReceivedLossReason,
       "ompTlocsFamilyEntriesReceivedLostToPeer": ompTlocsFamilyEntriesReceivedLostToPeer,
       "ompTlocsFamilyEntriesReceivedLostToPathId": ompTlocsFamilyEntriesReceivedLostToPathId,
       "ompTlocsFamilyEntriesReceivedAttributesTable": ompTlocsFamilyEntriesReceivedAttributesTable,
       "ompTlocsFamilyEntriesReceivedAttributesEntry": ompTlocsFamilyEntriesReceivedAttributesEntry,
       "ompTlocsFamilyEntriesReceivedAttributesPseudoKey": ompTlocsFamilyEntriesReceivedAttributesPseudoKey,
       "ompTlocsFamilyEntriesReceivedAttributesAttributeType": ompTlocsFamilyEntriesReceivedAttributesAttributeType,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey": ompTlocsFamilyEntriesReceivedAttributesTlocEncapKey,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto": ompTlocsFamilyEntriesReceivedAttributesTlocEncapProto,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi": ompTlocsFamilyEntriesReceivedAttributesTlocEncapSpi,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType": ompTlocsFamilyEntriesReceivedAttributesTlocEncapAuthType,
       "ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType": ompTlocsFamilyEntriesReceivedAttributesTlocEncapEncryptType,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort": ompTlocsFamilyEntriesReceivedAttributesTlocMapPublicPort,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivateIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort": ompTlocsFamilyEntriesReceivedAttributesTlocMapPrivatePort,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PublicPort,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivateIp,
       "ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort": ompTlocsFamilyEntriesReceivedAttributesTlocMapV6PrivatePort,
       "ompTlocsFamilyEntriesReceivedAttributesBfdStatus": ompTlocsFamilyEntriesReceivedAttributesBfdStatus,
       "ompTlocsFamilyEntriesReceivedAttributesDomainId": ompTlocsFamilyEntriesReceivedAttributesDomainId,
       "ompTlocsFamilyEntriesReceivedAttributesSiteId": ompTlocsFamilyEntriesReceivedAttributesSiteId,
       "ompTlocsFamilyEntriesReceivedAttributesPreference": ompTlocsFamilyEntriesReceivedAttributesPreference,
       "ompTlocsFamilyEntriesReceivedAttributesTag": ompTlocsFamilyEntriesReceivedAttributesTag,
       "ompTlocsFamilyEntriesReceivedAttributesStale": ompTlocsFamilyEntriesReceivedAttributesStale,
       "ompTlocsFamilyEntriesReceivedAttributesCarrier": ompTlocsFamilyEntriesReceivedAttributesCarrier,
       "ompTlocsFamilyEntriesReceivedAttributesGroups": ompTlocsFamilyEntriesReceivedAttributesGroups,
       "ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen": ompTlocsFamilyEntriesReceivedAttributesUnknownAttributeLen,
       "ompTlocsFamilyEntriesReceivedAttributesWeight": ompTlocsFamilyEntriesReceivedAttributesWeight,
       "ompTlocsFamilyEntriesReceivedAttributesGenId": ompTlocsFamilyEntriesReceivedAttributesGenId,
       "ompTlocsFamilyEntriesReceivedAttributesVersion": ompTlocsFamilyEntriesReceivedAttributesVersion,
       "ompTlocsFamilyEntriesReceivedAttributesOriginator": ompTlocsFamilyEntriesReceivedAttributesOriginator,
       "ompTlocsFamilyEntriesReceivedAttributesRestrict": ompTlocsFamilyEntriesReceivedAttributesRestrict,
       "ompTlocsFamilyEntriesReceivedAttributesOverlayId": ompTlocsFamilyEntriesReceivedAttributesOverlayId,
       "ompTlocsFamilyEntriesReceivedAttributesBandwidth": ompTlocsFamilyEntriesReceivedAttributesBandwidth,
       "ompTlocsFamilyEntriesReceivedAttributesQosGroup": ompTlocsFamilyEntriesReceivedAttributesQosGroup,
       "ompTlocsFamilyEntriesReceivedAttributesOnDemand": ompTlocsFamilyEntriesReceivedAttributesOnDemand,
       "ompTlocsFamilyEntriesAdvertisedTable": ompTlocsFamilyEntriesAdvertisedTable,
       "ompTlocsFamilyEntriesAdvertisedEntry": ompTlocsFamilyEntriesAdvertisedEntry,
       "ompTlocsFamilyEntriesAdvertisedToPeer": ompTlocsFamilyEntriesAdvertisedToPeer,
       "ompTlocsFamilyEntriesAdvertisedAttributesTable": ompTlocsFamilyEntriesAdvertisedAttributesTable,
       "ompTlocsFamilyEntriesAdvertisedAttributesEntry": ompTlocsFamilyEntriesAdvertisedAttributesEntry,
       "ompTlocsFamilyEntriesAdvertisedAttributesAttributeId": ompTlocsFamilyEntriesAdvertisedAttributesAttributeId,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapKey,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapProto,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapSpi,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapAuthType,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType": ompTlocsFamilyEntriesAdvertisedAttributesTlocEncapEncryptType,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPublicPort,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivateIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapPrivatePort,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PublicPort,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivateIp,
       "ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort": ompTlocsFamilyEntriesAdvertisedAttributesTlocMapV6PrivatePort,
       "ompTlocsFamilyEntriesAdvertisedAttributesDomainId": ompTlocsFamilyEntriesAdvertisedAttributesDomainId,
       "ompTlocsFamilyEntriesAdvertisedAttributesSiteId": ompTlocsFamilyEntriesAdvertisedAttributesSiteId,
       "ompTlocsFamilyEntriesAdvertisedAttributesPreference": ompTlocsFamilyEntriesAdvertisedAttributesPreference,
       "ompTlocsFamilyEntriesAdvertisedAttributesTag": ompTlocsFamilyEntriesAdvertisedAttributesTag,
       "ompTlocsFamilyEntriesAdvertisedAttributesStale": ompTlocsFamilyEntriesAdvertisedAttributesStale,
       "ompTlocsFamilyEntriesAdvertisedAttributesCarrier": ompTlocsFamilyEntriesAdvertisedAttributesCarrier,
       "ompTlocsFamilyEntriesAdvertisedAttributesGroups": ompTlocsFamilyEntriesAdvertisedAttributesGroups,
       "ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen": ompTlocsFamilyEntriesAdvertisedAttributesUnknownAttributeLen,
       "ompTlocsFamilyEntriesAdvertisedAttributesWeight": ompTlocsFamilyEntriesAdvertisedAttributesWeight,
       "ompTlocsFamilyEntriesAdvertisedAttributesGenId": ompTlocsFamilyEntriesAdvertisedAttributesGenId,
       "ompTlocsFamilyEntriesAdvertisedAttributesVersion": ompTlocsFamilyEntriesAdvertisedAttributesVersion,
       "ompTlocsFamilyEntriesAdvertisedAttributesOriginator": ompTlocsFamilyEntriesAdvertisedAttributesOriginator,
       "ompTlocsFamilyEntriesAdvertisedAttributesRestrict": ompTlocsFamilyEntriesAdvertisedAttributesRestrict,
       "ompTlocsFamilyEntriesAdvertisedAttributesOverlayId": ompTlocsFamilyEntriesAdvertisedAttributesOverlayId,
       "ompTlocsFamilyEntriesAdvertisedAttributesBandwidth": ompTlocsFamilyEntriesAdvertisedAttributesBandwidth,
       "ompTlocsFamilyEntriesAdvertisedAttributesQosGroup": ompTlocsFamilyEntriesAdvertisedAttributesQosGroup,
       "ompTlocsFamilyEntriesAdvertisedAttributesOnDemand": ompTlocsFamilyEntriesAdvertisedAttributesOnDemand,
       "ompServices": ompServices,
       "ompServicesFamilyTable": ompServicesFamilyTable,
       "ompServicesFamilyEntry": ompServicesFamilyEntry,
       "ompServicesFamilyAddressFamily": ompServicesFamilyAddressFamily,
       "ompServicesFamilyEntriesTable": ompServicesFamilyEntriesTable,
       "ompServicesFamilyEntriesEntry": ompServicesFamilyEntriesEntry,
       "ompServicesFamilyEntriesVpnId": ompServicesFamilyEntriesVpnId,
       "ompServicesFamilyEntriesService": ompServicesFamilyEntriesService,
       "ompServicesFamilyEntriesOriginator": ompServicesFamilyEntriesOriginator,
       "ompServicesFamilyEntriesReceivedTable": ompServicesFamilyEntriesReceivedTable,
       "ompServicesFamilyEntriesReceivedEntry": ompServicesFamilyEntriesReceivedEntry,
       "ompServicesFamilyEntriesReceivedFromPeer": ompServicesFamilyEntriesReceivedFromPeer,
       "ompServicesFamilyEntriesReceivedPathId": ompServicesFamilyEntriesReceivedPathId,
       "ompServicesFamilyEntriesReceivedLabel": ompServicesFamilyEntriesReceivedLabel,
       "ompServicesFamilyEntriesReceivedStatus": ompServicesFamilyEntriesReceivedStatus,
       "ompServicesFamilyEntriesReceivedLossReason": ompServicesFamilyEntriesReceivedLossReason,
       "ompServicesFamilyEntriesReceivedLostToPeer": ompServicesFamilyEntriesReceivedLostToPeer,
       "ompServicesFamilyEntriesReceivedLostToPathId": ompServicesFamilyEntriesReceivedLostToPathId,
       "ompServicesFamilyEntriesAdvertisedTable": ompServicesFamilyEntriesAdvertisedTable,
       "ompServicesFamilyEntriesAdvertisedEntry": ompServicesFamilyEntriesAdvertisedEntry,
       "ompServicesFamilyEntriesAdvertisedToPeer": ompServicesFamilyEntriesAdvertisedToPeer,
       "ompMulticastAutoDiscover": ompMulticastAutoDiscover,
       "ompMulticastAutoDiscoverFamilyTable": ompMulticastAutoDiscoverFamilyTable,
       "ompMulticastAutoDiscoverFamilyEntry": ompMulticastAutoDiscoverFamilyEntry,
       "ompMulticastAutoDiscoverFamilyAddressFamily": ompMulticastAutoDiscoverFamilyAddressFamily,
       "ompMulticastAutoDiscoverFamilyEntriesTable": ompMulticastAutoDiscoverFamilyEntriesTable,
       "ompMulticastAutoDiscoverFamilyEntriesEntry": ompMulticastAutoDiscoverFamilyEntriesEntry,
       "ompMulticastAutoDiscoverFamilyEntriesVpnId": ompMulticastAutoDiscoverFamilyEntriesVpnId,
       "ompMulticastAutoDiscoverFamilyEntriesSourceOriginator": ompMulticastAutoDiscoverFamilyEntriesSourceOriginator,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedTable": ompMulticastAutoDiscoverFamilyEntriesReceivedTable,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedEntry": ompMulticastAutoDiscoverFamilyEntriesReceivedEntry,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer": ompMulticastAutoDiscoverFamilyEntriesReceivedFromPeer,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedStatus": ompMulticastAutoDiscoverFamilyEntriesReceivedStatus,
       "ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason": ompMulticastAutoDiscoverFamilyEntriesReceivedLossReason,
       "ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable": ompMulticastAutoDiscoverFamilyEntriesAdvertisedTable,
       "ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry": ompMulticastAutoDiscoverFamilyEntriesAdvertisedEntry,
       "ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer": ompMulticastAutoDiscoverFamilyEntriesAdvertisedToPeer,
       "ompMulticastRoutes": ompMulticastRoutes,
       "ompMulticastRoutesFamilyTable": ompMulticastRoutesFamilyTable,
       "ompMulticastRoutesFamilyEntry": ompMulticastRoutesFamilyEntry,
       "ompMulticastRoutesFamilyAddressFamily": ompMulticastRoutesFamilyAddressFamily,
       "ompMulticastRoutesFamilyEntriesTable": ompMulticastRoutesFamilyEntriesTable,
       "ompMulticastRoutesFamilyEntriesEntry": ompMulticastRoutesFamilyEntriesEntry,
       "ompMulticastRoutesFamilyEntriesType": ompMulticastRoutesFamilyEntriesType,
       "ompMulticastRoutesFamilyEntriesVpnId": ompMulticastRoutesFamilyEntriesVpnId,
       "ompMulticastRoutesFamilyEntriesSourceOriginator": ompMulticastRoutesFamilyEntriesSourceOriginator,
       "ompMulticastRoutesFamilyEntriesDestination": ompMulticastRoutesFamilyEntriesDestination,
       "ompMulticastRoutesFamilyEntriesGroup": ompMulticastRoutesFamilyEntriesGroup,
       "ompMulticastRoutesFamilyEntriesSource": ompMulticastRoutesFamilyEntriesSource,
       "ompMulticastRoutesFamilyEntriesReceivedTable": ompMulticastRoutesFamilyEntriesReceivedTable,
       "ompMulticastRoutesFamilyEntriesReceivedEntry": ompMulticastRoutesFamilyEntriesReceivedEntry,
       "ompMulticastRoutesFamilyEntriesReceivedFromPeer": ompMulticastRoutesFamilyEntriesReceivedFromPeer,
       "ompMulticastRoutesFamilyEntriesReceivedRp": ompMulticastRoutesFamilyEntriesReceivedRp,
       "ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes": ompMulticastRoutesFamilyEntriesReceivedReceivedPrunes,
       "ompMulticastRoutesFamilyEntriesReceivedStatus": ompMulticastRoutesFamilyEntriesReceivedStatus,
       "ompMulticastRoutesFamilyEntriesReceivedLossReason": ompMulticastRoutesFamilyEntriesReceivedLossReason,
       "ompMulticastRoutesFamilyEntriesAdvertisedTable": ompMulticastRoutesFamilyEntriesAdvertisedTable,
       "ompMulticastRoutesFamilyEntriesAdvertisedEntry": ompMulticastRoutesFamilyEntriesAdvertisedEntry,
       "ompMulticastRoutesFamilyEntriesAdvertisedToPeer": ompMulticastRoutesFamilyEntriesAdvertisedToPeer,
       "ompMulticastRoutesFamilyEntriesAdvertisedRp": ompMulticastRoutesFamilyEntriesAdvertisedRp,
       "ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes": ompMulticastRoutesFamilyEntriesAdvertisedAdvertisedPrunes,
       "ompCloudexpressRoutes": ompCloudexpressRoutes,
       "ompCloudexpressEntriesTable": ompCloudexpressEntriesTable,
       "ompCloudexpressEntriesEntry": ompCloudexpressEntriesEntry,
       "ompCloudexpressEntriesVpnId": ompCloudexpressEntriesVpnId,
       "ompCloudexpressEntriesOriginator": ompCloudexpressEntriesOriginator,
       "ompCloudexpressEntriesAppid": ompCloudexpressEntriesAppid,
       "ompCloudexpressEntriesAppname": ompCloudexpressEntriesAppname,
       "ompCloudexpressEntriesReceivedTable": ompCloudexpressEntriesReceivedTable,
       "ompCloudexpressEntriesReceivedEntry": ompCloudexpressEntriesReceivedEntry,
       "ompCloudexpressEntriesReceivedFromPeer": ompCloudexpressEntriesReceivedFromPeer,
       "ompCloudexpressEntriesReceivedStatus": ompCloudexpressEntriesReceivedStatus,
       "ompCloudexpressEntriesReceivedLossReason": ompCloudexpressEntriesReceivedLossReason,
       "ompCloudexpressEntriesReceivedLatency": ompCloudexpressEntriesReceivedLatency,
       "ompCloudexpressEntriesReceivedLoss": ompCloudexpressEntriesReceivedLoss,
       "ompCloudexpressEntriesAdvertisedTable": ompCloudexpressEntriesAdvertisedTable,
       "ompCloudexpressEntriesAdvertisedEntry": ompCloudexpressEntriesAdvertisedEntry,
       "ompCloudexpressEntriesAdvertisedToPeer": ompCloudexpressEntriesAdvertisedToPeer,
       "ompCloudexpressEntriesAdvertisedLatency": ompCloudexpressEntriesAdvertisedLatency,
       "ompCloudexpressEntriesAdvertisedLoss": ompCloudexpressEntriesAdvertisedLoss}
)
