# SNMP MIB module (TN-CES-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-CES-ROUTING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:48 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnCesRoutingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61)
)
if mibBuilder.loadTexts:
    tnCesRoutingMIB.setRevisions(
        ("2014-06-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnCesRoutingObjects_ObjectIdentity = ObjectIdentity
tnCesRoutingObjects = _TnCesRoutingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1)
)
_TnCesGroupTable_Object = MibTable
tnCesGroupTable = _TnCesGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1)
)
if mibBuilder.loadTexts:
    tnCesGroupTable.setStatus("current")
_TnCesGroupEntry_Object = MibTableRow
tnCesGroupEntry = _TnCesGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1, 1)
)
tnCesGroupEntry.setIndexNames(
    (0, "TN-CES-ROUTING-MIB", "tnCesGroupIndex"),
    (0, "TN-CES-ROUTING-MIB", "tnCesGroupPortNumber"),
)
if mibBuilder.loadTexts:
    tnCesGroupEntry.setStatus("current")


class _TnCesGroupIndex_Type(Unsigned32):
    """Custom type tnCesGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCesGroupIndex_Type.__name__ = "Unsigned32"
_TnCesGroupIndex_Object = MibTableColumn
tnCesGroupIndex = _TnCesGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1, 1, 1),
    _TnCesGroupIndex_Type()
)
tnCesGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesGroupIndex.setStatus("current")


class _TnCesGroupPortNumber_Type(Unsigned32):
    """Custom type tnCesGroupPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesGroupPortNumber_Type.__name__ = "Unsigned32"
_TnCesGroupPortNumber_Object = MibTableColumn
tnCesGroupPortNumber = _TnCesGroupPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1, 1, 2),
    _TnCesGroupPortNumber_Type()
)
tnCesGroupPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesGroupPortNumber.setStatus("current")


class _TnCesGroupName_Type(DisplayString):
    """Custom type tnCesGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCesGroupName_Type.__name__ = "DisplayString"
_TnCesGroupName_Object = MibTableColumn
tnCesGroupName = _TnCesGroupName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1, 1, 3),
    _TnCesGroupName_Type()
)
tnCesGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesGroupName.setStatus("current")
_TnCesGroupCyclicPortSearch_Type = TruthValue
_TnCesGroupCyclicPortSearch_Object = MibTableColumn
tnCesGroupCyclicPortSearch = _TnCesGroupCyclicPortSearch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1, 1, 4),
    _TnCesGroupCyclicPortSearch_Type()
)
tnCesGroupCyclicPortSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesGroupCyclicPortSearch.setStatus("current")
_TnCesGroupCyclicChannelSearch_Type = TruthValue
_TnCesGroupCyclicChannelSearch_Object = MibTableColumn
tnCesGroupCyclicChannelSearch = _TnCesGroupCyclicChannelSearch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1, 1, 5),
    _TnCesGroupCyclicChannelSearch_Type()
)
tnCesGroupCyclicChannelSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesGroupCyclicChannelSearch.setStatus("current")
_TnCesGroupChannels_Type = Unsigned32
_TnCesGroupChannels_Object = MibTableColumn
tnCesGroupChannels = _TnCesGroupChannels_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 1, 1, 6),
    _TnCesGroupChannels_Type()
)
tnCesGroupChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesGroupChannels.setStatus("current")
_TnCesIPNameTable_Object = MibTable
tnCesIPNameTable = _TnCesIPNameTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 2)
)
if mibBuilder.loadTexts:
    tnCesIPNameTable.setStatus("current")
_TnCesIPNameEntry_Object = MibTableRow
tnCesIPNameEntry = _TnCesIPNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 2, 1)
)
tnCesIPNameEntry.setIndexNames(
    (0, "TN-CES-ROUTING-MIB", "tnCesIPNameIndex"),
)
if mibBuilder.loadTexts:
    tnCesIPNameEntry.setStatus("current")


class _TnCesIPNameIndex_Type(Unsigned32):
    """Custom type tnCesIPNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCesIPNameIndex_Type.__name__ = "Unsigned32"
_TnCesIPNameIndex_Object = MibTableColumn
tnCesIPNameIndex = _TnCesIPNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 2, 1, 1),
    _TnCesIPNameIndex_Type()
)
tnCesIPNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesIPNameIndex.setStatus("current")


class _TnCesIPNameName_Type(DisplayString):
    """Custom type tnCesIPNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCesIPNameName_Type.__name__ = "DisplayString"
_TnCesIPNameName_Object = MibTableColumn
tnCesIPNameName = _TnCesIPNameName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 2, 1, 2),
    _TnCesIPNameName_Type()
)
tnCesIPNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesIPNameName.setStatus("current")
_TnCesIPNameIpAddrType_Type = InetAddressType
_TnCesIPNameIpAddrType_Object = MibTableColumn
tnCesIPNameIpAddrType = _TnCesIPNameIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 2, 1, 3),
    _TnCesIPNameIpAddrType_Type()
)
tnCesIPNameIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesIPNameIpAddrType.setStatus("current")
_TnCesIPNameIpAddr_Type = InetAddress
_TnCesIPNameIpAddr_Object = MibTableColumn
tnCesIPNameIpAddr = _TnCesIPNameIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 2, 1, 4),
    _TnCesIPNameIpAddr_Type()
)
tnCesIPNameIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesIPNameIpAddr.setStatus("current")
_TnCesProfileTable_Object = MibTable
tnCesProfileTable = _TnCesProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3)
)
if mibBuilder.loadTexts:
    tnCesProfileTable.setStatus("current")
_TnCesProfileEntry_Object = MibTableRow
tnCesProfileEntry = _TnCesProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1)
)
tnCesProfileEntry.setIndexNames(
    (0, "TN-CES-ROUTING-MIB", "tnCesProfileIndex"),
)
if mibBuilder.loadTexts:
    tnCesProfileEntry.setStatus("current")


class _TnCesProfileIndex_Type(Unsigned32):
    """Custom type tnCesProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TnCesProfileIndex_Type.__name__ = "Unsigned32"
_TnCesProfileIndex_Object = MibTableColumn
tnCesProfileIndex = _TnCesProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 1),
    _TnCesProfileIndex_Type()
)
tnCesProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesProfileIndex.setStatus("current")


class _TnCesProfileName_Type(DisplayString):
    """Custom type tnCesProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCesProfileName_Type.__name__ = "DisplayString"
_TnCesProfileName_Object = MibTableColumn
tnCesProfileName = _TnCesProfileName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 2),
    _TnCesProfileName_Type()
)
tnCesProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileName.setStatus("current")


class _TnCesProfileType_Type(Integer32):
    """Custom type tnCesProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("converting", 1),
          ("barring", 2),
          ("nailed", 3))
    )


_TnCesProfileType_Type.__name__ = "Integer32"
_TnCesProfileType_Object = MibTableColumn
tnCesProfileType = _TnCesProfileType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 3),
    _TnCesProfileType_Type()
)
tnCesProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileType.setStatus("current")
_TnCesProfileEnabled_Type = TruthValue
_TnCesProfileEnabled_Object = MibTableColumn
tnCesProfileEnabled = _TnCesProfileEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 4),
    _TnCesProfileEnabled_Type()
)
tnCesProfileEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileEnabled.setStatus("current")
_TnCesProfileRerouteUnanswered_Type = TruthValue
_TnCesProfileRerouteUnanswered_Object = MibTableColumn
tnCesProfileRerouteUnanswered = _TnCesProfileRerouteUnanswered_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 5),
    _TnCesProfileRerouteUnanswered_Type()
)
tnCesProfileRerouteUnanswered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileRerouteUnanswered.setStatus("current")


class _TnCesProfileRerouteUnansweredSec_Type(Unsigned32):
    """Custom type tnCesProfileRerouteUnansweredSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TnCesProfileRerouteUnansweredSec_Type.__name__ = "Unsigned32"
_TnCesProfileRerouteUnansweredSec_Object = MibTableColumn
tnCesProfileRerouteUnansweredSec = _TnCesProfileRerouteUnansweredSec_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 6),
    _TnCesProfileRerouteUnansweredSec_Type()
)
tnCesProfileRerouteUnansweredSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileRerouteUnansweredSec.setStatus("current")


class _TnCesProfileSourceEndpointType_Type(Integer32):
    """Custom type tnCesProfileSourceEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("all", 1),
          ("tdmport", 2),
          ("tdmchannel", 3),
          ("logicallink", 4),
          ("group", 5))
    )


_TnCesProfileSourceEndpointType_Type.__name__ = "Integer32"
_TnCesProfileSourceEndpointType_Object = MibTableColumn
tnCesProfileSourceEndpointType = _TnCesProfileSourceEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 7),
    _TnCesProfileSourceEndpointType_Type()
)
tnCesProfileSourceEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileSourceEndpointType.setStatus("current")
_TnCesProfileSourceItemIndex_Type = Unsigned32
_TnCesProfileSourceItemIndex_Object = MibTableColumn
tnCesProfileSourceItemIndex = _TnCesProfileSourceItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 8),
    _TnCesProfileSourceItemIndex_Type()
)
tnCesProfileSourceItemIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileSourceItemIndex.setStatus("current")


class _TnCesProfileSourceChanNumber_Type(Unsigned32):
    """Custom type tnCesProfileSourceChanNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnCesProfileSourceChanNumber_Type.__name__ = "Unsigned32"
_TnCesProfileSourceChanNumber_Object = MibTableColumn
tnCesProfileSourceChanNumber = _TnCesProfileSourceChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 9),
    _TnCesProfileSourceChanNumber_Type()
)
tnCesProfileSourceChanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileSourceChanNumber.setStatus("current")


class _TnCesProfileDestPrimEndpointType_Type(Integer32):
    """Custom type tnCesProfileDestPrimEndpointType based on Integer32"""
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
        *(("none", 0),
          ("all", 1),
          ("tdmport", 2),
          ("tdmchannel", 3),
          ("logicallink", 4),
          ("group", 5),
          ("ipname", 6))
    )


_TnCesProfileDestPrimEndpointType_Type.__name__ = "Integer32"
_TnCesProfileDestPrimEndpointType_Object = MibTableColumn
tnCesProfileDestPrimEndpointType = _TnCesProfileDestPrimEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 10),
    _TnCesProfileDestPrimEndpointType_Type()
)
tnCesProfileDestPrimEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestPrimEndpointType.setStatus("current")
_TnCesProfileDestPrimItemIndex_Type = Unsigned32
_TnCesProfileDestPrimItemIndex_Object = MibTableColumn
tnCesProfileDestPrimItemIndex = _TnCesProfileDestPrimItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 11),
    _TnCesProfileDestPrimItemIndex_Type()
)
tnCesProfileDestPrimItemIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestPrimItemIndex.setStatus("current")


class _TnCesProfileDestPrimChanNumber_Type(Unsigned32):
    """Custom type tnCesProfileDestPrimChanNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnCesProfileDestPrimChanNumber_Type.__name__ = "Unsigned32"
_TnCesProfileDestPrimChanNumber_Object = MibTableColumn
tnCesProfileDestPrimChanNumber = _TnCesProfileDestPrimChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 12),
    _TnCesProfileDestPrimChanNumber_Type()
)
tnCesProfileDestPrimChanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestPrimChanNumber.setStatus("current")


class _TnCesProfileDestSecEndpointType_Type(Integer32):
    """Custom type tnCesProfileDestSecEndpointType based on Integer32"""
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
        *(("none", 0),
          ("all", 1),
          ("tdmport", 2),
          ("tdmchannel", 3),
          ("logicallink", 4),
          ("group", 5),
          ("ipname", 6))
    )


_TnCesProfileDestSecEndpointType_Type.__name__ = "Integer32"
_TnCesProfileDestSecEndpointType_Object = MibTableColumn
tnCesProfileDestSecEndpointType = _TnCesProfileDestSecEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 13),
    _TnCesProfileDestSecEndpointType_Type()
)
tnCesProfileDestSecEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestSecEndpointType.setStatus("current")
_TnCesProfileDestSecItemIndex_Type = Unsigned32
_TnCesProfileDestSecItemIndex_Object = MibTableColumn
tnCesProfileDestSecItemIndex = _TnCesProfileDestSecItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 14),
    _TnCesProfileDestSecItemIndex_Type()
)
tnCesProfileDestSecItemIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestSecItemIndex.setStatus("current")


class _TnCesProfileDestSecChanNumber_Type(Unsigned32):
    """Custom type tnCesProfileDestSecChanNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnCesProfileDestSecChanNumber_Type.__name__ = "Unsigned32"
_TnCesProfileDestSecChanNumber_Object = MibTableColumn
tnCesProfileDestSecChanNumber = _TnCesProfileDestSecChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 15),
    _TnCesProfileDestSecChanNumber_Type()
)
tnCesProfileDestSecChanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestSecChanNumber.setStatus("current")


class _TnCesProfileDestTerEndpointType_Type(Integer32):
    """Custom type tnCesProfileDestTerEndpointType based on Integer32"""
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
        *(("none", 0),
          ("all", 1),
          ("tdmport", 2),
          ("tdmchannel", 3),
          ("logicallink", 4),
          ("group", 5),
          ("ipname", 6))
    )


_TnCesProfileDestTerEndpointType_Type.__name__ = "Integer32"
_TnCesProfileDestTerEndpointType_Object = MibTableColumn
tnCesProfileDestTerEndpointType = _TnCesProfileDestTerEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 16),
    _TnCesProfileDestTerEndpointType_Type()
)
tnCesProfileDestTerEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestTerEndpointType.setStatus("current")
_TnCesProfileDestTerItemIndex_Type = Unsigned32
_TnCesProfileDestTerItemIndex_Object = MibTableColumn
tnCesProfileDestTerItemIndex = _TnCesProfileDestTerItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 17),
    _TnCesProfileDestTerItemIndex_Type()
)
tnCesProfileDestTerItemIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestTerItemIndex.setStatus("current")


class _TnCesProfileDestTerChanNumber_Type(Unsigned32):
    """Custom type tnCesProfileDestTerChanNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnCesProfileDestTerChanNumber_Type.__name__ = "Unsigned32"
_TnCesProfileDestTerChanNumber_Object = MibTableColumn
tnCesProfileDestTerChanNumber = _TnCesProfileDestTerChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 18),
    _TnCesProfileDestTerChanNumber_Type()
)
tnCesProfileDestTerChanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileDestTerChanNumber.setStatus("current")


class _TnCesProfileVoiceConversion_Type(Integer32):
    """Custom type tnCesProfileVoiceConversion based on Integer32"""
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
          ("utoa", 1),
          ("atou", 2))
    )


_TnCesProfileVoiceConversion_Type.__name__ = "Integer32"
_TnCesProfileVoiceConversion_Object = MibTableColumn
tnCesProfileVoiceConversion = _TnCesProfileVoiceConversion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 19),
    _TnCesProfileVoiceConversion_Type()
)
tnCesProfileVoiceConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileVoiceConversion.setStatus("current")


class _TnCesProfilePrimaryCalledNumber_Type(DisplayString):
    """Custom type tnCesProfilePrimaryCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TnCesProfilePrimaryCalledNumber_Type.__name__ = "DisplayString"
_TnCesProfilePrimaryCalledNumber_Object = MibTableColumn
tnCesProfilePrimaryCalledNumber = _TnCesProfilePrimaryCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 20),
    _TnCesProfilePrimaryCalledNumber_Type()
)
tnCesProfilePrimaryCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfilePrimaryCalledNumber.setStatus("current")


class _TnCesProfilePrimaryCallingNumber_Type(DisplayString):
    """Custom type tnCesProfilePrimaryCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TnCesProfilePrimaryCallingNumber_Type.__name__ = "DisplayString"
_TnCesProfilePrimaryCallingNumber_Object = MibTableColumn
tnCesProfilePrimaryCallingNumber = _TnCesProfilePrimaryCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 21),
    _TnCesProfilePrimaryCallingNumber_Type()
)
tnCesProfilePrimaryCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfilePrimaryCallingNumber.setStatus("current")


class _TnCesProfileSecCalledNumber_Type(DisplayString):
    """Custom type tnCesProfileSecCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TnCesProfileSecCalledNumber_Type.__name__ = "DisplayString"
_TnCesProfileSecCalledNumber_Object = MibTableColumn
tnCesProfileSecCalledNumber = _TnCesProfileSecCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 22),
    _TnCesProfileSecCalledNumber_Type()
)
tnCesProfileSecCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileSecCalledNumber.setStatus("current")


class _TnCesProfileSecCallingNumber_Type(DisplayString):
    """Custom type tnCesProfileSecCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TnCesProfileSecCallingNumber_Type.__name__ = "DisplayString"
_TnCesProfileSecCallingNumber_Object = MibTableColumn
tnCesProfileSecCallingNumber = _TnCesProfileSecCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 23),
    _TnCesProfileSecCallingNumber_Type()
)
tnCesProfileSecCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileSecCallingNumber.setStatus("current")


class _TnCesProfileTerCalledNumber_Type(DisplayString):
    """Custom type tnCesProfileTerCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TnCesProfileTerCalledNumber_Type.__name__ = "DisplayString"
_TnCesProfileTerCalledNumber_Object = MibTableColumn
tnCesProfileTerCalledNumber = _TnCesProfileTerCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 24),
    _TnCesProfileTerCalledNumber_Type()
)
tnCesProfileTerCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileTerCalledNumber.setStatus("current")


class _TnCesProfileTerCallingNumber_Type(DisplayString):
    """Custom type tnCesProfileTerCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TnCesProfileTerCallingNumber_Type.__name__ = "DisplayString"
_TnCesProfileTerCallingNumber_Object = MibTableColumn
tnCesProfileTerCallingNumber = _TnCesProfileTerCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 3, 1, 25),
    _TnCesProfileTerCallingNumber_Type()
)
tnCesProfileTerCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfileTerCallingNumber.setStatus("current")
_TnCesProfCalledNumTable_Object = MibTable
tnCesProfCalledNumTable = _TnCesProfCalledNumTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 4)
)
if mibBuilder.loadTexts:
    tnCesProfCalledNumTable.setStatus("current")
_TnCesProfCalledNumEntry_Object = MibTableRow
tnCesProfCalledNumEntry = _TnCesProfCalledNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 4, 1)
)
tnCesProfCalledNumEntry.setIndexNames(
    (0, "TN-CES-ROUTING-MIB", "tnCesProfCalledNumProfileIndex"),
)
if mibBuilder.loadTexts:
    tnCesProfCalledNumEntry.setStatus("current")


class _TnCesProfCalledNumProfileIndex_Type(Unsigned32):
    """Custom type tnCesProfCalledNumProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TnCesProfCalledNumProfileIndex_Type.__name__ = "Unsigned32"
_TnCesProfCalledNumProfileIndex_Object = MibTableColumn
tnCesProfCalledNumProfileIndex = _TnCesProfCalledNumProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 4, 1, 1),
    _TnCesProfCalledNumProfileIndex_Type()
)
tnCesProfCalledNumProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesProfCalledNumProfileIndex.setStatus("current")
_TnCesProfCalledNumValue_Type = OctetString
_TnCesProfCalledNumValue_Object = MibTableColumn
tnCesProfCalledNumValue = _TnCesProfCalledNumValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 4, 1, 2),
    _TnCesProfCalledNumValue_Type()
)
tnCesProfCalledNumValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfCalledNumValue.setStatus("current")
_TnCesProfCallingNumTable_Object = MibTable
tnCesProfCallingNumTable = _TnCesProfCallingNumTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 5)
)
if mibBuilder.loadTexts:
    tnCesProfCallingNumTable.setStatus("current")
_TnCesProfCallingNumEntry_Object = MibTableRow
tnCesProfCallingNumEntry = _TnCesProfCallingNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 5, 1)
)
tnCesProfCallingNumEntry.setIndexNames(
    (0, "TN-CES-ROUTING-MIB", "tnCesProfCallingNumProfileIndex"),
)
if mibBuilder.loadTexts:
    tnCesProfCallingNumEntry.setStatus("current")


class _TnCesProfCallingNumProfileIndex_Type(Unsigned32):
    """Custom type tnCesProfCallingNumProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TnCesProfCallingNumProfileIndex_Type.__name__ = "Unsigned32"
_TnCesProfCallingNumProfileIndex_Object = MibTableColumn
tnCesProfCallingNumProfileIndex = _TnCesProfCallingNumProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 5, 1, 1),
    _TnCesProfCallingNumProfileIndex_Type()
)
tnCesProfCallingNumProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesProfCallingNumProfileIndex.setStatus("current")
_TnCesProfCallingNumValue_Type = OctetString
_TnCesProfCallingNumValue_Object = MibTableColumn
tnCesProfCallingNumValue = _TnCesProfCallingNumValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 5, 1, 2),
    _TnCesProfCallingNumValue_Type()
)
tnCesProfCallingNumValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfCallingNumValue.setStatus("current")
_TnCesProfSchedTable_Object = MibTable
tnCesProfSchedTable = _TnCesProfSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6)
)
if mibBuilder.loadTexts:
    tnCesProfSchedTable.setStatus("current")
_TnCesProfSchedEntry_Object = MibTableRow
tnCesProfSchedEntry = _TnCesProfSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1)
)
tnCesProfSchedEntry.setIndexNames(
    (0, "TN-CES-ROUTING-MIB", "tnCesProfSchedProfileIndex"),
    (0, "TN-CES-ROUTING-MIB", "tnCesProfSchedNumber"),
)
if mibBuilder.loadTexts:
    tnCesProfSchedEntry.setStatus("current")


class _TnCesProfSchedProfileIndex_Type(Unsigned32):
    """Custom type tnCesProfSchedProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TnCesProfSchedProfileIndex_Type.__name__ = "Unsigned32"
_TnCesProfSchedProfileIndex_Object = MibTableColumn
tnCesProfSchedProfileIndex = _TnCesProfSchedProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 1),
    _TnCesProfSchedProfileIndex_Type()
)
tnCesProfSchedProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesProfSchedProfileIndex.setStatus("current")


class _TnCesProfSchedNumber_Type(Unsigned32):
    """Custom type tnCesProfSchedNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TnCesProfSchedNumber_Type.__name__ = "Unsigned32"
_TnCesProfSchedNumber_Object = MibTableColumn
tnCesProfSchedNumber = _TnCesProfSchedNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 2),
    _TnCesProfSchedNumber_Type()
)
tnCesProfSchedNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesProfSchedNumber.setStatus("current")
_TnCesProfSchedEnable_Type = TruthValue
_TnCesProfSchedEnable_Object = MibTableColumn
tnCesProfSchedEnable = _TnCesProfSchedEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 3),
    _TnCesProfSchedEnable_Type()
)
tnCesProfSchedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedEnable.setStatus("current")


class _TnCesProfSchedStartTimeMonHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeMonHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStartTimeMonHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeMonHours_Object = MibTableColumn
tnCesProfSchedStartTimeMonHours = _TnCesProfSchedStartTimeMonHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 4),
    _TnCesProfSchedStartTimeMonHours_Type()
)
tnCesProfSchedStartTimeMonHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeMonHours.setStatus("current")


class _TnCesProfSchedStartTimeMonMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeMonMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStartTimeMonMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeMonMins_Object = MibTableColumn
tnCesProfSchedStartTimeMonMins = _TnCesProfSchedStartTimeMonMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 5),
    _TnCesProfSchedStartTimeMonMins_Type()
)
tnCesProfSchedStartTimeMonMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeMonMins.setStatus("current")


class _TnCesProfSchedStopTimeMonHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeMonHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStopTimeMonHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeMonHours_Object = MibTableColumn
tnCesProfSchedStopTimeMonHours = _TnCesProfSchedStopTimeMonHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 6),
    _TnCesProfSchedStopTimeMonHours_Type()
)
tnCesProfSchedStopTimeMonHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeMonHours.setStatus("current")


class _TnCesProfSchedStopTimeMonMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeMonMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStopTimeMonMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeMonMins_Object = MibTableColumn
tnCesProfSchedStopTimeMonMins = _TnCesProfSchedStopTimeMonMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 7),
    _TnCesProfSchedStopTimeMonMins_Type()
)
tnCesProfSchedStopTimeMonMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeMonMins.setStatus("current")


class _TnCesProfSchedStartTimeTueHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeTueHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStartTimeTueHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeTueHours_Object = MibTableColumn
tnCesProfSchedStartTimeTueHours = _TnCesProfSchedStartTimeTueHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 8),
    _TnCesProfSchedStartTimeTueHours_Type()
)
tnCesProfSchedStartTimeTueHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeTueHours.setStatus("current")


class _TnCesProfSchedStartTimeTueMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeTueMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStartTimeTueMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeTueMins_Object = MibTableColumn
tnCesProfSchedStartTimeTueMins = _TnCesProfSchedStartTimeTueMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 9),
    _TnCesProfSchedStartTimeTueMins_Type()
)
tnCesProfSchedStartTimeTueMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeTueMins.setStatus("current")


class _TnCesProfSchedStopTimeTueHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeTueHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStopTimeTueHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeTueHours_Object = MibTableColumn
tnCesProfSchedStopTimeTueHours = _TnCesProfSchedStopTimeTueHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 10),
    _TnCesProfSchedStopTimeTueHours_Type()
)
tnCesProfSchedStopTimeTueHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeTueHours.setStatus("current")


class _TnCesProfSchedStopTimeTueMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeTueMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStopTimeTueMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeTueMins_Object = MibTableColumn
tnCesProfSchedStopTimeTueMins = _TnCesProfSchedStopTimeTueMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 11),
    _TnCesProfSchedStopTimeTueMins_Type()
)
tnCesProfSchedStopTimeTueMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeTueMins.setStatus("current")


class _TnCesProfSchedStartTimeWedHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeWedHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStartTimeWedHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeWedHours_Object = MibTableColumn
tnCesProfSchedStartTimeWedHours = _TnCesProfSchedStartTimeWedHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 12),
    _TnCesProfSchedStartTimeWedHours_Type()
)
tnCesProfSchedStartTimeWedHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeWedHours.setStatus("current")


class _TnCesProfSchedStartTimeWedMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeWedMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStartTimeWedMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeWedMins_Object = MibTableColumn
tnCesProfSchedStartTimeWedMins = _TnCesProfSchedStartTimeWedMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 13),
    _TnCesProfSchedStartTimeWedMins_Type()
)
tnCesProfSchedStartTimeWedMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeWedMins.setStatus("current")


class _TnCesProfSchedStopTimeWedHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeWedHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStopTimeWedHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeWedHours_Object = MibTableColumn
tnCesProfSchedStopTimeWedHours = _TnCesProfSchedStopTimeWedHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 14),
    _TnCesProfSchedStopTimeWedHours_Type()
)
tnCesProfSchedStopTimeWedHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeWedHours.setStatus("current")


class _TnCesProfSchedStopTimeWedMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeWedMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStopTimeWedMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeWedMins_Object = MibTableColumn
tnCesProfSchedStopTimeWedMins = _TnCesProfSchedStopTimeWedMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 15),
    _TnCesProfSchedStopTimeWedMins_Type()
)
tnCesProfSchedStopTimeWedMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeWedMins.setStatus("current")


class _TnCesProfSchedStartTimeThuHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeThuHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStartTimeThuHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeThuHours_Object = MibTableColumn
tnCesProfSchedStartTimeThuHours = _TnCesProfSchedStartTimeThuHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 16),
    _TnCesProfSchedStartTimeThuHours_Type()
)
tnCesProfSchedStartTimeThuHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeThuHours.setStatus("current")


class _TnCesProfSchedStartTimeThuMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeThuMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStartTimeThuMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeThuMins_Object = MibTableColumn
tnCesProfSchedStartTimeThuMins = _TnCesProfSchedStartTimeThuMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 17),
    _TnCesProfSchedStartTimeThuMins_Type()
)
tnCesProfSchedStartTimeThuMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeThuMins.setStatus("current")


class _TnCesProfSchedStopTimeThuHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeThuHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStopTimeThuHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeThuHours_Object = MibTableColumn
tnCesProfSchedStopTimeThuHours = _TnCesProfSchedStopTimeThuHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 18),
    _TnCesProfSchedStopTimeThuHours_Type()
)
tnCesProfSchedStopTimeThuHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeThuHours.setStatus("current")


class _TnCesProfSchedStopTimeThuMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeThuMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStopTimeThuMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeThuMins_Object = MibTableColumn
tnCesProfSchedStopTimeThuMins = _TnCesProfSchedStopTimeThuMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 19),
    _TnCesProfSchedStopTimeThuMins_Type()
)
tnCesProfSchedStopTimeThuMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeThuMins.setStatus("current")


class _TnCesProfSchedStartTimeFriHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeFriHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStartTimeFriHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeFriHours_Object = MibTableColumn
tnCesProfSchedStartTimeFriHours = _TnCesProfSchedStartTimeFriHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 20),
    _TnCesProfSchedStartTimeFriHours_Type()
)
tnCesProfSchedStartTimeFriHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeFriHours.setStatus("current")


class _TnCesProfSchedStartTimeFriMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeFriMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStartTimeFriMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeFriMins_Object = MibTableColumn
tnCesProfSchedStartTimeFriMins = _TnCesProfSchedStartTimeFriMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 21),
    _TnCesProfSchedStartTimeFriMins_Type()
)
tnCesProfSchedStartTimeFriMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeFriMins.setStatus("current")


class _TnCesProfSchedStopTimeFriHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeFriHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStopTimeFriHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeFriHours_Object = MibTableColumn
tnCesProfSchedStopTimeFriHours = _TnCesProfSchedStopTimeFriHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 22),
    _TnCesProfSchedStopTimeFriHours_Type()
)
tnCesProfSchedStopTimeFriHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeFriHours.setStatus("current")


class _TnCesProfSchedStopTimeFriMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeFriMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStopTimeFriMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeFriMins_Object = MibTableColumn
tnCesProfSchedStopTimeFriMins = _TnCesProfSchedStopTimeFriMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 23),
    _TnCesProfSchedStopTimeFriMins_Type()
)
tnCesProfSchedStopTimeFriMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeFriMins.setStatus("current")


class _TnCesProfSchedStartTimeSatHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeSatHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStartTimeSatHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeSatHours_Object = MibTableColumn
tnCesProfSchedStartTimeSatHours = _TnCesProfSchedStartTimeSatHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 24),
    _TnCesProfSchedStartTimeSatHours_Type()
)
tnCesProfSchedStartTimeSatHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeSatHours.setStatus("current")


class _TnCesProfSchedStartTimeSatMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeSatMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStartTimeSatMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeSatMins_Object = MibTableColumn
tnCesProfSchedStartTimeSatMins = _TnCesProfSchedStartTimeSatMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 25),
    _TnCesProfSchedStartTimeSatMins_Type()
)
tnCesProfSchedStartTimeSatMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeSatMins.setStatus("current")


class _TnCesProfSchedStopTimeSatHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeSatHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStopTimeSatHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeSatHours_Object = MibTableColumn
tnCesProfSchedStopTimeSatHours = _TnCesProfSchedStopTimeSatHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 26),
    _TnCesProfSchedStopTimeSatHours_Type()
)
tnCesProfSchedStopTimeSatHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeSatHours.setStatus("current")


class _TnCesProfSchedStopTimeSatMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeSatMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStopTimeSatMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeSatMins_Object = MibTableColumn
tnCesProfSchedStopTimeSatMins = _TnCesProfSchedStopTimeSatMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 27),
    _TnCesProfSchedStopTimeSatMins_Type()
)
tnCesProfSchedStopTimeSatMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeSatMins.setStatus("current")


class _TnCesProfSchedStartTimeSunHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeSunHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStartTimeSunHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeSunHours_Object = MibTableColumn
tnCesProfSchedStartTimeSunHours = _TnCesProfSchedStartTimeSunHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 28),
    _TnCesProfSchedStartTimeSunHours_Type()
)
tnCesProfSchedStartTimeSunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeSunHours.setStatus("current")


class _TnCesProfSchedStartTimeSunMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStartTimeSunMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStartTimeSunMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStartTimeSunMins_Object = MibTableColumn
tnCesProfSchedStartTimeSunMins = _TnCesProfSchedStartTimeSunMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 29),
    _TnCesProfSchedStartTimeSunMins_Type()
)
tnCesProfSchedStartTimeSunMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStartTimeSunMins.setStatus("current")


class _TnCesProfSchedStopTimeSunHours_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeSunHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesProfSchedStopTimeSunHours_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeSunHours_Object = MibTableColumn
tnCesProfSchedStopTimeSunHours = _TnCesProfSchedStopTimeSunHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 30),
    _TnCesProfSchedStopTimeSunHours_Type()
)
tnCesProfSchedStopTimeSunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeSunHours.setStatus("current")


class _TnCesProfSchedStopTimeSunMins_Type(Unsigned32):
    """Custom type tnCesProfSchedStopTimeSunMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesProfSchedStopTimeSunMins_Type.__name__ = "Unsigned32"
_TnCesProfSchedStopTimeSunMins_Object = MibTableColumn
tnCesProfSchedStopTimeSunMins = _TnCesProfSchedStopTimeSunMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 1, 6, 1, 31),
    _TnCesProfSchedStopTimeSunMins_Type()
)
tnCesProfSchedStopTimeSunMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProfSchedStopTimeSunMins.setStatus("current")
_TnCesRoutingConformance_ObjectIdentity = ObjectIdentity
tnCesRoutingConformance = _TnCesRoutingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 2)
)
_TnCesRoutingCompliances_ObjectIdentity = ObjectIdentity
tnCesRoutingCompliances = _TnCesRoutingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 2, 1)
)
_TnCesRoutingGroups_ObjectIdentity = ObjectIdentity
tnCesRoutingGroups = _TnCesRoutingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 2, 2)
)

# Managed Objects groups

tnCesRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 2, 2, 1)
)
tnCesRoutingGroup.setObjects(
      *(("TN-CES-ROUTING-MIB", "tnCesIPNameName"),
        ("TN-CES-ROUTING-MIB", "tnCesIPNameIpAddrType"),
        ("TN-CES-ROUTING-MIB", "tnCesIPNameIpAddr"),
        ("TN-CES-ROUTING-MIB", "tnCesGroupName"),
        ("TN-CES-ROUTING-MIB", "tnCesGroupCyclicPortSearch"),
        ("TN-CES-ROUTING-MIB", "tnCesGroupCyclicChannelSearch"),
        ("TN-CES-ROUTING-MIB", "tnCesGroupChannels"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileName"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileType"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileEnabled"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileRerouteUnanswered"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileRerouteUnansweredSec"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileSourceEndpointType"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileSourceItemIndex"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileSourceChanNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestPrimEndpointType"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestPrimItemIndex"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestPrimChanNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestSecEndpointType"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestSecItemIndex"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestSecChanNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestTerEndpointType"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestTerItemIndex"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileDestTerChanNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileVoiceConversion"),
        ("TN-CES-ROUTING-MIB", "tnCesProfilePrimaryCalledNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfilePrimaryCallingNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileSecCalledNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileSecCallingNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileTerCalledNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfileTerCallingNumber"),
        ("TN-CES-ROUTING-MIB", "tnCesProfCalledNumValue"),
        ("TN-CES-ROUTING-MIB", "tnCesProfCallingNumValue"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedEnable"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeMonHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeMonMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeMonHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeMonMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeTueHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeTueMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeTueHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeTueMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeWedHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeWedMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeWedHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeWedMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeThuHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeThuMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeThuHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeThuMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeFriHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeFriMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeFriHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeFriMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeSatHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeSatMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeSatHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeSatMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeSunHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStartTimeSunMins"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeSunHours"),
        ("TN-CES-ROUTING-MIB", "tnCesProfSchedStopTimeSunMins"))
)
if mibBuilder.loadTexts:
    tnCesRoutingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnCesRoutingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 61, 2, 1, 1)
)
tnCesRoutingMIBCompliance.setObjects(
    ("TN-CES-ROUTING-MIB", "tnCesRoutingGroup")
)
if mibBuilder.loadTexts:
    tnCesRoutingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-CES-ROUTING-MIB",
    **{"tnCesRoutingMIB": tnCesRoutingMIB,
       "tnCesRoutingObjects": tnCesRoutingObjects,
       "tnCesGroupTable": tnCesGroupTable,
       "tnCesGroupEntry": tnCesGroupEntry,
       "tnCesGroupIndex": tnCesGroupIndex,
       "tnCesGroupPortNumber": tnCesGroupPortNumber,
       "tnCesGroupName": tnCesGroupName,
       "tnCesGroupCyclicPortSearch": tnCesGroupCyclicPortSearch,
       "tnCesGroupCyclicChannelSearch": tnCesGroupCyclicChannelSearch,
       "tnCesGroupChannels": tnCesGroupChannels,
       "tnCesIPNameTable": tnCesIPNameTable,
       "tnCesIPNameEntry": tnCesIPNameEntry,
       "tnCesIPNameIndex": tnCesIPNameIndex,
       "tnCesIPNameName": tnCesIPNameName,
       "tnCesIPNameIpAddrType": tnCesIPNameIpAddrType,
       "tnCesIPNameIpAddr": tnCesIPNameIpAddr,
       "tnCesProfileTable": tnCesProfileTable,
       "tnCesProfileEntry": tnCesProfileEntry,
       "tnCesProfileIndex": tnCesProfileIndex,
       "tnCesProfileName": tnCesProfileName,
       "tnCesProfileType": tnCesProfileType,
       "tnCesProfileEnabled": tnCesProfileEnabled,
       "tnCesProfileRerouteUnanswered": tnCesProfileRerouteUnanswered,
       "tnCesProfileRerouteUnansweredSec": tnCesProfileRerouteUnansweredSec,
       "tnCesProfileSourceEndpointType": tnCesProfileSourceEndpointType,
       "tnCesProfileSourceItemIndex": tnCesProfileSourceItemIndex,
       "tnCesProfileSourceChanNumber": tnCesProfileSourceChanNumber,
       "tnCesProfileDestPrimEndpointType": tnCesProfileDestPrimEndpointType,
       "tnCesProfileDestPrimItemIndex": tnCesProfileDestPrimItemIndex,
       "tnCesProfileDestPrimChanNumber": tnCesProfileDestPrimChanNumber,
       "tnCesProfileDestSecEndpointType": tnCesProfileDestSecEndpointType,
       "tnCesProfileDestSecItemIndex": tnCesProfileDestSecItemIndex,
       "tnCesProfileDestSecChanNumber": tnCesProfileDestSecChanNumber,
       "tnCesProfileDestTerEndpointType": tnCesProfileDestTerEndpointType,
       "tnCesProfileDestTerItemIndex": tnCesProfileDestTerItemIndex,
       "tnCesProfileDestTerChanNumber": tnCesProfileDestTerChanNumber,
       "tnCesProfileVoiceConversion": tnCesProfileVoiceConversion,
       "tnCesProfilePrimaryCalledNumber": tnCesProfilePrimaryCalledNumber,
       "tnCesProfilePrimaryCallingNumber": tnCesProfilePrimaryCallingNumber,
       "tnCesProfileSecCalledNumber": tnCesProfileSecCalledNumber,
       "tnCesProfileSecCallingNumber": tnCesProfileSecCallingNumber,
       "tnCesProfileTerCalledNumber": tnCesProfileTerCalledNumber,
       "tnCesProfileTerCallingNumber": tnCesProfileTerCallingNumber,
       "tnCesProfCalledNumTable": tnCesProfCalledNumTable,
       "tnCesProfCalledNumEntry": tnCesProfCalledNumEntry,
       "tnCesProfCalledNumProfileIndex": tnCesProfCalledNumProfileIndex,
       "tnCesProfCalledNumValue": tnCesProfCalledNumValue,
       "tnCesProfCallingNumTable": tnCesProfCallingNumTable,
       "tnCesProfCallingNumEntry": tnCesProfCallingNumEntry,
       "tnCesProfCallingNumProfileIndex": tnCesProfCallingNumProfileIndex,
       "tnCesProfCallingNumValue": tnCesProfCallingNumValue,
       "tnCesProfSchedTable": tnCesProfSchedTable,
       "tnCesProfSchedEntry": tnCesProfSchedEntry,
       "tnCesProfSchedProfileIndex": tnCesProfSchedProfileIndex,
       "tnCesProfSchedNumber": tnCesProfSchedNumber,
       "tnCesProfSchedEnable": tnCesProfSchedEnable,
       "tnCesProfSchedStartTimeMonHours": tnCesProfSchedStartTimeMonHours,
       "tnCesProfSchedStartTimeMonMins": tnCesProfSchedStartTimeMonMins,
       "tnCesProfSchedStopTimeMonHours": tnCesProfSchedStopTimeMonHours,
       "tnCesProfSchedStopTimeMonMins": tnCesProfSchedStopTimeMonMins,
       "tnCesProfSchedStartTimeTueHours": tnCesProfSchedStartTimeTueHours,
       "tnCesProfSchedStartTimeTueMins": tnCesProfSchedStartTimeTueMins,
       "tnCesProfSchedStopTimeTueHours": tnCesProfSchedStopTimeTueHours,
       "tnCesProfSchedStopTimeTueMins": tnCesProfSchedStopTimeTueMins,
       "tnCesProfSchedStartTimeWedHours": tnCesProfSchedStartTimeWedHours,
       "tnCesProfSchedStartTimeWedMins": tnCesProfSchedStartTimeWedMins,
       "tnCesProfSchedStopTimeWedHours": tnCesProfSchedStopTimeWedHours,
       "tnCesProfSchedStopTimeWedMins": tnCesProfSchedStopTimeWedMins,
       "tnCesProfSchedStartTimeThuHours": tnCesProfSchedStartTimeThuHours,
       "tnCesProfSchedStartTimeThuMins": tnCesProfSchedStartTimeThuMins,
       "tnCesProfSchedStopTimeThuHours": tnCesProfSchedStopTimeThuHours,
       "tnCesProfSchedStopTimeThuMins": tnCesProfSchedStopTimeThuMins,
       "tnCesProfSchedStartTimeFriHours": tnCesProfSchedStartTimeFriHours,
       "tnCesProfSchedStartTimeFriMins": tnCesProfSchedStartTimeFriMins,
       "tnCesProfSchedStopTimeFriHours": tnCesProfSchedStopTimeFriHours,
       "tnCesProfSchedStopTimeFriMins": tnCesProfSchedStopTimeFriMins,
       "tnCesProfSchedStartTimeSatHours": tnCesProfSchedStartTimeSatHours,
       "tnCesProfSchedStartTimeSatMins": tnCesProfSchedStartTimeSatMins,
       "tnCesProfSchedStopTimeSatHours": tnCesProfSchedStopTimeSatHours,
       "tnCesProfSchedStopTimeSatMins": tnCesProfSchedStopTimeSatMins,
       "tnCesProfSchedStartTimeSunHours": tnCesProfSchedStartTimeSunHours,
       "tnCesProfSchedStartTimeSunMins": tnCesProfSchedStartTimeSunMins,
       "tnCesProfSchedStopTimeSunHours": tnCesProfSchedStopTimeSunHours,
       "tnCesProfSchedStopTimeSunMins": tnCesProfSchedStopTimeSunMins,
       "tnCesRoutingConformance": tnCesRoutingConformance,
       "tnCesRoutingCompliances": tnCesRoutingCompliances,
       "tnCesRoutingMIBCompliance": tnCesRoutingMIBCompliance,
       "tnCesRoutingGroups": tnCesRoutingGroups,
       "tnCesRoutingGroup": tnCesRoutingGroup}
)
