# SNMP MIB module (HH3C-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-TWAMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:10 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cTwamp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184)
)
if mibBuilder.loadTexts:
    hh3cTwamp.setRevisions(
        ("2020-09-10 00:00",
         "2019-12-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cTwampNotifications_ObjectIdentity = ObjectIdentity
hh3cTwampNotifications = _Hh3cTwampNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 1)
)
_Hh3cTwamplightObjects_ObjectIdentity = ObjectIdentity
hh3cTwamplightObjects = _Hh3cTwamplightObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2)
)
_Hh3cTwamplightController_ObjectIdentity = ObjectIdentity
hh3cTwamplightController = _Hh3cTwamplightController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1)
)


class _Hh3cTwamplightClientEnable_Type(TruthValue):
    """Custom type hh3cTwamplightClientEnable based on TruthValue"""
    defaultValue = 2


_Hh3cTwamplightClientEnable_Type.__name__ = "TruthValue"
_Hh3cTwamplightClientEnable_Object = MibScalar
hh3cTwamplightClientEnable = _Hh3cTwamplightClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 1),
    _Hh3cTwamplightClientEnable_Type()
)
hh3cTwamplightClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTwamplightClientEnable.setStatus("current")


class _Hh3cTwamplightSenderEnable_Type(TruthValue):
    """Custom type hh3cTwamplightSenderEnable based on TruthValue"""
    defaultValue = 2


_Hh3cTwamplightSenderEnable_Type.__name__ = "TruthValue"
_Hh3cTwamplightSenderEnable_Object = MibScalar
hh3cTwamplightSenderEnable = _Hh3cTwamplightSenderEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 2),
    _Hh3cTwamplightSenderEnable_Type()
)
hh3cTwamplightSenderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTwamplightSenderEnable.setStatus("current")
_Hh3cTwamplightClientTable_Object = MibTable
hh3cTwamplightClientTable = _Hh3cTwamplightClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cTwamplightClientTable.setStatus("current")
_Hh3cTwamplightClientEntry_Object = MibTableRow
hh3cTwamplightClientEntry = _Hh3cTwamplightClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1)
)
hh3cTwamplightClientEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightClientEntry.setStatus("current")
_Hh3cTwamplightControllerID_Type = Integer32
_Hh3cTwamplightControllerID_Object = MibTableColumn
hh3cTwamplightControllerID = _Hh3cTwamplightControllerID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 1),
    _Hh3cTwamplightControllerID_Type()
)
hh3cTwamplightControllerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTwamplightControllerID.setStatus("current")
_Hh3cTwamplightClientSrcAddrType_Type = InetAddressType
_Hh3cTwamplightClientSrcAddrType_Object = MibTableColumn
hh3cTwamplightClientSrcAddrType = _Hh3cTwamplightClientSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 2),
    _Hh3cTwamplightClientSrcAddrType_Type()
)
hh3cTwamplightClientSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientSrcAddrType.setStatus("current")


class _Hh3cTwamplightClientSrcAddr_Type(InetAddress):
    """Custom type hh3cTwamplightClientSrcAddr based on InetAddress"""
    defaultHexValue = ""


_Hh3cTwamplightClientSrcAddr_Type.__name__ = "InetAddress"
_Hh3cTwamplightClientSrcAddr_Object = MibTableColumn
hh3cTwamplightClientSrcAddr = _Hh3cTwamplightClientSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 3),
    _Hh3cTwamplightClientSrcAddr_Type()
)
hh3cTwamplightClientSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientSrcAddr.setStatus("current")
_Hh3cTwamplightClientTrgtAddrType_Type = InetAddressType
_Hh3cTwamplightClientTrgtAddrType_Object = MibTableColumn
hh3cTwamplightClientTrgtAddrType = _Hh3cTwamplightClientTrgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 4),
    _Hh3cTwamplightClientTrgtAddrType_Type()
)
hh3cTwamplightClientTrgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientTrgtAddrType.setStatus("current")


class _Hh3cTwamplightClientTrgtAddr_Type(InetAddress):
    """Custom type hh3cTwamplightClientTrgtAddr based on InetAddress"""
    defaultHexValue = ""


_Hh3cTwamplightClientTrgtAddr_Type.__name__ = "InetAddress"
_Hh3cTwamplightClientTrgtAddr_Object = MibTableColumn
hh3cTwamplightClientTrgtAddr = _Hh3cTwamplightClientTrgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 5),
    _Hh3cTwamplightClientTrgtAddr_Type()
)
hh3cTwamplightClientTrgtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientTrgtAddr.setStatus("current")


class _Hh3cTwamplightClientSrcPort_Type(Integer32):
    """Custom type hh3cTwamplightClientSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cTwamplightClientSrcPort_Type.__name__ = "Integer32"
_Hh3cTwamplightClientSrcPort_Object = MibTableColumn
hh3cTwamplightClientSrcPort = _Hh3cTwamplightClientSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 6),
    _Hh3cTwamplightClientSrcPort_Type()
)
hh3cTwamplightClientSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientSrcPort.setStatus("current")


class _Hh3cTwamplightClientTrgtPort_Type(Integer32):
    """Custom type hh3cTwamplightClientTrgtPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cTwamplightClientTrgtPort_Type.__name__ = "Integer32"
_Hh3cTwamplightClientTrgtPort_Object = MibTableColumn
hh3cTwamplightClientTrgtPort = _Hh3cTwamplightClientTrgtPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 7),
    _Hh3cTwamplightClientTrgtPort_Type()
)
hh3cTwamplightClientTrgtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientTrgtPort.setStatus("current")


class _Hh3cTwamplightClientVPN_Type(DisplayString):
    """Custom type hh3cTwamplightClientVPN based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cTwamplightClientVPN_Type.__name__ = "DisplayString"
_Hh3cTwamplightClientVPN_Object = MibTableColumn
hh3cTwamplightClientVPN = _Hh3cTwamplightClientVPN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 8),
    _Hh3cTwamplightClientVPN_Type()
)
hh3cTwamplightClientVPN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientVPN.setStatus("current")


class _Hh3cTwamplightClientDscp_Type(Integer32):
    """Custom type hh3cTwamplightClientDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cTwamplightClientDscp_Type.__name__ = "Integer32"
_Hh3cTwamplightClientDscp_Object = MibTableColumn
hh3cTwamplightClientDscp = _Hh3cTwamplightClientDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 9),
    _Hh3cTwamplightClientDscp_Type()
)
hh3cTwamplightClientDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientDscp.setStatus("current")


class _Hh3cTwamplightClientDataSize_Type(Integer32):
    """Custom type hh3cTwamplightClientDataSize based on Integer32"""
    defaultValue = 142

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(44, 1518),
    )


_Hh3cTwamplightClientDataSize_Type.__name__ = "Integer32"
_Hh3cTwamplightClientDataSize_Object = MibTableColumn
hh3cTwamplightClientDataSize = _Hh3cTwamplightClientDataSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 10),
    _Hh3cTwamplightClientDataSize_Type()
)
hh3cTwamplightClientDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientDataSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cTwamplightClientDataSize.setUnits("octets")


class _Hh3cTwamplightClientDescription_Type(DisplayString):
    """Custom type hh3cTwamplightClientDescription based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_Hh3cTwamplightClientDescription_Type.__name__ = "DisplayString"
_Hh3cTwamplightClientDescription_Object = MibTableColumn
hh3cTwamplightClientDescription = _Hh3cTwamplightClientDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 11),
    _Hh3cTwamplightClientDescription_Type()
)
hh3cTwamplightClientDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientDescription.setStatus("current")
_Hh3cTwamplightClientRowStatus_Type = RowStatus
_Hh3cTwamplightClientRowStatus_Object = MibTableColumn
hh3cTwamplightClientRowStatus = _Hh3cTwamplightClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 12),
    _Hh3cTwamplightClientRowStatus_Type()
)
hh3cTwamplightClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientRowStatus.setStatus("current")


class _Hh3cTwamplightClientSrcIfName_Type(DisplayString):
    """Custom type hh3cTwamplightClientSrcIfName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3cTwamplightClientSrcIfName_Type.__name__ = "DisplayString"
_Hh3cTwamplightClientSrcIfName_Object = MibTableColumn
hh3cTwamplightClientSrcIfName = _Hh3cTwamplightClientSrcIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 13),
    _Hh3cTwamplightClientSrcIfName_Type()
)
hh3cTwamplightClientSrcIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientSrcIfName.setStatus("current")


class _Hh3cTwamplightClientServiceID_Type(Unsigned32):
    """Custom type hh3cTwamplightClientServiceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Hh3cTwamplightClientServiceID_Type.__name__ = "Unsigned32"
_Hh3cTwamplightClientServiceID_Object = MibTableColumn
hh3cTwamplightClientServiceID = _Hh3cTwamplightClientServiceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 14),
    _Hh3cTwamplightClientServiceID_Type()
)
hh3cTwamplightClientServiceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientServiceID.setStatus("current")
if mibBuilder.loadTexts:
    hh3cTwamplightClientServiceID.setUnits("octets")
_Hh3cTwamplightClientDesMac_Type = MacAddress
_Hh3cTwamplightClientDesMac_Object = MibTableColumn
hh3cTwamplightClientDesMac = _Hh3cTwamplightClientDesMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 15),
    _Hh3cTwamplightClientDesMac_Type()
)
hh3cTwamplightClientDesMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientDesMac.setStatus("current")
_Hh3cTwamplightClientSrcMac_Type = MacAddress
_Hh3cTwamplightClientSrcMac_Object = MibTableColumn
hh3cTwamplightClientSrcMac = _Hh3cTwamplightClientSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 16),
    _Hh3cTwamplightClientSrcMac_Type()
)
hh3cTwamplightClientSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientSrcMac.setStatus("current")


class _Hh3cTwamplightClientTimeFormat_Type(Integer32):
    """Custom type hh3cTwamplightClientTimeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntp", 1),
          ("ptp", 2))
    )


_Hh3cTwamplightClientTimeFormat_Type.__name__ = "Integer32"
_Hh3cTwamplightClientTimeFormat_Object = MibTableColumn
hh3cTwamplightClientTimeFormat = _Hh3cTwamplightClientTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 17),
    _Hh3cTwamplightClientTimeFormat_Type()
)
hh3cTwamplightClientTimeFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientTimeFormat.setStatus("current")


class _Hh3cTwamplightClientDataFill_Type(DisplayString):
    """Custom type hh3cTwamplightClientDataFill based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_Hh3cTwamplightClientDataFill_Type.__name__ = "DisplayString"
_Hh3cTwamplightClientDataFill_Object = MibTableColumn
hh3cTwamplightClientDataFill = _Hh3cTwamplightClientDataFill_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 18),
    _Hh3cTwamplightClientDataFill_Type()
)
hh3cTwamplightClientDataFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientDataFill.setStatus("current")


class _Hh3cTwamplightClientDataFillType_Type(Integer32):
    """Custom type hh3cTwamplightClientDataFillType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2))
    )


_Hh3cTwamplightClientDataFillType_Type.__name__ = "Integer32"
_Hh3cTwamplightClientDataFillType_Object = MibTableColumn
hh3cTwamplightClientDataFillType = _Hh3cTwamplightClientDataFillType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 19),
    _Hh3cTwamplightClientDataFillType_Type()
)
hh3cTwamplightClientDataFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientDataFillType.setStatus("current")


class _Hh3cTwamplightClientSVlanID_Type(Unsigned32):
    """Custom type hh3cTwamplightClientSVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cTwamplightClientSVlanID_Type.__name__ = "Unsigned32"
_Hh3cTwamplightClientSVlanID_Object = MibTableColumn
hh3cTwamplightClientSVlanID = _Hh3cTwamplightClientSVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 20),
    _Hh3cTwamplightClientSVlanID_Type()
)
hh3cTwamplightClientSVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientSVlanID.setStatus("current")


class _Hh3cTwamplightClientCVlanID_Type(Unsigned32):
    """Custom type hh3cTwamplightClientCVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cTwamplightClientCVlanID_Type.__name__ = "Unsigned32"
_Hh3cTwamplightClientCVlanID_Object = MibTableColumn
hh3cTwamplightClientCVlanID = _Hh3cTwamplightClientCVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 21),
    _Hh3cTwamplightClientCVlanID_Type()
)
hh3cTwamplightClientCVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientCVlanID.setStatus("current")


class _Hh3cTwamplightClientVlanPriority_Type(Unsigned32):
    """Custom type hh3cTwamplightClientVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cTwamplightClientVlanPriority_Type.__name__ = "Unsigned32"
_Hh3cTwamplightClientVlanPriority_Object = MibTableColumn
hh3cTwamplightClientVlanPriority = _Hh3cTwamplightClientVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 22),
    _Hh3cTwamplightClientVlanPriority_Type()
)
hh3cTwamplightClientVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientVlanPriority.setStatus("current")


class _Hh3cTwamplightClientBindIfName_Type(DisplayString):
    """Custom type hh3cTwamplightClientBindIfName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3cTwamplightClientBindIfName_Type.__name__ = "DisplayString"
_Hh3cTwamplightClientBindIfName_Object = MibTableColumn
hh3cTwamplightClientBindIfName = _Hh3cTwamplightClientBindIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 3, 1, 23),
    _Hh3cTwamplightClientBindIfName_Type()
)
hh3cTwamplightClientBindIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightClientBindIfName.setStatus("current")
_Hh3cTwamplightSenderAdminTable_Object = MibTable
hh3cTwamplightSenderAdminTable = _Hh3cTwamplightSenderAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cTwamplightSenderAdminTable.setStatus("current")
_Hh3cTwamplightSenderAdminEntry_Object = MibTableRow
hh3cTwamplightSenderAdminEntry = _Hh3cTwamplightSenderAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4, 1)
)
hh3cTwamplightSenderAdminEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightSenderAdminEntry.setStatus("current")
_Hh3cTwamplightSendAdminContinual_Type = TruthValue
_Hh3cTwamplightSendAdminContinual_Object = MibTableColumn
hh3cTwamplightSendAdminContinual = _Hh3cTwamplightSendAdminContinual_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4, 1, 1),
    _Hh3cTwamplightSendAdminContinual_Type()
)
hh3cTwamplightSendAdminContinual.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightSendAdminContinual.setStatus("current")


class _Hh3cTwamplightSendAdminDuration_Type(Integer32):
    """Custom type hh3cTwamplightSendAdminDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Hh3cTwamplightSendAdminDuration_Type.__name__ = "Integer32"
_Hh3cTwamplightSendAdminDuration_Object = MibTableColumn
hh3cTwamplightSendAdminDuration = _Hh3cTwamplightSendAdminDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4, 1, 2),
    _Hh3cTwamplightSendAdminDuration_Type()
)
hh3cTwamplightSendAdminDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightSendAdminDuration.setStatus("current")


class _Hh3cTwamplightSendAdminPktCount_Type(Integer32):
    """Custom type hh3cTwamplightSendAdminPktCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_Hh3cTwamplightSendAdminPktCount_Type.__name__ = "Integer32"
_Hh3cTwamplightSendAdminPktCount_Object = MibTableColumn
hh3cTwamplightSendAdminPktCount = _Hh3cTwamplightSendAdminPktCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4, 1, 3),
    _Hh3cTwamplightSendAdminPktCount_Type()
)
hh3cTwamplightSendAdminPktCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightSendAdminPktCount.setStatus("current")


class _Hh3cTwamplightSendAdminTxPeriod_Type(Integer32):
    """Custom type hh3cTwamplightSendAdminTxPeriod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("interval10ms", 1),
          ("interval100ms", 2),
          ("interval1s", 3),
          ("interval30s", 4),
          ("interval10s", 5))
    )


_Hh3cTwamplightSendAdminTxPeriod_Type.__name__ = "Integer32"
_Hh3cTwamplightSendAdminTxPeriod_Object = MibTableColumn
hh3cTwamplightSendAdminTxPeriod = _Hh3cTwamplightSendAdminTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4, 1, 4),
    _Hh3cTwamplightSendAdminTxPeriod_Type()
)
hh3cTwamplightSendAdminTxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightSendAdminTxPeriod.setStatus("current")


class _Hh3cTwamplightSendAdminTimeOut_Type(Integer32):
    """Custom type hh3cTwamplightSendAdminTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cTwamplightSendAdminTimeOut_Type.__name__ = "Integer32"
_Hh3cTwamplightSendAdminTimeOut_Object = MibTableColumn
hh3cTwamplightSendAdminTimeOut = _Hh3cTwamplightSendAdminTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4, 1, 5),
    _Hh3cTwamplightSendAdminTimeOut_Type()
)
hh3cTwamplightSendAdminTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightSendAdminTimeOut.setStatus("current")
_Hh3cTwamplightSendAdminRowStatus_Type = RowStatus
_Hh3cTwamplightSendAdminRowStatus_Object = MibTableColumn
hh3cTwamplightSendAdminRowStatus = _Hh3cTwamplightSendAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 4, 1, 6),
    _Hh3cTwamplightSendAdminRowStatus_Type()
)
hh3cTwamplightSendAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightSendAdminRowStatus.setStatus("current")
_Hh3cTwamplightSenderStatusTable_Object = MibTable
hh3cTwamplightSenderStatusTable = _Hh3cTwamplightSenderStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cTwamplightSenderStatusTable.setStatus("current")
_Hh3cTwamplightSenderStatusEntry_Object = MibTableRow
hh3cTwamplightSenderStatusEntry = _Hh3cTwamplightSenderStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 5, 1)
)
hh3cTwamplightSenderStatusEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightSenderStatusEntry.setStatus("current")


class _Hh3cTwamplightSenderStatus_Type(Integer32):
    """Custom type hh3cTwamplightSenderStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_Hh3cTwamplightSenderStatus_Type.__name__ = "Integer32"
_Hh3cTwamplightSenderStatus_Object = MibTableColumn
hh3cTwamplightSenderStatus = _Hh3cTwamplightSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 5, 1, 1),
    _Hh3cTwamplightSenderStatus_Type()
)
hh3cTwamplightSenderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightSenderStatus.setStatus("current")


class _Hh3cTwamplightSenderStatusType_Type(Integer32):
    """Custom type hh3cTwamplightSenderStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("continual", 1),
          ("onDemand", 2))
    )


_Hh3cTwamplightSenderStatusType_Type.__name__ = "Integer32"
_Hh3cTwamplightSenderStatusType_Object = MibTableColumn
hh3cTwamplightSenderStatusType = _Hh3cTwamplightSenderStatusType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 5, 1, 2),
    _Hh3cTwamplightSenderStatusType_Type()
)
hh3cTwamplightSenderStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightSenderStatusType.setStatus("current")


class _Hh3cTwamplightLastStartTime_Type(DateAndTime):
    """Custom type hh3cTwamplightLastStartTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Hh3cTwamplightLastStartTime_Type.__name__ = "DateAndTime"
_Hh3cTwamplightLastStartTime_Object = MibTableColumn
hh3cTwamplightLastStartTime = _Hh3cTwamplightLastStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 5, 1, 4),
    _Hh3cTwamplightLastStartTime_Type()
)
hh3cTwamplightLastStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightLastStartTime.setStatus("current")


class _Hh3cTwamplightLastStopTime_Type(DateAndTime):
    """Custom type hh3cTwamplightLastStopTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Hh3cTwamplightLastStopTime_Type.__name__ = "DateAndTime"
_Hh3cTwamplightLastStopTime_Object = MibTableColumn
hh3cTwamplightLastStopTime = _Hh3cTwamplightLastStopTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 5, 1, 5),
    _Hh3cTwamplightLastStopTime_Type()
)
hh3cTwamplightLastStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightLastStopTime.setStatus("current")
_Hh3cTwamplightTwoWayDelayTable_Object = MibTable
hh3cTwamplightTwoWayDelayTable = _Hh3cTwamplightTwoWayDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cTwamplightTwoWayDelayTable.setStatus("current")
_Hh3cTwamplightTwoWayDelayEntry_Object = MibTableRow
hh3cTwamplightTwoWayDelayEntry = _Hh3cTwamplightTwoWayDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1)
)
hh3cTwamplightTwoWayDelayEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightTWDelaySeq"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightTwoWayDelayEntry.setStatus("current")


class _Hh3cTwamplightTWDelaySeq_Type(Gauge32):
    """Custom type hh3cTwamplightTWDelaySeq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cTwamplightTWDelaySeq_Type.__name__ = "Gauge32"
_Hh3cTwamplightTWDelaySeq_Object = MibTableColumn
hh3cTwamplightTWDelaySeq = _Hh3cTwamplightTWDelaySeq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 1),
    _Hh3cTwamplightTWDelaySeq_Type()
)
hh3cTwamplightTWDelaySeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelaySeq.setStatus("current")
_Hh3cTwamplightTWDelayAvgDelay_Type = Integer32
_Hh3cTwamplightTWDelayAvgDelay_Object = MibTableColumn
hh3cTwamplightTWDelayAvgDelay = _Hh3cTwamplightTWDelayAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 2),
    _Hh3cTwamplightTWDelayAvgDelay_Type()
)
hh3cTwamplightTWDelayAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayAvgDelay.setStatus("current")
_Hh3cTwamplightTWDelayMaxDelay_Type = Integer32
_Hh3cTwamplightTWDelayMaxDelay_Object = MibTableColumn
hh3cTwamplightTWDelayMaxDelay = _Hh3cTwamplightTWDelayMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 3),
    _Hh3cTwamplightTWDelayMaxDelay_Type()
)
hh3cTwamplightTWDelayMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMaxDelay.setStatus("current")
_Hh3cTwamplightTWDelayMinDelay_Type = Integer32
_Hh3cTwamplightTWDelayMinDelay_Object = MibTableColumn
hh3cTwamplightTWDelayMinDelay = _Hh3cTwamplightTWDelayMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 4),
    _Hh3cTwamplightTWDelayMinDelay_Type()
)
hh3cTwamplightTWDelayMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMinDelay.setStatus("current")
_Hh3cTwamplightTWDelayAvgJitter_Type = Integer32
_Hh3cTwamplightTWDelayAvgJitter_Object = MibTableColumn
hh3cTwamplightTWDelayAvgJitter = _Hh3cTwamplightTWDelayAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 5),
    _Hh3cTwamplightTWDelayAvgJitter_Type()
)
hh3cTwamplightTWDelayAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayAvgJitter.setStatus("current")
_Hh3cTwamplightTWDelayMaxJitter_Type = Integer32
_Hh3cTwamplightTWDelayMaxJitter_Object = MibTableColumn
hh3cTwamplightTWDelayMaxJitter = _Hh3cTwamplightTWDelayMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 6),
    _Hh3cTwamplightTWDelayMaxJitter_Type()
)
hh3cTwamplightTWDelayMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMaxJitter.setStatus("current")
_Hh3cTwamplightTWDelayMinJitter_Type = Integer32
_Hh3cTwamplightTWDelayMinJitter_Object = MibTableColumn
hh3cTwamplightTWDelayMinJitter = _Hh3cTwamplightTWDelayMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 7),
    _Hh3cTwamplightTWDelayMinJitter_Type()
)
hh3cTwamplightTWDelayMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMinJitter.setStatus("current")
_Hh3cTwamplightTWDelayAvgJitterSD_Type = Integer32
_Hh3cTwamplightTWDelayAvgJitterSD_Object = MibTableColumn
hh3cTwamplightTWDelayAvgJitterSD = _Hh3cTwamplightTWDelayAvgJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 8),
    _Hh3cTwamplightTWDelayAvgJitterSD_Type()
)
hh3cTwamplightTWDelayAvgJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayAvgJitterSD.setStatus("current")
_Hh3cTwamplightTWDelayMaxJitterSD_Type = Integer32
_Hh3cTwamplightTWDelayMaxJitterSD_Object = MibTableColumn
hh3cTwamplightTWDelayMaxJitterSD = _Hh3cTwamplightTWDelayMaxJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 9),
    _Hh3cTwamplightTWDelayMaxJitterSD_Type()
)
hh3cTwamplightTWDelayMaxJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMaxJitterSD.setStatus("current")
_Hh3cTwamplightTWDelayMinJitterSD_Type = Integer32
_Hh3cTwamplightTWDelayMinJitterSD_Object = MibTableColumn
hh3cTwamplightTWDelayMinJitterSD = _Hh3cTwamplightTWDelayMinJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 10),
    _Hh3cTwamplightTWDelayMinJitterSD_Type()
)
hh3cTwamplightTWDelayMinJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMinJitterSD.setStatus("current")
_Hh3cTwamplightTWDelayAvgJitterDS_Type = Integer32
_Hh3cTwamplightTWDelayAvgJitterDS_Object = MibTableColumn
hh3cTwamplightTWDelayAvgJitterDS = _Hh3cTwamplightTWDelayAvgJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 11),
    _Hh3cTwamplightTWDelayAvgJitterDS_Type()
)
hh3cTwamplightTWDelayAvgJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayAvgJitterDS.setStatus("current")
_Hh3cTwamplightTWDelayMaxJitterDS_Type = Integer32
_Hh3cTwamplightTWDelayMaxJitterDS_Object = MibTableColumn
hh3cTwamplightTWDelayMaxJitterDS = _Hh3cTwamplightTWDelayMaxJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 12),
    _Hh3cTwamplightTWDelayMaxJitterDS_Type()
)
hh3cTwamplightTWDelayMaxJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMaxJitterDS.setStatus("current")
_Hh3cTwamplightTWDelayMinJitterDS_Type = Integer32
_Hh3cTwamplightTWDelayMinJitterDS_Object = MibTableColumn
hh3cTwamplightTWDelayMinJitterDS = _Hh3cTwamplightTWDelayMinJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 6, 1, 13),
    _Hh3cTwamplightTWDelayMinJitterDS_Type()
)
hh3cTwamplightTWDelayMinJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWDelayMinJitterDS.setStatus("current")
_Hh3cTwamplightTwoWayLossTable_Object = MibTable
hh3cTwamplightTwoWayLossTable = _Hh3cTwamplightTwoWayLossTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cTwamplightTwoWayLossTable.setStatus("current")
_Hh3cTwamplightTwoWayLossEntry_Object = MibTableRow
hh3cTwamplightTwoWayLossEntry = _Hh3cTwamplightTwoWayLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1)
)
hh3cTwamplightTwoWayLossEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightTWLossSeq"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightTwoWayLossEntry.setStatus("current")


class _Hh3cTwamplightTWLossSeq_Type(Gauge32):
    """Custom type hh3cTwamplightTWLossSeq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cTwamplightTWLossSeq_Type.__name__ = "Gauge32"
_Hh3cTwamplightTWLossSeq_Object = MibTableColumn
hh3cTwamplightTWLossSeq = _Hh3cTwamplightTWLossSeq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1, 1),
    _Hh3cTwamplightTWLossSeq_Type()
)
hh3cTwamplightTWLossSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWLossSeq.setStatus("current")
_Hh3cTwamplightTWLossValue_Type = Integer32
_Hh3cTwamplightTWLossValue_Object = MibTableColumn
hh3cTwamplightTWLossValue = _Hh3cTwamplightTWLossValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1, 2),
    _Hh3cTwamplightTWLossValue_Type()
)
hh3cTwamplightTWLossValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWLossValue.setStatus("current")
_Hh3cTwamplightTWSentCount_Type = Integer32
_Hh3cTwamplightTWSentCount_Object = MibTableColumn
hh3cTwamplightTWSentCount = _Hh3cTwamplightTWSentCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1, 3),
    _Hh3cTwamplightTWSentCount_Type()
)
hh3cTwamplightTWSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWSentCount.setStatus("current")
_Hh3cTwamplightTWTotalLossValue_Type = Integer32
_Hh3cTwamplightTWTotalLossValue_Object = MibTableColumn
hh3cTwamplightTWTotalLossValue = _Hh3cTwamplightTWTotalLossValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1, 4),
    _Hh3cTwamplightTWTotalLossValue_Type()
)
hh3cTwamplightTWTotalLossValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWTotalLossValue.setStatus("current")
_Hh3cTwamplightTWTotalSentCount_Type = Integer32
_Hh3cTwamplightTWTotalSentCount_Object = MibTableColumn
hh3cTwamplightTWTotalSentCount = _Hh3cTwamplightTWTotalSentCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1, 5),
    _Hh3cTwamplightTWTotalSentCount_Type()
)
hh3cTwamplightTWTotalSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWTotalSentCount.setStatus("current")
_Hh3cTwamplightTWErrorCount_Type = Unsigned32
_Hh3cTwamplightTWErrorCount_Object = MibTableColumn
hh3cTwamplightTWErrorCount = _Hh3cTwamplightTWErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1, 6),
    _Hh3cTwamplightTWErrorCount_Type()
)
hh3cTwamplightTWErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWErrorCount.setStatus("current")
_Hh3cTwamplightTWTotalErrorCount_Type = Unsigned32
_Hh3cTwamplightTWTotalErrorCount_Object = MibTableColumn
hh3cTwamplightTWTotalErrorCount = _Hh3cTwamplightTWTotalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 7, 1, 7),
    _Hh3cTwamplightTWTotalErrorCount_Type()
)
hh3cTwamplightTWTotalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightTWTotalErrorCount.setStatus("current")
_Hh3cTwamplightSenderLossSeqTable_Object = MibTable
hh3cTwamplightSenderLossSeqTable = _Hh3cTwamplightSenderLossSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cTwamplightSenderLossSeqTable.setStatus("current")
_Hh3cTwamplightSenderLossSeqEntry_Object = MibTableRow
hh3cTwamplightSenderLossSeqEntry = _Hh3cTwamplightSenderLossSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 8, 1)
)
hh3cTwamplightSenderLossSeqEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightSenderLossSeqEntry.setStatus("current")


class _Hh3cTwamplightLossSeqNumValue_Type(Gauge32):
    """Custom type hh3cTwamplightLossSeqNumValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cTwamplightLossSeqNumValue_Type.__name__ = "Gauge32"
_Hh3cTwamplightLossSeqNumValue_Object = MibTableColumn
hh3cTwamplightLossSeqNumValue = _Hh3cTwamplightLossSeqNumValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 8, 1, 1),
    _Hh3cTwamplightLossSeqNumValue_Type()
)
hh3cTwamplightLossSeqNumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightLossSeqNumValue.setStatus("current")
_Hh3cTwamplightSendDelaySeqTable_Object = MibTable
hh3cTwamplightSendDelaySeqTable = _Hh3cTwamplightSendDelaySeqTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cTwamplightSendDelaySeqTable.setStatus("current")
_Hh3cTwamplightSendDelaySeqEntry_Object = MibTableRow
hh3cTwamplightSendDelaySeqEntry = _Hh3cTwamplightSendDelaySeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 9, 1)
)
hh3cTwamplightSendDelaySeqEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightSendDelaySeqEntry.setStatus("current")


class _Hh3cTwamplightSenderDelaySeqNum_Type(Gauge32):
    """Custom type hh3cTwamplightSenderDelaySeqNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cTwamplightSenderDelaySeqNum_Type.__name__ = "Gauge32"
_Hh3cTwamplightSenderDelaySeqNum_Object = MibTableColumn
hh3cTwamplightSenderDelaySeqNum = _Hh3cTwamplightSenderDelaySeqNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 9, 1, 1),
    _Hh3cTwamplightSenderDelaySeqNum_Type()
)
hh3cTwamplightSenderDelaySeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTwamplightSenderDelaySeqNum.setStatus("current")
_Hh3cTwamplightResetStatTable_Object = MibTable
hh3cTwamplightResetStatTable = _Hh3cTwamplightResetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cTwamplightResetStatTable.setStatus("current")
_Hh3cTwamplightResetStatEntry_Object = MibTableRow
hh3cTwamplightResetStatEntry = _Hh3cTwamplightResetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 10, 1)
)
hh3cTwamplightResetStatEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightResetStatEntry.setStatus("current")


class _Hh3cTwamplightResetStatistics_Type(Integer32):
    """Custom type hh3cTwamplightResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("all", 2))
    )


_Hh3cTwamplightResetStatistics_Type.__name__ = "Integer32"
_Hh3cTwamplightResetStatistics_Object = MibTableColumn
hh3cTwamplightResetStatistics = _Hh3cTwamplightResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 10, 1, 1),
    _Hh3cTwamplightResetStatistics_Type()
)
hh3cTwamplightResetStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightResetStatistics.setStatus("current")
_Hh3cTwamplightReactionTable_Object = MibTable
hh3cTwamplightReactionTable = _Hh3cTwamplightReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cTwamplightReactionTable.setStatus("current")
_Hh3cTwamplightReactionEntry_Object = MibTableRow
hh3cTwamplightReactionEntry = _Hh3cTwamplightReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11, 1)
)
hh3cTwamplightReactionEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightControllerID"),
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightReactItemIndex"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightReactionEntry.setStatus("current")


class _Hh3cTwamplightReactItemIndex_Type(Unsigned32):
    """Custom type hh3cTwamplightReactItemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cTwamplightReactItemIndex_Type.__name__ = "Unsigned32"
_Hh3cTwamplightReactItemIndex_Object = MibTableColumn
hh3cTwamplightReactItemIndex = _Hh3cTwamplightReactItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11, 1, 1),
    _Hh3cTwamplightReactItemIndex_Type()
)
hh3cTwamplightReactItemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTwamplightReactItemIndex.setStatus("current")


class _Hh3cTwamplightReactCheckElement_Type(Integer32):
    """Custom type hh3cTwamplightReactCheckElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twoWayDelay", 1),
          ("twoWayJitter", 2),
          ("twoWayLoss", 3))
    )


_Hh3cTwamplightReactCheckElement_Type.__name__ = "Integer32"
_Hh3cTwamplightReactCheckElement_Object = MibTableColumn
hh3cTwamplightReactCheckElement = _Hh3cTwamplightReactCheckElement_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11, 1, 2),
    _Hh3cTwamplightReactCheckElement_Type()
)
hh3cTwamplightReactCheckElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightReactCheckElement.setStatus("current")


class _Hh3cTwamplightReactUpperLimit_Type(Unsigned32):
    """Custom type hh3cTwamplightReactUpperLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000000),
    )


_Hh3cTwamplightReactUpperLimit_Type.__name__ = "Unsigned32"
_Hh3cTwamplightReactUpperLimit_Object = MibTableColumn
hh3cTwamplightReactUpperLimit = _Hh3cTwamplightReactUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11, 1, 3),
    _Hh3cTwamplightReactUpperLimit_Type()
)
hh3cTwamplightReactUpperLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightReactUpperLimit.setStatus("current")


class _Hh3cTwamplightReactLowerLimit_Type(Unsigned32):
    """Custom type hh3cTwamplightReactLowerLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_Hh3cTwamplightReactLowerLimit_Type.__name__ = "Unsigned32"
_Hh3cTwamplightReactLowerLimit_Object = MibTableColumn
hh3cTwamplightReactLowerLimit = _Hh3cTwamplightReactLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11, 1, 4),
    _Hh3cTwamplightReactLowerLimit_Type()
)
hh3cTwamplightReactLowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightReactLowerLimit.setStatus("current")


class _Hh3cTwamplightReactActionType_Type(Integer32):
    """Custom type hh3cTwamplightReactActionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trapOnly", 1))
    )


_Hh3cTwamplightReactActionType_Type.__name__ = "Integer32"
_Hh3cTwamplightReactActionType_Object = MibTableColumn
hh3cTwamplightReactActionType = _Hh3cTwamplightReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11, 1, 5),
    _Hh3cTwamplightReactActionType_Type()
)
hh3cTwamplightReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightReactActionType.setStatus("current")
_Hh3cTwamplightReactRowStatus_Type = RowStatus
_Hh3cTwamplightReactRowStatus_Object = MibTableColumn
hh3cTwamplightReactRowStatus = _Hh3cTwamplightReactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 1, 11, 1, 6),
    _Hh3cTwamplightReactRowStatus_Type()
)
hh3cTwamplightReactRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightReactRowStatus.setStatus("current")
_Hh3cTwamplightReponsder_ObjectIdentity = ObjectIdentity
hh3cTwamplightReponsder = _Hh3cTwamplightReponsder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2)
)


class _Hh3cTwamplightResponderEnable_Type(TruthValue):
    """Custom type hh3cTwamplightResponderEnable based on TruthValue"""
    defaultValue = 2


_Hh3cTwamplightResponderEnable_Type.__name__ = "TruthValue"
_Hh3cTwamplightResponderEnable_Object = MibScalar
hh3cTwamplightResponderEnable = _Hh3cTwamplightResponderEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 1),
    _Hh3cTwamplightResponderEnable_Type()
)
hh3cTwamplightResponderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTwamplightResponderEnable.setStatus("current")
_Hh3cTwamplightResponderTable_Object = MibTable
hh3cTwamplightResponderTable = _Hh3cTwamplightResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cTwamplightResponderTable.setStatus("current")
_Hh3cTwamplightResponderEntry_Object = MibTableRow
hh3cTwamplightResponderEntry = _Hh3cTwamplightResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1)
)
hh3cTwamplightResponderEntry.setIndexNames(
    (0, "HH3C-TWAMP-MIB", "hh3cTwamplightRespID"),
)
if mibBuilder.loadTexts:
    hh3cTwamplightResponderEntry.setStatus("current")
_Hh3cTwamplightRespID_Type = Integer32
_Hh3cTwamplightRespID_Object = MibTableColumn
hh3cTwamplightRespID = _Hh3cTwamplightRespID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 1),
    _Hh3cTwamplightRespID_Type()
)
hh3cTwamplightRespID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTwamplightRespID.setStatus("current")
_Hh3cTwamplightRespSrcAddrType_Type = InetAddressType
_Hh3cTwamplightRespSrcAddrType_Object = MibTableColumn
hh3cTwamplightRespSrcAddrType = _Hh3cTwamplightRespSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 2),
    _Hh3cTwamplightRespSrcAddrType_Type()
)
hh3cTwamplightRespSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespSrcAddrType.setStatus("current")


class _Hh3cTwamplightRespSrcAddr_Type(InetAddress):
    """Custom type hh3cTwamplightRespSrcAddr based on InetAddress"""
    defaultHexValue = ""


_Hh3cTwamplightRespSrcAddr_Type.__name__ = "InetAddress"
_Hh3cTwamplightRespSrcAddr_Object = MibTableColumn
hh3cTwamplightRespSrcAddr = _Hh3cTwamplightRespSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 3),
    _Hh3cTwamplightRespSrcAddr_Type()
)
hh3cTwamplightRespSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespSrcAddr.setStatus("current")
_Hh3cTwamplightRespTrgtAddrType_Type = InetAddressType
_Hh3cTwamplightRespTrgtAddrType_Object = MibTableColumn
hh3cTwamplightRespTrgtAddrType = _Hh3cTwamplightRespTrgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 4),
    _Hh3cTwamplightRespTrgtAddrType_Type()
)
hh3cTwamplightRespTrgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespTrgtAddrType.setStatus("current")


class _Hh3cTwamplightRespTrgtAddr_Type(InetAddress):
    """Custom type hh3cTwamplightRespTrgtAddr based on InetAddress"""
    defaultHexValue = ""


_Hh3cTwamplightRespTrgtAddr_Type.__name__ = "InetAddress"
_Hh3cTwamplightRespTrgtAddr_Object = MibTableColumn
hh3cTwamplightRespTrgtAddr = _Hh3cTwamplightRespTrgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 5),
    _Hh3cTwamplightRespTrgtAddr_Type()
)
hh3cTwamplightRespTrgtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespTrgtAddr.setStatus("current")


class _Hh3cTwamplightRespSrcPort_Type(Integer32):
    """Custom type hh3cTwamplightRespSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cTwamplightRespSrcPort_Type.__name__ = "Integer32"
_Hh3cTwamplightRespSrcPort_Object = MibTableColumn
hh3cTwamplightRespSrcPort = _Hh3cTwamplightRespSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 6),
    _Hh3cTwamplightRespSrcPort_Type()
)
hh3cTwamplightRespSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespSrcPort.setStatus("current")


class _Hh3cTwamplightRespTrgtPort_Type(Integer32):
    """Custom type hh3cTwamplightRespTrgtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cTwamplightRespTrgtPort_Type.__name__ = "Integer32"
_Hh3cTwamplightRespTrgtPort_Object = MibTableColumn
hh3cTwamplightRespTrgtPort = _Hh3cTwamplightRespTrgtPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 7),
    _Hh3cTwamplightRespTrgtPort_Type()
)
hh3cTwamplightRespTrgtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespTrgtPort.setStatus("current")


class _Hh3cTwamplightRespVPN_Type(DisplayString):
    """Custom type hh3cTwamplightRespVPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cTwamplightRespVPN_Type.__name__ = "DisplayString"
_Hh3cTwamplightRespVPN_Object = MibTableColumn
hh3cTwamplightRespVPN = _Hh3cTwamplightRespVPN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 8),
    _Hh3cTwamplightRespVPN_Type()
)
hh3cTwamplightRespVPN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespVPN.setStatus("current")


class _Hh3cTwamplightRespDescription_Type(DisplayString):
    """Custom type hh3cTwamplightRespDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_Hh3cTwamplightRespDescription_Type.__name__ = "DisplayString"
_Hh3cTwamplightRespDescription_Object = MibTableColumn
hh3cTwamplightRespDescription = _Hh3cTwamplightRespDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 9),
    _Hh3cTwamplightRespDescription_Type()
)
hh3cTwamplightRespDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespDescription.setStatus("current")
_Hh3cTwamplightRespRowStatus_Type = RowStatus
_Hh3cTwamplightRespRowStatus_Object = MibTableColumn
hh3cTwamplightRespRowStatus = _Hh3cTwamplightRespRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 10),
    _Hh3cTwamplightRespRowStatus_Type()
)
hh3cTwamplightRespRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespRowStatus.setStatus("current")


class _Hh3cTwamplightRespSrcIfName_Type(DisplayString):
    """Custom type hh3cTwamplightRespSrcIfName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3cTwamplightRespSrcIfName_Type.__name__ = "DisplayString"
_Hh3cTwamplightRespSrcIfName_Object = MibTableColumn
hh3cTwamplightRespSrcIfName = _Hh3cTwamplightRespSrcIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 11),
    _Hh3cTwamplightRespSrcIfName_Type()
)
hh3cTwamplightRespSrcIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespSrcIfName.setStatus("current")


class _Hh3cTwamplightRespServiceID_Type(Unsigned32):
    """Custom type hh3cTwamplightRespServiceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Hh3cTwamplightRespServiceID_Type.__name__ = "Unsigned32"
_Hh3cTwamplightRespServiceID_Object = MibTableColumn
hh3cTwamplightRespServiceID = _Hh3cTwamplightRespServiceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 12),
    _Hh3cTwamplightRespServiceID_Type()
)
hh3cTwamplightRespServiceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespServiceID.setStatus("current")
if mibBuilder.loadTexts:
    hh3cTwamplightRespServiceID.setUnits("octets")
_Hh3cTwamplightRespDesMac_Type = MacAddress
_Hh3cTwamplightRespDesMac_Object = MibTableColumn
hh3cTwamplightRespDesMac = _Hh3cTwamplightRespDesMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 13),
    _Hh3cTwamplightRespDesMac_Type()
)
hh3cTwamplightRespDesMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespDesMac.setStatus("current")
_Hh3cTwamplightRespSrcMac_Type = MacAddress
_Hh3cTwamplightRespSrcMac_Object = MibTableColumn
hh3cTwamplightRespSrcMac = _Hh3cTwamplightRespSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 14),
    _Hh3cTwamplightRespSrcMac_Type()
)
hh3cTwamplightRespSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespSrcMac.setStatus("current")


class _Hh3cTwamplightRespTimeFormat_Type(Integer32):
    """Custom type hh3cTwamplightRespTimeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("ntp", 1),
          ("ptp", 2))
    )


_Hh3cTwamplightRespTimeFormat_Type.__name__ = "Integer32"
_Hh3cTwamplightRespTimeFormat_Object = MibTableColumn
hh3cTwamplightRespTimeFormat = _Hh3cTwamplightRespTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 15),
    _Hh3cTwamplightRespTimeFormat_Type()
)
hh3cTwamplightRespTimeFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespTimeFormat.setStatus("current")


class _Hh3cTwamplightRespSVlanID_Type(Unsigned32):
    """Custom type hh3cTwamplightRespSVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cTwamplightRespSVlanID_Type.__name__ = "Unsigned32"
_Hh3cTwamplightRespSVlanID_Object = MibTableColumn
hh3cTwamplightRespSVlanID = _Hh3cTwamplightRespSVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 16),
    _Hh3cTwamplightRespSVlanID_Type()
)
hh3cTwamplightRespSVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespSVlanID.setStatus("current")


class _Hh3cTwamplightRespCVlanID_Type(Unsigned32):
    """Custom type hh3cTwamplightRespCVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cTwamplightRespCVlanID_Type.__name__ = "Unsigned32"
_Hh3cTwamplightRespCVlanID_Object = MibTableColumn
hh3cTwamplightRespCVlanID = _Hh3cTwamplightRespCVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 184, 2, 2, 2, 1, 17),
    _Hh3cTwamplightRespCVlanID_Type()
)
hh3cTwamplightRespCVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTwamplightRespCVlanID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-TWAMP-MIB",
    **{"hh3cTwamp": hh3cTwamp,
       "hh3cTwampNotifications": hh3cTwampNotifications,
       "hh3cTwamplightObjects": hh3cTwamplightObjects,
       "hh3cTwamplightController": hh3cTwamplightController,
       "hh3cTwamplightClientEnable": hh3cTwamplightClientEnable,
       "hh3cTwamplightSenderEnable": hh3cTwamplightSenderEnable,
       "hh3cTwamplightClientTable": hh3cTwamplightClientTable,
       "hh3cTwamplightClientEntry": hh3cTwamplightClientEntry,
       "hh3cTwamplightControllerID": hh3cTwamplightControllerID,
       "hh3cTwamplightClientSrcAddrType": hh3cTwamplightClientSrcAddrType,
       "hh3cTwamplightClientSrcAddr": hh3cTwamplightClientSrcAddr,
       "hh3cTwamplightClientTrgtAddrType": hh3cTwamplightClientTrgtAddrType,
       "hh3cTwamplightClientTrgtAddr": hh3cTwamplightClientTrgtAddr,
       "hh3cTwamplightClientSrcPort": hh3cTwamplightClientSrcPort,
       "hh3cTwamplightClientTrgtPort": hh3cTwamplightClientTrgtPort,
       "hh3cTwamplightClientVPN": hh3cTwamplightClientVPN,
       "hh3cTwamplightClientDscp": hh3cTwamplightClientDscp,
       "hh3cTwamplightClientDataSize": hh3cTwamplightClientDataSize,
       "hh3cTwamplightClientDescription": hh3cTwamplightClientDescription,
       "hh3cTwamplightClientRowStatus": hh3cTwamplightClientRowStatus,
       "hh3cTwamplightClientSrcIfName": hh3cTwamplightClientSrcIfName,
       "hh3cTwamplightClientServiceID": hh3cTwamplightClientServiceID,
       "hh3cTwamplightClientDesMac": hh3cTwamplightClientDesMac,
       "hh3cTwamplightClientSrcMac": hh3cTwamplightClientSrcMac,
       "hh3cTwamplightClientTimeFormat": hh3cTwamplightClientTimeFormat,
       "hh3cTwamplightClientDataFill": hh3cTwamplightClientDataFill,
       "hh3cTwamplightClientDataFillType": hh3cTwamplightClientDataFillType,
       "hh3cTwamplightClientSVlanID": hh3cTwamplightClientSVlanID,
       "hh3cTwamplightClientCVlanID": hh3cTwamplightClientCVlanID,
       "hh3cTwamplightClientVlanPriority": hh3cTwamplightClientVlanPriority,
       "hh3cTwamplightClientBindIfName": hh3cTwamplightClientBindIfName,
       "hh3cTwamplightSenderAdminTable": hh3cTwamplightSenderAdminTable,
       "hh3cTwamplightSenderAdminEntry": hh3cTwamplightSenderAdminEntry,
       "hh3cTwamplightSendAdminContinual": hh3cTwamplightSendAdminContinual,
       "hh3cTwamplightSendAdminDuration": hh3cTwamplightSendAdminDuration,
       "hh3cTwamplightSendAdminPktCount": hh3cTwamplightSendAdminPktCount,
       "hh3cTwamplightSendAdminTxPeriod": hh3cTwamplightSendAdminTxPeriod,
       "hh3cTwamplightSendAdminTimeOut": hh3cTwamplightSendAdminTimeOut,
       "hh3cTwamplightSendAdminRowStatus": hh3cTwamplightSendAdminRowStatus,
       "hh3cTwamplightSenderStatusTable": hh3cTwamplightSenderStatusTable,
       "hh3cTwamplightSenderStatusEntry": hh3cTwamplightSenderStatusEntry,
       "hh3cTwamplightSenderStatus": hh3cTwamplightSenderStatus,
       "hh3cTwamplightSenderStatusType": hh3cTwamplightSenderStatusType,
       "hh3cTwamplightLastStartTime": hh3cTwamplightLastStartTime,
       "hh3cTwamplightLastStopTime": hh3cTwamplightLastStopTime,
       "hh3cTwamplightTwoWayDelayTable": hh3cTwamplightTwoWayDelayTable,
       "hh3cTwamplightTwoWayDelayEntry": hh3cTwamplightTwoWayDelayEntry,
       "hh3cTwamplightTWDelaySeq": hh3cTwamplightTWDelaySeq,
       "hh3cTwamplightTWDelayAvgDelay": hh3cTwamplightTWDelayAvgDelay,
       "hh3cTwamplightTWDelayMaxDelay": hh3cTwamplightTWDelayMaxDelay,
       "hh3cTwamplightTWDelayMinDelay": hh3cTwamplightTWDelayMinDelay,
       "hh3cTwamplightTWDelayAvgJitter": hh3cTwamplightTWDelayAvgJitter,
       "hh3cTwamplightTWDelayMaxJitter": hh3cTwamplightTWDelayMaxJitter,
       "hh3cTwamplightTWDelayMinJitter": hh3cTwamplightTWDelayMinJitter,
       "hh3cTwamplightTWDelayAvgJitterSD": hh3cTwamplightTWDelayAvgJitterSD,
       "hh3cTwamplightTWDelayMaxJitterSD": hh3cTwamplightTWDelayMaxJitterSD,
       "hh3cTwamplightTWDelayMinJitterSD": hh3cTwamplightTWDelayMinJitterSD,
       "hh3cTwamplightTWDelayAvgJitterDS": hh3cTwamplightTWDelayAvgJitterDS,
       "hh3cTwamplightTWDelayMaxJitterDS": hh3cTwamplightTWDelayMaxJitterDS,
       "hh3cTwamplightTWDelayMinJitterDS": hh3cTwamplightTWDelayMinJitterDS,
       "hh3cTwamplightTwoWayLossTable": hh3cTwamplightTwoWayLossTable,
       "hh3cTwamplightTwoWayLossEntry": hh3cTwamplightTwoWayLossEntry,
       "hh3cTwamplightTWLossSeq": hh3cTwamplightTWLossSeq,
       "hh3cTwamplightTWLossValue": hh3cTwamplightTWLossValue,
       "hh3cTwamplightTWSentCount": hh3cTwamplightTWSentCount,
       "hh3cTwamplightTWTotalLossValue": hh3cTwamplightTWTotalLossValue,
       "hh3cTwamplightTWTotalSentCount": hh3cTwamplightTWTotalSentCount,
       "hh3cTwamplightTWErrorCount": hh3cTwamplightTWErrorCount,
       "hh3cTwamplightTWTotalErrorCount": hh3cTwamplightTWTotalErrorCount,
       "hh3cTwamplightSenderLossSeqTable": hh3cTwamplightSenderLossSeqTable,
       "hh3cTwamplightSenderLossSeqEntry": hh3cTwamplightSenderLossSeqEntry,
       "hh3cTwamplightLossSeqNumValue": hh3cTwamplightLossSeqNumValue,
       "hh3cTwamplightSendDelaySeqTable": hh3cTwamplightSendDelaySeqTable,
       "hh3cTwamplightSendDelaySeqEntry": hh3cTwamplightSendDelaySeqEntry,
       "hh3cTwamplightSenderDelaySeqNum": hh3cTwamplightSenderDelaySeqNum,
       "hh3cTwamplightResetStatTable": hh3cTwamplightResetStatTable,
       "hh3cTwamplightResetStatEntry": hh3cTwamplightResetStatEntry,
       "hh3cTwamplightResetStatistics": hh3cTwamplightResetStatistics,
       "hh3cTwamplightReactionTable": hh3cTwamplightReactionTable,
       "hh3cTwamplightReactionEntry": hh3cTwamplightReactionEntry,
       "hh3cTwamplightReactItemIndex": hh3cTwamplightReactItemIndex,
       "hh3cTwamplightReactCheckElement": hh3cTwamplightReactCheckElement,
       "hh3cTwamplightReactUpperLimit": hh3cTwamplightReactUpperLimit,
       "hh3cTwamplightReactLowerLimit": hh3cTwamplightReactLowerLimit,
       "hh3cTwamplightReactActionType": hh3cTwamplightReactActionType,
       "hh3cTwamplightReactRowStatus": hh3cTwamplightReactRowStatus,
       "hh3cTwamplightReponsder": hh3cTwamplightReponsder,
       "hh3cTwamplightResponderEnable": hh3cTwamplightResponderEnable,
       "hh3cTwamplightResponderTable": hh3cTwamplightResponderTable,
       "hh3cTwamplightResponderEntry": hh3cTwamplightResponderEntry,
       "hh3cTwamplightRespID": hh3cTwamplightRespID,
       "hh3cTwamplightRespSrcAddrType": hh3cTwamplightRespSrcAddrType,
       "hh3cTwamplightRespSrcAddr": hh3cTwamplightRespSrcAddr,
       "hh3cTwamplightRespTrgtAddrType": hh3cTwamplightRespTrgtAddrType,
       "hh3cTwamplightRespTrgtAddr": hh3cTwamplightRespTrgtAddr,
       "hh3cTwamplightRespSrcPort": hh3cTwamplightRespSrcPort,
       "hh3cTwamplightRespTrgtPort": hh3cTwamplightRespTrgtPort,
       "hh3cTwamplightRespVPN": hh3cTwamplightRespVPN,
       "hh3cTwamplightRespDescription": hh3cTwamplightRespDescription,
       "hh3cTwamplightRespRowStatus": hh3cTwamplightRespRowStatus,
       "hh3cTwamplightRespSrcIfName": hh3cTwamplightRespSrcIfName,
       "hh3cTwamplightRespServiceID": hh3cTwamplightRespServiceID,
       "hh3cTwamplightRespDesMac": hh3cTwamplightRespDesMac,
       "hh3cTwamplightRespSrcMac": hh3cTwamplightRespSrcMac,
       "hh3cTwamplightRespTimeFormat": hh3cTwamplightRespTimeFormat,
       "hh3cTwamplightRespSVlanID": hh3cTwamplightRespSVlanID,
       "hh3cTwamplightRespCVlanID": hh3cTwamplightRespCVlanID}
)
