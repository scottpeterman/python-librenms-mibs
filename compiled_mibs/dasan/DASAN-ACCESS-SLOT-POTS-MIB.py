# SNMP MIB module (DASAN-ACCESS-SLOT-POTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-ACCESS-SLOT-POTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:56 2025
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

(dasanMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 iso,
 mib_2) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

dasanAccessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100)
)
if mibBuilder.loadTexts:
    dasanAccessMib.setRevisions(
        ("2005-02-11 21:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanAccGatewayMIBObjects_ObjectIdentity = ObjectIdentity
dasanAccGatewayMIBObjects = _DasanAccGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2)
)
_DsAccGwyPots_ObjectIdentity = ObjectIdentity
dsAccGwyPots = _DsAccGwyPots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1)
)
_DsAccGwyPotsConfiguration_ObjectIdentity = ObjectIdentity
dsAccGwyPotsConfiguration = _DsAccGwyPotsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1)
)
_DsAccGwyConfigPotsSystem_ObjectIdentity = ObjectIdentity
dsAccGwyConfigPotsSystem = _DsAccGwyConfigPotsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 1)
)


class _DsAccGwyConfigGlobalDigitmap_Type(DisplayString):
    """Custom type dsAccGwyConfigGlobalDigitmap based on DisplayString"""
    defaultValue = OctetString("x.T")


_DsAccGwyConfigGlobalDigitmap_Type.__name__ = "DisplayString"
_DsAccGwyConfigGlobalDigitmap_Object = MibScalar
dsAccGwyConfigGlobalDigitmap = _DsAccGwyConfigGlobalDigitmap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 1, 1),
    _DsAccGwyConfigGlobalDigitmap_Type()
)
dsAccGwyConfigGlobalDigitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAccGwyConfigGlobalDigitmap.setStatus("current")


class _DsAccGwyConfigGlobalSwitchDhcp_Type(DisplayString):
    """Custom type dsAccGwyConfigGlobalSwitchDhcp based on DisplayString"""
    defaultValue = OctetString("off")


_DsAccGwyConfigGlobalSwitchDhcp_Type.__name__ = "DisplayString"
_DsAccGwyConfigGlobalSwitchDhcp_Object = MibScalar
dsAccGwyConfigGlobalSwitchDhcp = _DsAccGwyConfigGlobalSwitchDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 1, 2),
    _DsAccGwyConfigGlobalSwitchDhcp_Type()
)
dsAccGwyConfigGlobalSwitchDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAccGwyConfigGlobalSwitchDhcp.setStatus("current")
_DsAccGwyConfigPotsSlot_ObjectIdentity = ObjectIdentity
dsAccGwyConfigPotsSlot = _DsAccGwyConfigPotsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2)
)
_DsAccGwyConfigSlotTable_Object = MibTable
dsAccGwyConfigSlotTable = _DsAccGwyConfigSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSlotTable.setStatus("current")
_DsAccGwyConfigSlotEntry_Object = MibTableRow
dsAccGwyConfigSlotEntry = _DsAccGwyConfigSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1)
)
dsAccGwyConfigSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-POTS-MIB", "dsSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSlotEntry.setStatus("current")
_DsSlotIndex_Type = Integer32
_DsSlotIndex_Object = MibTableColumn
dsSlotIndex = _DsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 1),
    _DsSlotIndex_Type()
)
dsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotIndex.setStatus("current")


class _DsSlotAddAreaCode_Type(Integer32):
    """Custom type dsSlotAddAreaCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DsSlotAddAreaCode_Type.__name__ = "Integer32"
_DsSlotAddAreaCode_Object = MibTableColumn
dsSlotAddAreaCode = _DsSlotAddAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 2),
    _DsSlotAddAreaCode_Type()
)
dsSlotAddAreaCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotAddAreaCode.setStatus("current")


class _DsSlotAreaCode_Type(DisplayString):
    """Custom type dsSlotAreaCode based on DisplayString"""
    defaultValue = OctetString("")


_DsSlotAreaCode_Type.__name__ = "DisplayString"
_DsSlotAreaCode_Object = MibTableColumn
dsSlotAreaCode = _DsSlotAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 3),
    _DsSlotAreaCode_Type()
)
dsSlotAreaCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotAreaCode.setStatus("current")


class _DsSlotAreaCodeAllows_Type(DisplayString):
    """Custom type dsSlotAreaCodeAllows based on DisplayString"""
    defaultValue = OctetString("")


_DsSlotAreaCodeAllows_Type.__name__ = "DisplayString"
_DsSlotAreaCodeAllows_Object = MibTableColumn
dsSlotAreaCodeAllows = _DsSlotAreaCodeAllows_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 4),
    _DsSlotAreaCodeAllows_Type()
)
dsSlotAreaCodeAllows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotAreaCodeAllows.setStatus("current")


class _DsSlotAreaCodeExceptions_Type(DisplayString):
    """Custom type dsSlotAreaCodeExceptions based on DisplayString"""
    defaultValue = OctetString("")


_DsSlotAreaCodeExceptions_Type.__name__ = "DisplayString"
_DsSlotAreaCodeExceptions_Object = MibTableColumn
dsSlotAreaCodeExceptions = _DsSlotAreaCodeExceptions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 5),
    _DsSlotAreaCodeExceptions_Type()
)
dsSlotAreaCodeExceptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotAreaCodeExceptions.setStatus("current")


class _DsSlotCodecType_Type(DisplayString):
    """Custom type dsSlotCodecType based on DisplayString"""
    defaultValue = OctetString("")


_DsSlotCodecType_Type.__name__ = "DisplayString"
_DsSlotCodecType_Object = MibTableColumn
dsSlotCodecType = _DsSlotCodecType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 6),
    _DsSlotCodecType_Type()
)
dsSlotCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecType.setStatus("current")
_DsSlotCodecPacketizationPeriodG711_Type = Integer32
_DsSlotCodecPacketizationPeriodG711_Object = MibTableColumn
dsSlotCodecPacketizationPeriodG711 = _DsSlotCodecPacketizationPeriodG711_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 7),
    _DsSlotCodecPacketizationPeriodG711_Type()
)
dsSlotCodecPacketizationPeriodG711.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecPacketizationPeriodG711.setStatus("current")
_DsSlotCodecPacketizationPeriodG723_Type = Integer32
_DsSlotCodecPacketizationPeriodG723_Object = MibTableColumn
dsSlotCodecPacketizationPeriodG723 = _DsSlotCodecPacketizationPeriodG723_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 8),
    _DsSlotCodecPacketizationPeriodG723_Type()
)
dsSlotCodecPacketizationPeriodG723.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecPacketizationPeriodG723.setStatus("current")
_DsSlotCodecPacketizationPeriodG729_Type = Integer32
_DsSlotCodecPacketizationPeriodG729_Object = MibTableColumn
dsSlotCodecPacketizationPeriodG729 = _DsSlotCodecPacketizationPeriodG729_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 9),
    _DsSlotCodecPacketizationPeriodG729_Type()
)
dsSlotCodecPacketizationPeriodG729.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecPacketizationPeriodG729.setStatus("current")


class _DsSlotJitterbuffer_Type(DisplayString):
    """Custom type dsSlotJitterbuffer based on DisplayString"""
    defaultValue = OctetString("")


_DsSlotJitterbuffer_Type.__name__ = "DisplayString"
_DsSlotJitterbuffer_Object = MibTableColumn
dsSlotJitterbuffer = _DsSlotJitterbuffer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 10),
    _DsSlotJitterbuffer_Type()
)
dsSlotJitterbuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotJitterbuffer.setStatus("current")
_DsSlotRingonTime_Type = Integer32
_DsSlotRingonTime_Object = MibTableColumn
dsSlotRingonTime = _DsSlotRingonTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 11),
    _DsSlotRingonTime_Type()
)
dsSlotRingonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotRingonTime.setStatus("current")
_DsSlotRingoffTime_Type = Integer32
_DsSlotRingoffTime_Object = MibTableColumn
dsSlotRingoffTime = _DsSlotRingoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 12),
    _DsSlotRingoffTime_Type()
)
dsSlotRingoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotRingoffTime.setStatus("current")
_DsSlotHookflashMin_Type = Integer32
_DsSlotHookflashMin_Object = MibTableColumn
dsSlotHookflashMin = _DsSlotHookflashMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 13),
    _DsSlotHookflashMin_Type()
)
dsSlotHookflashMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotHookflashMin.setStatus("current")
_DsSlotHookflashMax_Type = Integer32
_DsSlotHookflashMax_Object = MibTableColumn
dsSlotHookflashMax = _DsSlotHookflashMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 14),
    _DsSlotHookflashMax_Type()
)
dsSlotHookflashMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotHookflashMax.setStatus("current")
_DsSlotInterdigitTimeout_Type = Integer32
_DsSlotInterdigitTimeout_Object = MibTableColumn
dsSlotInterdigitTimeout = _DsSlotInterdigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 15),
    _DsSlotInterdigitTimeout_Type()
)
dsSlotInterdigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotInterdigitTimeout.setStatus("current")


class _DsSlotEce_Type(DisplayString):
    """Custom type dsSlotEce based on DisplayString"""
    defaultValue = OctetString("1")


_DsSlotEce_Type.__name__ = "DisplayString"
_DsSlotEce_Object = MibTableColumn
dsSlotEce = _DsSlotEce_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 16),
    _DsSlotEce_Type()
)
dsSlotEce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotEce.setStatus("current")


class _DsSlotFax_Type(Integer32):
    """Custom type dsSlotFax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DsSlotFax_Type.__name__ = "Integer32"
_DsSlotFax_Object = MibTableColumn
dsSlotFax = _DsSlotFax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 17),
    _DsSlotFax_Type()
)
dsSlotFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotFax.setStatus("current")


class _DsSlotCid_Type(Integer32):
    """Custom type dsSlotCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("belcore", 1),
          ("ntt", 2))
    )


_DsSlotCid_Type.__name__ = "Integer32"
_DsSlotCid_Object = MibTableColumn
dsSlotCid = _DsSlotCid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 18),
    _DsSlotCid_Type()
)
dsSlotCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCid.setStatus("current")


class _DsSlotVad_Type(Integer32):
    """Custom type dsSlotVad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DsSlotVad_Type.__name__ = "Integer32"
_DsSlotVad_Object = MibTableColumn
dsSlotVad = _DsSlotVad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 19),
    _DsSlotVad_Type()
)
dsSlotVad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotVad.setStatus("current")


class _DsSlotCng_Type(Integer32):
    """Custom type dsSlotCng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DsSlotCng_Type.__name__ = "Integer32"
_DsSlotCng_Object = MibTableColumn
dsSlotCng = _DsSlotCng_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 20),
    _DsSlotCng_Type()
)
dsSlotCng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCng.setStatus("current")


class _DsSlotOobdtmf_Type(Integer32):
    """Custom type dsSlotOobdtmf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DsSlotOobdtmf_Type.__name__ = "Integer32"
_DsSlotOobdtmf_Object = MibTableColumn
dsSlotOobdtmf = _DsSlotOobdtmf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 21),
    _DsSlotOobdtmf_Type()
)
dsSlotOobdtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotOobdtmf.setStatus("current")


class _DsSlotNetworkHostname_Type(DisplayString):
    """Custom type dsSlotNetworkHostname based on DisplayString"""
    defaultValue = OctetString("")


_DsSlotNetworkHostname_Type.__name__ = "DisplayString"
_DsSlotNetworkHostname_Object = MibTableColumn
dsSlotNetworkHostname = _DsSlotNetworkHostname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 22),
    _DsSlotNetworkHostname_Type()
)
dsSlotNetworkHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotNetworkHostname.setStatus("current")


class _DsSlotNetworkDhcp_Type(Integer32):
    """Custom type dsSlotNetworkDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("on-syslog", 2))
    )


_DsSlotNetworkDhcp_Type.__name__ = "Integer32"
_DsSlotNetworkDhcp_Object = MibTableColumn
dsSlotNetworkDhcp = _DsSlotNetworkDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 23),
    _DsSlotNetworkDhcp_Type()
)
dsSlotNetworkDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkDhcp.setStatus("current")


class _DsSlotNetworkIpaddress_Type(DisplayString):
    """Custom type dsSlotNetworkIpaddress based on DisplayString"""
    defaultValue = OctetString("192.168.1.2")


_DsSlotNetworkIpaddress_Type.__name__ = "DisplayString"
_DsSlotNetworkIpaddress_Object = MibTableColumn
dsSlotNetworkIpaddress = _DsSlotNetworkIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 24),
    _DsSlotNetworkIpaddress_Type()
)
dsSlotNetworkIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkIpaddress.setStatus("current")


class _DsSlotNetworkSubnetmask_Type(DisplayString):
    """Custom type dsSlotNetworkSubnetmask based on DisplayString"""
    defaultValue = OctetString("255.255.255.0")


_DsSlotNetworkSubnetmask_Type.__name__ = "DisplayString"
_DsSlotNetworkSubnetmask_Object = MibTableColumn
dsSlotNetworkSubnetmask = _DsSlotNetworkSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 25),
    _DsSlotNetworkSubnetmask_Type()
)
dsSlotNetworkSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkSubnetmask.setStatus("current")


class _DsSlotNetworkRouter_Type(DisplayString):
    """Custom type dsSlotNetworkRouter based on DisplayString"""
    defaultValue = OctetString("192.168.1.1")


_DsSlotNetworkRouter_Type.__name__ = "DisplayString"
_DsSlotNetworkRouter_Object = MibTableColumn
dsSlotNetworkRouter = _DsSlotNetworkRouter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 26),
    _DsSlotNetworkRouter_Type()
)
dsSlotNetworkRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkRouter.setStatus("current")


class _DsSlotNetworkNameserver_Type(DisplayString):
    """Custom type dsSlotNetworkNameserver based on DisplayString"""
    defaultValue = OctetString("168.126.63.1")


_DsSlotNetworkNameserver_Type.__name__ = "DisplayString"
_DsSlotNetworkNameserver_Object = MibTableColumn
dsSlotNetworkNameserver = _DsSlotNetworkNameserver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 27),
    _DsSlotNetworkNameserver_Type()
)
dsSlotNetworkNameserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkNameserver.setStatus("current")
_DsSlotVersion_Type = DisplayString
_DsSlotVersion_Object = MibTableColumn
dsSlotVersion = _DsSlotVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 2, 1, 1, 28),
    _DsSlotVersion_Type()
)
dsSlotVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotVersion.setStatus("current")
_DsAccGwyConfigPotsPort_ObjectIdentity = ObjectIdentity
dsAccGwyConfigPotsPort = _DsAccGwyConfigPotsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 3)
)
_DsAccGwyConfigPortTable_Object = MibTable
dsAccGwyConfigPortTable = _DsAccGwyConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigPortTable.setStatus("current")
_DsAccGwyConfigPortEntry_Object = MibTableRow
dsAccGwyConfigPortEntry = _DsAccGwyConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 3, 1, 1)
)
dsAccGwyConfigPortEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-POTS-MIB", "dsPortIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigPortEntry.setStatus("current")
_DsPortIndex_Type = Integer32
_DsPortIndex_Object = MibTableColumn
dsPortIndex = _DsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 3, 1, 1, 1),
    _DsPortIndex_Type()
)
dsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsPortIndex.setStatus("current")
_DsPortIvol_Type = Integer32
_DsPortIvol_Object = MibTableColumn
dsPortIvol = _DsPortIvol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 3, 1, 1, 2),
    _DsPortIvol_Type()
)
dsPortIvol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsPortIvol.setStatus("current")
_DsPortOvol_Type = Integer32
_DsPortOvol_Object = MibTableColumn
dsPortOvol = _DsPortOvol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 1, 3, 1, 1, 3),
    _DsPortOvol_Type()
)
dsPortOvol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsPortOvol.setStatus("current")
_DsAccGwyPotsMonitor_ObjectIdentity = ObjectIdentity
dsAccGwyPotsMonitor = _DsAccGwyPotsMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2)
)
_DsAccGwyMonitorPotsSystem_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorPotsSystem = _DsAccGwyMonitorPotsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 1)
)
_DsMonitorAccGwyUpsStatus_Type = DisplayString
_DsMonitorAccGwyUpsStatus_Object = MibScalar
dsMonitorAccGwyUpsStatus = _DsMonitorAccGwyUpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 1, 1),
    _DsMonitorAccGwyUpsStatus_Type()
)
dsMonitorAccGwyUpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMonitorAccGwyUpsStatus.setStatus("current")
_DsAccGwyMonitorPotsSlot_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorPotsSlot = _DsAccGwyMonitorPotsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 2)
)
_DsAccGwyMonitorSlotTable_Object = MibTable
dsAccGwyMonitorSlotTable = _DsAccGwyMonitorSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorSlotTable.setStatus("current")
_DsAccGwyMonitorSlotEntry_Object = MibTableRow
dsAccGwyMonitorSlotEntry = _DsAccGwyMonitorSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 2, 1, 1)
)
dsAccGwyMonitorSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-POTS-MIB", "dsMonitorSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorSlotEntry.setStatus("current")
_DsMonitorSlotIndex_Type = Integer32
_DsMonitorSlotIndex_Object = MibTableColumn
dsMonitorSlotIndex = _DsMonitorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 2, 1, 1, 1),
    _DsMonitorSlotIndex_Type()
)
dsMonitorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMonitorSlotIndex.setStatus("current")


class _DsMonitorSlotInstallStatus_Type(Integer32):
    """Custom type dsMonitorSlotInstallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("removed", 2))
    )


_DsMonitorSlotInstallStatus_Type.__name__ = "Integer32"
_DsMonitorSlotInstallStatus_Object = MibTableColumn
dsMonitorSlotInstallStatus = _DsMonitorSlotInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 2, 1, 1, 2),
    _DsMonitorSlotInstallStatus_Type()
)
dsMonitorSlotInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMonitorSlotInstallStatus.setStatus("current")
_DsAccGwyMonitorPotsPort_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorPotsPort = _DsAccGwyMonitorPotsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 3)
)
_DsAccGwyMonitorPortTable_Object = MibTable
dsAccGwyMonitorPortTable = _DsAccGwyMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorPortTable.setStatus("current")
_DsAccGwyMonitorPortEntry_Object = MibTableRow
dsAccGwyMonitorPortEntry = _DsAccGwyMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 3, 1, 1)
)
dsAccGwyMonitorPortEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-POTS-MIB", "dsMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorPortEntry.setStatus("current")
_DsMonitorPortIndex_Type = Integer32
_DsMonitorPortIndex_Object = MibTableColumn
dsMonitorPortIndex = _DsMonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 3, 1, 1, 1),
    _DsMonitorPortIndex_Type()
)
dsMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMonitorPortIndex.setStatus("current")
_DsMonitorPortStatus_Type = DisplayString
_DsMonitorPortStatus_Object = MibTableColumn
dsMonitorPortStatus = _DsMonitorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 3, 1, 1, 2),
    _DsMonitorPortStatus_Type()
)
dsMonitorPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMonitorPortStatus.setStatus("current")
_DsMonitorPortStatistics_Type = DisplayString
_DsMonitorPortStatistics_Object = MibTableColumn
dsMonitorPortStatistics = _DsMonitorPortStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 2, 3, 1, 1, 3),
    _DsMonitorPortStatistics_Type()
)
dsMonitorPortStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMonitorPortStatistics.setStatus("current")
_DsAccGwyPotsControl_ObjectIdentity = ObjectIdentity
dsAccGwyPotsControl = _DsAccGwyPotsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3)
)
_DsAccGwyControlPotsSlot_ObjectIdentity = ObjectIdentity
dsAccGwyControlPotsSlot = _DsAccGwyControlPotsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 1)
)
_DsAccGwyControlSlotTable_Object = MibTable
dsAccGwyControlSlotTable = _DsAccGwyControlSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyControlSlotTable.setStatus("current")
_DsAccGwyControlSlotEntry_Object = MibTableRow
dsAccGwyControlSlotEntry = _DsAccGwyControlSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 1, 1, 1)
)
dsAccGwyControlSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-POTS-MIB", "dsControlSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyControlSlotEntry.setStatus("current")
_DsControlSlotIndex_Type = Integer32
_DsControlSlotIndex_Object = MibTableColumn
dsControlSlotIndex = _DsControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 1, 1, 1, 1),
    _DsControlSlotIndex_Type()
)
dsControlSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsControlSlotIndex.setStatus("current")


class _DsControlSlotPotsRestart_Type(Integer32):
    """Custom type dsControlSlotPotsRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_DsControlSlotPotsRestart_Type.__name__ = "Integer32"
_DsControlSlotPotsRestart_Object = MibTableColumn
dsControlSlotPotsRestart = _DsControlSlotPotsRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 1, 1, 1, 2),
    _DsControlSlotPotsRestart_Type()
)
dsControlSlotPotsRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlSlotPotsRestart.setStatus("current")


class _DsControlSlotRestart_Type(Integer32):
    """Custom type dsControlSlotRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_DsControlSlotRestart_Type.__name__ = "Integer32"
_DsControlSlotRestart_Object = MibTableColumn
dsControlSlotRestart = _DsControlSlotRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 1, 1, 1, 3),
    _DsControlSlotRestart_Type()
)
dsControlSlotRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlSlotRestart.setStatus("current")
_DsAccGwyControlPotsPort_ObjectIdentity = ObjectIdentity
dsAccGwyControlPotsPort = _DsAccGwyControlPotsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 2)
)
_DsAccGwyControlPortTable_Object = MibTable
dsAccGwyControlPortTable = _DsAccGwyControlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyControlPortTable.setStatus("current")
_DsAccGwyControlPortEntry_Object = MibTableRow
dsAccGwyControlPortEntry = _DsAccGwyControlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 2, 1, 1)
)
dsAccGwyControlPortEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-POTS-MIB", "dsControlPortIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyControlPortEntry.setStatus("current")
_DsControlPortIndex_Type = Integer32
_DsControlPortIndex_Object = MibTableColumn
dsControlPortIndex = _DsControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 2, 1, 1, 1),
    _DsControlPortIndex_Type()
)
dsControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsControlPortIndex.setStatus("current")


class _DsControlPortReset_Type(Integer32):
    """Custom type dsControlPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DsControlPortReset_Type.__name__ = "Integer32"
_DsControlPortReset_Object = MibTableColumn
dsControlPortReset = _DsControlPortReset_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 2, 1, 1, 2),
    _DsControlPortReset_Type()
)
dsControlPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlPortReset.setStatus("current")


class _DsControlPortPortBlock_Type(Integer32):
    """Custom type dsControlPortPortBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unblock", 0),
          ("block", 1))
    )


_DsControlPortPortBlock_Type.__name__ = "Integer32"
_DsControlPortPortBlock_Object = MibTableColumn
dsControlPortPortBlock = _DsControlPortPortBlock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 1, 3, 2, 1, 1, 3),
    _DsControlPortPortBlock_Type()
)
dsControlPortPortBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlPortPortBlock.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-ACCESS-SLOT-POTS-MIB",
    **{"dasanAccessMib": dasanAccessMib,
       "dasanAccGatewayMIBObjects": dasanAccGatewayMIBObjects,
       "dsAccGwyPots": dsAccGwyPots,
       "dsAccGwyPotsConfiguration": dsAccGwyPotsConfiguration,
       "dsAccGwyConfigPotsSystem": dsAccGwyConfigPotsSystem,
       "dsAccGwyConfigGlobalDigitmap": dsAccGwyConfigGlobalDigitmap,
       "dsAccGwyConfigGlobalSwitchDhcp": dsAccGwyConfigGlobalSwitchDhcp,
       "dsAccGwyConfigPotsSlot": dsAccGwyConfigPotsSlot,
       "dsAccGwyConfigSlotTable": dsAccGwyConfigSlotTable,
       "dsAccGwyConfigSlotEntry": dsAccGwyConfigSlotEntry,
       "dsSlotIndex": dsSlotIndex,
       "dsSlotAddAreaCode": dsSlotAddAreaCode,
       "dsSlotAreaCode": dsSlotAreaCode,
       "dsSlotAreaCodeAllows": dsSlotAreaCodeAllows,
       "dsSlotAreaCodeExceptions": dsSlotAreaCodeExceptions,
       "dsSlotCodecType": dsSlotCodecType,
       "dsSlotCodecPacketizationPeriodG711": dsSlotCodecPacketizationPeriodG711,
       "dsSlotCodecPacketizationPeriodG723": dsSlotCodecPacketizationPeriodG723,
       "dsSlotCodecPacketizationPeriodG729": dsSlotCodecPacketizationPeriodG729,
       "dsSlotJitterbuffer": dsSlotJitterbuffer,
       "dsSlotRingonTime": dsSlotRingonTime,
       "dsSlotRingoffTime": dsSlotRingoffTime,
       "dsSlotHookflashMin": dsSlotHookflashMin,
       "dsSlotHookflashMax": dsSlotHookflashMax,
       "dsSlotInterdigitTimeout": dsSlotInterdigitTimeout,
       "dsSlotEce": dsSlotEce,
       "dsSlotFax": dsSlotFax,
       "dsSlotCid": dsSlotCid,
       "dsSlotVad": dsSlotVad,
       "dsSlotCng": dsSlotCng,
       "dsSlotOobdtmf": dsSlotOobdtmf,
       "dsSlotNetworkHostname": dsSlotNetworkHostname,
       "dsSlotNetworkDhcp": dsSlotNetworkDhcp,
       "dsSlotNetworkIpaddress": dsSlotNetworkIpaddress,
       "dsSlotNetworkSubnetmask": dsSlotNetworkSubnetmask,
       "dsSlotNetworkRouter": dsSlotNetworkRouter,
       "dsSlotNetworkNameserver": dsSlotNetworkNameserver,
       "dsSlotVersion": dsSlotVersion,
       "dsAccGwyConfigPotsPort": dsAccGwyConfigPotsPort,
       "dsAccGwyConfigPortTable": dsAccGwyConfigPortTable,
       "dsAccGwyConfigPortEntry": dsAccGwyConfigPortEntry,
       "dsPortIndex": dsPortIndex,
       "dsPortIvol": dsPortIvol,
       "dsPortOvol": dsPortOvol,
       "dsAccGwyPotsMonitor": dsAccGwyPotsMonitor,
       "dsAccGwyMonitorPotsSystem": dsAccGwyMonitorPotsSystem,
       "dsMonitorAccGwyUpsStatus": dsMonitorAccGwyUpsStatus,
       "dsAccGwyMonitorPotsSlot": dsAccGwyMonitorPotsSlot,
       "dsAccGwyMonitorSlotTable": dsAccGwyMonitorSlotTable,
       "dsAccGwyMonitorSlotEntry": dsAccGwyMonitorSlotEntry,
       "dsMonitorSlotIndex": dsMonitorSlotIndex,
       "dsMonitorSlotInstallStatus": dsMonitorSlotInstallStatus,
       "dsAccGwyMonitorPotsPort": dsAccGwyMonitorPotsPort,
       "dsAccGwyMonitorPortTable": dsAccGwyMonitorPortTable,
       "dsAccGwyMonitorPortEntry": dsAccGwyMonitorPortEntry,
       "dsMonitorPortIndex": dsMonitorPortIndex,
       "dsMonitorPortStatus": dsMonitorPortStatus,
       "dsMonitorPortStatistics": dsMonitorPortStatistics,
       "dsAccGwyPotsControl": dsAccGwyPotsControl,
       "dsAccGwyControlPotsSlot": dsAccGwyControlPotsSlot,
       "dsAccGwyControlSlotTable": dsAccGwyControlSlotTable,
       "dsAccGwyControlSlotEntry": dsAccGwyControlSlotEntry,
       "dsControlSlotIndex": dsControlSlotIndex,
       "dsControlSlotPotsRestart": dsControlSlotPotsRestart,
       "dsControlSlotRestart": dsControlSlotRestart,
       "dsAccGwyControlPotsPort": dsAccGwyControlPotsPort,
       "dsAccGwyControlPortTable": dsAccGwyControlPortTable,
       "dsAccGwyControlPortEntry": dsAccGwyControlPortEntry,
       "dsControlPortIndex": dsControlPortIndex,
       "dsControlPortReset": dsControlPortReset,
       "dsControlPortPortBlock": dsControlPortPortBlock}
)
