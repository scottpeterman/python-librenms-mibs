# SNMP MIB module (RUIJIE-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruijie\RUIJIE-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:23 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifAdminStatus,
 ifDescr,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifOperStatus")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10)
)
if mibBuilder.loadTexts:
    ruijieInterfaceMIB.setRevisions(
        ("2010-02-01 00:00",
         "2002-03-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIfConfigMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIfConfigMIBObjects = _RuijieIfConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1)
)
_RuijieIfTable_Object = MibTable
ruijieIfTable = _RuijieIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIfTable.setStatus("current")
_RuijieIfEntry_Object = MibTableRow
ruijieIfEntry = _RuijieIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1)
)
ruijieIfEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfEntry.setStatus("current")
_RuijieIfIndex_Type = IfIndex
_RuijieIfIndex_Object = MibTableColumn
ruijieIfIndex = _RuijieIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 1),
    _RuijieIfIndex_Type()
)
ruijieIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIndex.setStatus("current")


class _RuijieIfPortType_Type(Integer32):
    """Custom type ruijieIfPortType based on Integer32"""
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("port10M100MBASETX", 2),
          ("port100MBASEFXL", 3),
          ("port100MBASEFXS", 4),
          ("port1000MBASESX", 5),
          ("port1000MBASELX", 6),
          ("port1000MBASETX", 7),
          ("portGBIC", 8),
          ("port100MBASEFX", 9),
          ("port1000MBASEFX", 10),
          ("portSFP", 11),
          ("port10GBASESR", 12),
          ("port10GBASELR", 13),
          ("port10GBASEER", 14),
          ("port10GBASELX4", 15),
          ("port10GBASESW", 16),
          ("port10GBASELW", 17),
          ("port10GBASEEW", 18),
          ("port10GBASE", 19),
          ("port40GBASEKR", 20),
          ("port40GBASECR", 21),
          ("port40GBASELR", 22),
          ("port40GBASESR", 23),
          ("port40GBASE", 24),
          ("port100GBASECR", 25),
          ("port100GBASESR", 26),
          ("port100GBASELR", 27),
          ("port100GBASEER", 28),
          ("port100GBASE", 29),
          ("port155MCPOS", 50),
          ("port622MCPOS", 51),
          ("port2G5CPOS", 52),
          ("port10GCPOS", 53),
          ("port155MPOS", 54),
          ("port622MPOS", 55),
          ("port2G5POS", 56),
          ("port10GPOS", 57),
          ("port155MATM", 58),
          ("port622MATM", 59),
          ("port2G5ATM", 60),
          ("port10GATM", 61),
          ("portE1ELC", 62),
          ("port20GBASE", 63),
          ("port25GBASE", 64),
          ("port2500MBASE", 65),
          ("port5000MBASE", 66),
          ("port50GBASE", 67),
          ("port200GBASE", 68),
          ("port400GBASE", 69),
          ("port100MFE", 70),
          ("port1000MSFP", 71),
          ("port2500MMS", 72),
          ("port5GFS", 73),
          ("port10GXS", 74),
          ("port50GFABRIC", 75),
          ("port200GFABRIC", 76),
          ("portXTS", 77))
    )


_RuijieIfPortType_Type.__name__ = "Integer32"
_RuijieIfPortType_Object = MibTableColumn
ruijieIfPortType = _RuijieIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 2),
    _RuijieIfPortType_Type()
)
ruijieIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfPortType.setStatus("current")


class _RuijieIfFlowControlAdminStatus_Type(Integer32):
    """Custom type ruijieIfFlowControlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("autonego", 3),
          ("unknown", 4),
          ("rxon", 5),
          ("txon", 6))
    )


_RuijieIfFlowControlAdminStatus_Type.__name__ = "Integer32"
_RuijieIfFlowControlAdminStatus_Object = MibTableColumn
ruijieIfFlowControlAdminStatus = _RuijieIfFlowControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 3),
    _RuijieIfFlowControlAdminStatus_Type()
)
ruijieIfFlowControlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfFlowControlAdminStatus.setStatus("current")
_RuijieIfFlowControlOperStatus_Type = EnabledStatus
_RuijieIfFlowControlOperStatus_Object = MibTableColumn
ruijieIfFlowControlOperStatus = _RuijieIfFlowControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 4),
    _RuijieIfFlowControlOperStatus_Type()
)
ruijieIfFlowControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFlowControlOperStatus.setStatus("current")


class _RuijieIfAdminSpeed_Type(Integer32):
    """Custom type ruijieIfAdminSpeed based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("speed10Mb", 1),
          ("speed100Mb", 2),
          ("speed1000Mb", 3),
          ("autonego", 4),
          ("speed10Gb", 5),
          ("unknown", 6),
          ("speed40Gb", 7),
          ("speed100Gb", 8),
          ("speed20Gb", 9),
          ("speed25Gb", 10),
          ("speed2500Mb", 11),
          ("speed5000Mb", 12),
          ("speed50Gb", 13),
          ("speed200Gb", 14),
          ("speed400Gb", 15))
    )


_RuijieIfAdminSpeed_Type.__name__ = "Integer32"
_RuijieIfAdminSpeed_Object = MibTableColumn
ruijieIfAdminSpeed = _RuijieIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 5),
    _RuijieIfAdminSpeed_Type()
)
ruijieIfAdminSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfAdminSpeed.setStatus("current")


class _RuijieIfAdminDuplex_Type(Integer32):
    """Custom type ruijieIfAdminDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("autonego", 3),
          ("unknown", 4))
    )


_RuijieIfAdminDuplex_Type.__name__ = "Integer32"
_RuijieIfAdminDuplex_Object = MibTableColumn
ruijieIfAdminDuplex = _RuijieIfAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 6),
    _RuijieIfAdminDuplex_Type()
)
ruijieIfAdminDuplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfAdminDuplex.setStatus("current")


class _RuijieIfOperSpeed_Type(Integer32):
    """Custom type ruijieIfOperSpeed based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("speed10Mb", 1),
          ("speed100Mb", 2),
          ("speed1000Mb", 3),
          ("unknown", 4),
          ("speed10Gb", 5),
          ("speed40Gb", 6),
          ("speed100Gb", 7),
          ("speed20Gb", 8),
          ("speed25Gb", 9),
          ("speed2500Mb", 10),
          ("speed5000Mb", 11),
          ("speed50Gb", 12),
          ("speed200Gb", 13),
          ("speed400Gb", 14))
    )


_RuijieIfOperSpeed_Type.__name__ = "Integer32"
_RuijieIfOperSpeed_Object = MibTableColumn
ruijieIfOperSpeed = _RuijieIfOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 7),
    _RuijieIfOperSpeed_Type()
)
ruijieIfOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOperSpeed.setStatus("current")


class _RuijieIfOperDuplex_Type(Integer32):
    """Custom type ruijieIfOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("unknown", 3))
    )


_RuijieIfOperDuplex_Type.__name__ = "Integer32"
_RuijieIfOperDuplex_Object = MibTableColumn
ruijieIfOperDuplex = _RuijieIfOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 8),
    _RuijieIfOperDuplex_Type()
)
ruijieIfOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOperDuplex.setStatus("current")


class _RuijieIfManageStatus_Type(EnabledStatus):
    """Custom type ruijieIfManageStatus based on EnabledStatus"""
    defaultValue = 1


_RuijieIfManageStatus_Type.__name__ = "EnabledStatus"
_RuijieIfManageStatus_Object = MibTableColumn
ruijieIfManageStatus = _RuijieIfManageStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 9),
    _RuijieIfManageStatus_Type()
)
ruijieIfManageStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfManageStatus.setStatus("current")
_RuijieIfIpBroadcast_Type = IpAddress
_RuijieIfIpBroadcast_Object = MibTableColumn
ruijieIfIpBroadcast = _RuijieIfIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 10),
    _RuijieIfIpBroadcast_Type()
)
ruijieIfIpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfIpBroadcast.setStatus("current")


class _RuijieIfLayer_Type(Integer32):
    """Custom type ruijieIfLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer-2", 1),
          ("layer-3", 2))
    )


_RuijieIfLayer_Type.__name__ = "Integer32"
_RuijieIfLayer_Object = MibTableColumn
ruijieIfLayer = _RuijieIfLayer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 11),
    _RuijieIfLayer_Type()
)
ruijieIfLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfLayer.setStatus("current")


class _RuijieIfMode_Type(Integer32):
    """Custom type ruijieIfMode based on Integer32"""
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
        *(("access", 1),
          ("trunk", 2),
          ("dot1q-tunnel", 3),
          ("hybrid", 4),
          ("other", 5),
          ("uplink", 6),
          ("host", 7),
          ("promiscuous", 8),
          ("ptrunk", 9))
    )


_RuijieIfMode_Type.__name__ = "Integer32"
_RuijieIfMode_Object = MibTableColumn
ruijieIfMode = _RuijieIfMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 12),
    _RuijieIfMode_Type()
)
ruijieIfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfMode.setStatus("current")
_RuijieIfCounterClear_Type = Integer32
_RuijieIfCounterClear_Object = MibTableColumn
ruijieIfCounterClear = _RuijieIfCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 13),
    _RuijieIfCounterClear_Type()
)
ruijieIfCounterClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfCounterClear.setStatus("current")
_RuijieIfEntryStatus_Type = ConfigStatus
_RuijieIfEntryStatus_Object = MibTableColumn
ruijieIfEntryStatus = _RuijieIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 14),
    _RuijieIfEntryStatus_Type()
)
ruijieIfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfEntryStatus.setStatus("current")


class _RuijieIfMediumType_Type(Integer32):
    """Custom type ruijieIfMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("copper", 1),
          ("fiber", 2))
    )


_RuijieIfMediumType_Type.__name__ = "Integer32"
_RuijieIfMediumType_Object = MibTableColumn
ruijieIfMediumType = _RuijieIfMediumType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 15),
    _RuijieIfMediumType_Type()
)
ruijieIfMediumType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfMediumType.setStatus("current")
_RuijieIfDownCounter_Type = Counter32
_RuijieIfDownCounter_Object = MibTableColumn
ruijieIfDownCounter = _RuijieIfDownCounter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 16),
    _RuijieIfDownCounter_Type()
)
ruijieIfDownCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownCounter.setStatus("current")
_RuijieIfInOctets_Type = Counter64
_RuijieIfInOctets_Object = MibTableColumn
ruijieIfInOctets = _RuijieIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 17),
    _RuijieIfInOctets_Type()
)
ruijieIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInOctets.setStatus("current")
_RuijieIfOutOctets_Type = Counter64
_RuijieIfOutOctets_Object = MibTableColumn
ruijieIfOutOctets = _RuijieIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 18),
    _RuijieIfOutOctets_Type()
)
ruijieIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutOctets.setStatus("current")
_RuijieIfBcastInhibit_Type = Integer32
_RuijieIfBcastInhibit_Object = MibTableColumn
ruijieIfBcastInhibit = _RuijieIfBcastInhibit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 19),
    _RuijieIfBcastInhibit_Type()
)
ruijieIfBcastInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfBcastInhibit.setStatus("current")


class _RuijieIfNegotiation_Type(Integer32):
    """Custom type ruijieIfNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieIfNegotiation_Type.__name__ = "Integer32"
_RuijieIfNegotiation_Object = MibTableColumn
ruijieIfNegotiation = _RuijieIfNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 20),
    _RuijieIfNegotiation_Type()
)
ruijieIfNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfNegotiation.setStatus("current")
_RuijieIfPhysAddress_Type = MacAddress
_RuijieIfPhysAddress_Object = MibTableColumn
ruijieIfPhysAddress = _RuijieIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 21),
    _RuijieIfPhysAddress_Type()
)
ruijieIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfPhysAddress.setStatus("current")


class _RuijieIfAdminSpeedRW_Type(Integer32):
    """Custom type ruijieIfAdminSpeedRW based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("speed10Mb", 1),
          ("speed100Mb", 2),
          ("speed1000Mb", 3),
          ("autonego", 4),
          ("speed10Gb", 5),
          ("unknown", 6),
          ("speed40Gb", 7),
          ("speed100Gb", 8),
          ("speed20Gb", 9),
          ("speed25Gb", 10),
          ("speed2500Mb", 11),
          ("speed5000Mb", 12),
          ("speed50Gb", 13),
          ("speed200Gb", 14),
          ("speed400Gb", 15))
    )


_RuijieIfAdminSpeedRW_Type.__name__ = "Integer32"
_RuijieIfAdminSpeedRW_Object = MibTableColumn
ruijieIfAdminSpeedRW = _RuijieIfAdminSpeedRW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 22),
    _RuijieIfAdminSpeedRW_Type()
)
ruijieIfAdminSpeedRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfAdminSpeedRW.setStatus("current")


class _RuijieIfAdminDuplexRW_Type(Integer32):
    """Custom type ruijieIfAdminDuplexRW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("autonego", 3),
          ("unknown", 4))
    )


_RuijieIfAdminDuplexRW_Type.__name__ = "Integer32"
_RuijieIfAdminDuplexRW_Object = MibTableColumn
ruijieIfAdminDuplexRW = _RuijieIfAdminDuplexRW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 23),
    _RuijieIfAdminDuplexRW_Type()
)
ruijieIfAdminDuplexRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfAdminDuplexRW.setStatus("current")


class _RuijieIfModeRW_Type(Integer32):
    """Custom type ruijieIfModeRW based on Integer32"""
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
        *(("access", 1),
          ("trunk", 2),
          ("dot1q-tunnel", 3),
          ("hybrid", 4),
          ("other", 5),
          ("uplink", 6),
          ("host", 7),
          ("promiscuous", 8),
          ("ptrunk", 9))
    )


_RuijieIfModeRW_Type.__name__ = "Integer32"
_RuijieIfModeRW_Object = MibTableColumn
ruijieIfModeRW = _RuijieIfModeRW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 24),
    _RuijieIfModeRW_Type()
)
ruijieIfModeRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfModeRW.setStatus("current")
_RuijieIfSpeed_Type = Gauge32
_RuijieIfSpeed_Object = MibTableColumn
ruijieIfSpeed = _RuijieIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 25),
    _RuijieIfSpeed_Type()
)
ruijieIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfSpeed.setStatus("current")


class _RuijieifAdminStatus_Type(Integer32):
    """Custom type ruijieifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminup", 1),
          ("admindown", 2),
          ("admintest", 3))
    )


_RuijieifAdminStatus_Type.__name__ = "Integer32"
_RuijieifAdminStatus_Object = MibTableColumn
ruijieifAdminStatus = _RuijieifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 26),
    _RuijieifAdminStatus_Type()
)
ruijieifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieifAdminStatus.setStatus("current")


class _RuijieifOperStatus_Type(Integer32):
    """Custom type ruijieifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("test", 3),
          ("unknow", 4),
          ("dormant", 5),
          ("admindown", 8))
    )


_RuijieifOperStatus_Type.__name__ = "Integer32"
_RuijieifOperStatus_Object = MibTableColumn
ruijieifOperStatus = _RuijieifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 27),
    _RuijieifOperStatus_Type()
)
ruijieifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieifOperStatus.setStatus("current")
_RuijieIfInNUcastPkts_Type = Counter64
_RuijieIfInNUcastPkts_Object = MibTableColumn
ruijieIfInNUcastPkts = _RuijieIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 28),
    _RuijieIfInNUcastPkts_Type()
)
ruijieIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInNUcastPkts.setStatus("current")
_RuijieIfOutNUcastPkts_Type = Counter64
_RuijieIfOutNUcastPkts_Object = MibTableColumn
ruijieIfOutNUcastPkts = _RuijieIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 29),
    _RuijieIfOutNUcastPkts_Type()
)
ruijieIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutNUcastPkts.setStatus("current")
_RuijieIfUpDownTimes_Type = Counter32
_RuijieIfUpDownTimes_Object = MibTableColumn
ruijieIfUpDownTimes = _RuijieIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 30),
    _RuijieIfUpDownTimes_Type()
)
ruijieIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUpDownTimes.setStatus("current")


class _RuijieifAdminStatusw_Type(Integer32):
    """Custom type ruijieifAdminStatusw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("admindown", 1))
    )


_RuijieifAdminStatusw_Type.__name__ = "Integer32"
_RuijieifAdminStatusw_Object = MibTableColumn
ruijieifAdminStatusw = _RuijieifAdminStatusw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 31),
    _RuijieifAdminStatusw_Type()
)
ruijieifAdminStatusw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieifAdminStatusw.setStatus("current")


class _RuijieifOperStatusw_Type(Integer32):
    """Custom type ruijieifOperStatusw based on Integer32"""
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
          ("admindown", 2))
    )


_RuijieifOperStatusw_Type.__name__ = "Integer32"
_RuijieifOperStatusw_Object = MibTableColumn
ruijieifOperStatusw = _RuijieifOperStatusw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 32),
    _RuijieifOperStatusw_Type()
)
ruijieifOperStatusw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieifOperStatusw.setStatus("current")
_RuijieifSpeedw_Type = Integer32
_RuijieifSpeedw_Object = MibTableColumn
ruijieifSpeedw = _RuijieifSpeedw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 33),
    _RuijieifSpeedw_Type()
)
ruijieifSpeedw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieifSpeedw.setStatus("current")
_RuijieifMacAddress_Type = MacAddress
_RuijieifMacAddress_Object = MibTableColumn
ruijieifMacAddress = _RuijieifMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 34),
    _RuijieifMacAddress_Type()
)
ruijieifMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieifMacAddress.setStatus("current")
_RuijieifLastChange_Type = TimeTicks
_RuijieifLastChange_Object = MibTableColumn
ruijieifLastChange = _RuijieifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 35),
    _RuijieifLastChange_Type()
)
ruijieifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieifLastChange.setStatus("current")
_RuijieIfInPkts_Type = Counter64
_RuijieIfInPkts_Object = MibTableColumn
ruijieIfInPkts = _RuijieIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 36),
    _RuijieIfInPkts_Type()
)
ruijieIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInPkts.setStatus("current")
_RuijieIfDiscard_Type = Counter64
_RuijieIfDiscard_Object = MibTableColumn
ruijieIfDiscard = _RuijieIfDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 37),
    _RuijieIfDiscard_Type()
)
ruijieIfDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDiscard.setStatus("current")
_RuijieIfBandwidthUsage_Type = DisplayString
_RuijieIfBandwidthUsage_Object = MibTableColumn
ruijieIfBandwidthUsage = _RuijieIfBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 38),
    _RuijieIfBandwidthUsage_Type()
)
ruijieIfBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfBandwidthUsage.setStatus("current")
_RuijieIfInBitsRate_Type = Counter64
_RuijieIfInBitsRate_Object = MibTableColumn
ruijieIfInBitsRate = _RuijieIfInBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 39),
    _RuijieIfInBitsRate_Type()
)
ruijieIfInBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInBitsRate.setStatus("current")
_RuijieIfInPktRate_Type = Counter64
_RuijieIfInPktRate_Object = MibTableColumn
ruijieIfInPktRate = _RuijieIfInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 40),
    _RuijieIfInPktRate_Type()
)
ruijieIfInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInPktRate.setStatus("current")
_RuijieIfOutBitsRate_Type = Counter64
_RuijieIfOutBitsRate_Object = MibTableColumn
ruijieIfOutBitsRate = _RuijieIfOutBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 41),
    _RuijieIfOutBitsRate_Type()
)
ruijieIfOutBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutBitsRate.setStatus("current")
_RuijieIfOutPktRate_Type = Counter64
_RuijieIfOutPktRate_Object = MibTableColumn
ruijieIfOutPktRate = _RuijieIfOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 42),
    _RuijieIfOutPktRate_Type()
)
ruijieIfOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutPktRate.setStatus("current")
_RuijieIfInBandwidthUsage_Type = DisplayString
_RuijieIfInBandwidthUsage_Object = MibTableColumn
ruijieIfInBandwidthUsage = _RuijieIfInBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 43),
    _RuijieIfInBandwidthUsage_Type()
)
ruijieIfInBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInBandwidthUsage.setStatus("current")
_RuijieIfOutBandwidthUsage_Type = DisplayString
_RuijieIfOutBandwidthUsage_Object = MibTableColumn
ruijieIfOutBandwidthUsage = _RuijieIfOutBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 44),
    _RuijieIfOutBandwidthUsage_Type()
)
ruijieIfOutBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutBandwidthUsage.setStatus("current")
_RuijieIfInErrorPktsRate_Type = DisplayString
_RuijieIfInErrorPktsRate_Object = MibTableColumn
ruijieIfInErrorPktsRate = _RuijieIfInErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 45),
    _RuijieIfInErrorPktsRate_Type()
)
ruijieIfInErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInErrorPktsRate.setStatus("current")
_RuijieIfOutErrorPktsRate_Type = DisplayString
_RuijieIfOutErrorPktsRate_Object = MibTableColumn
ruijieIfOutErrorPktsRate = _RuijieIfOutErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 46),
    _RuijieIfOutErrorPktsRate_Type()
)
ruijieIfOutErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutErrorPktsRate.setStatus("current")
_RuijieIfInDropPktsRate_Type = DisplayString
_RuijieIfInDropPktsRate_Object = MibTableColumn
ruijieIfInDropPktsRate = _RuijieIfInDropPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 47),
    _RuijieIfInDropPktsRate_Type()
)
ruijieIfInDropPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInDropPktsRate.setStatus("current")
_RuijieIfOutDropPktsRate_Type = DisplayString
_RuijieIfOutDropPktsRate_Object = MibTableColumn
ruijieIfOutDropPktsRate = _RuijieIfOutDropPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 48),
    _RuijieIfOutDropPktsRate_Type()
)
ruijieIfOutDropPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutDropPktsRate.setStatus("current")
_RuijieIfOutNoBuffer_Type = Counter64
_RuijieIfOutNoBuffer_Object = MibTableColumn
ruijieIfOutNoBuffer = _RuijieIfOutNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 49),
    _RuijieIfOutNoBuffer_Type()
)
ruijieIfOutNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutNoBuffer.setStatus("current")
_RuijieIfOutPkts_Type = Counter64
_RuijieIfOutPkts_Object = MibTableColumn
ruijieIfOutPkts = _RuijieIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 50),
    _RuijieIfOutPkts_Type()
)
ruijieIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutPkts.setStatus("current")
_RuijieIfNeighborIP_Type = IpAddress
_RuijieIfNeighborIP_Object = MibTableColumn
ruijieIfNeighborIP = _RuijieIfNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 51),
    _RuijieIfNeighborIP_Type()
)
ruijieIfNeighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfNeighborIP.setStatus("current")
_RuijieIfNeighborIPv6_Type = DisplayString
_RuijieIfNeighborIPv6_Object = MibTableColumn
ruijieIfNeighborIPv6 = _RuijieIfNeighborIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 52),
    _RuijieIfNeighborIPv6_Type()
)
ruijieIfNeighborIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfNeighborIPv6.setStatus("current")


class _RuijieIfIsSubPort_Type(Unsigned32):
    """Custom type ruijieIfIsSubPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieIfIsSubPort_Type.__name__ = "Unsigned32"
_RuijieIfIsSubPort_Object = MibTableColumn
ruijieIfIsSubPort = _RuijieIfIsSubPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 53),
    _RuijieIfIsSubPort_Type()
)
ruijieIfIsSubPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIsSubPort.setStatus("current")
_RuijieIfDemux_Type = DisplayString
_RuijieIfDemux_Object = MibTableColumn
ruijieIfDemux = _RuijieIfDemux_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 54),
    _RuijieIfDemux_Type()
)
ruijieIfDemux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDemux.setStatus("current")
_RuijieIfDemuxChannelId_Type = Integer32
_RuijieIfDemuxChannelId_Object = MibTableColumn
ruijieIfDemuxChannelId = _RuijieIfDemuxChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 55),
    _RuijieIfDemuxChannelId_Type()
)
ruijieIfDemuxChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDemuxChannelId.setStatus("current")
_RuijieIfInFecCorrect_Type = Counter64
_RuijieIfInFecCorrect_Object = MibTableColumn
ruijieIfInFecCorrect = _RuijieIfInFecCorrect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 56),
    _RuijieIfInFecCorrect_Type()
)
ruijieIfInFecCorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInFecCorrect.setStatus("current")
_RuijieIfInFecUnCorrect_Type = Counter64
_RuijieIfInFecUnCorrect_Object = MibTableColumn
ruijieIfInFecUnCorrect = _RuijieIfInFecUnCorrect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 57),
    _RuijieIfInFecUnCorrect_Type()
)
ruijieIfInFecUnCorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInFecUnCorrect.setStatus("current")


class _RuijieIfLinkDownReason_Type(Integer32):
    """Custom type ruijieIfLinkDownReason based on Integer32"""
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
        *(("unknown", 1),
          ("admin-down", 2),
          ("err-disabled", 3),
          ("apm-standby", 4),
          ("apr", 5),
          ("UPC-fault", 6),
          ("peer-off", 7),
          ("BF-failure", 8),
          ("TF-failure", 9))
    )


_RuijieIfLinkDownReason_Type.__name__ = "Integer32"
_RuijieIfLinkDownReason_Object = MibTableColumn
ruijieIfLinkDownReason = _RuijieIfLinkDownReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 1, 1, 58),
    _RuijieIfLinkDownReason_Type()
)
ruijieIfLinkDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkDownReason.setStatus("current")
_RuijieIfIpTable_Object = MibTable
ruijieIfIpTable = _RuijieIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieIfIpTable.setStatus("current")
_RuijieIfIpEntry_Object = MibTableRow
ruijieIfIpEntry = _RuijieIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 2, 1)
)
ruijieIfIpEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfIpIfIndex"),
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfIpId"),
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfIp"),
)
if mibBuilder.loadTexts:
    ruijieIfIpEntry.setStatus("current")
_RuijieIfIpIfIndex_Type = IfIndex
_RuijieIfIpIfIndex_Object = MibTableColumn
ruijieIfIpIfIndex = _RuijieIfIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 2, 1, 1),
    _RuijieIfIpIfIndex_Type()
)
ruijieIfIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpIfIndex.setStatus("current")


class _RuijieIfIpId_Type(Integer32):
    """Custom type ruijieIfIpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_RuijieIfIpId_Type.__name__ = "Integer32"
_RuijieIfIpId_Object = MibTableColumn
ruijieIfIpId = _RuijieIfIpId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 2, 1, 2),
    _RuijieIfIpId_Type()
)
ruijieIfIpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpId.setStatus("current")
_RuijieIfIp_Type = IpAddress
_RuijieIfIp_Object = MibTableColumn
ruijieIfIp = _RuijieIfIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 2, 1, 3),
    _RuijieIfIp_Type()
)
ruijieIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIp.setStatus("current")
_RuijieIfIpMask_Type = IpAddress
_RuijieIfIpMask_Object = MibTableColumn
ruijieIfIpMask = _RuijieIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 2, 1, 4),
    _RuijieIfIpMask_Type()
)
ruijieIfIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfIpMask.setStatus("current")
_RuijieIfIpEntryStatus_Type = RowStatus
_RuijieIfIpEntryStatus_Object = MibTableColumn
ruijieIfIpEntryStatus = _RuijieIfIpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 2, 1, 5),
    _RuijieIfIpEntryStatus_Type()
)
ruijieIfIpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIfIpEntryStatus.setStatus("current")
_RuijieIfStatusTable_Object = MibTable
ruijieIfStatusTable = _RuijieIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieIfStatusTable.setStatus("current")
_RuijieIfStatusEntry_Object = MibTableRow
ruijieIfStatusEntry = _RuijieIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 3, 1)
)
ruijieIfStatusEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfStatusIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfStatusEntry.setStatus("current")
_RuijieIfStatusIndex_Type = IfIndex
_RuijieIfStatusIndex_Object = MibTableColumn
ruijieIfStatusIndex = _RuijieIfStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 3, 1, 1),
    _RuijieIfStatusIndex_Type()
)
ruijieIfStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfStatusIndex.setStatus("current")
_RuijieIfStatusLoopBackExamine_Type = Integer32
_RuijieIfStatusLoopBackExamine_Object = MibTableColumn
ruijieIfStatusLoopBackExamine = _RuijieIfStatusLoopBackExamine_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 3, 1, 2),
    _RuijieIfStatusLoopBackExamine_Type()
)
ruijieIfStatusLoopBackExamine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfStatusLoopBackExamine.setStatus("current")


class _RuijieIfErrorStatus_Type(Integer32):
    """Custom type ruijieIfErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 1),
          ("err-disable-bpduguard", 2),
          ("err-disable-ptsecurity", 3))
    )


_RuijieIfErrorStatus_Type.__name__ = "Integer32"
_RuijieIfErrorStatus_Object = MibTableColumn
ruijieIfErrorStatus = _RuijieIfErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 3, 1, 3),
    _RuijieIfErrorStatus_Type()
)
ruijieIfErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfErrorStatus.setStatus("current")
_RuijieIfLineDetect_Type = Integer32
_RuijieIfLineDetect_Object = MibTableColumn
ruijieIfLineDetect = _RuijieIfLineDetect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 3, 1, 4),
    _RuijieIfLineDetect_Type()
)
ruijieIfLineDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLineDetect.setStatus("current")
_RuijieGlobalIfDisableRecovery_Type = Integer32
_RuijieGlobalIfDisableRecovery_Object = MibScalar
ruijieGlobalIfDisableRecovery = _RuijieGlobalIfDisableRecovery_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 4),
    _RuijieGlobalIfDisableRecovery_Type()
)
ruijieGlobalIfDisableRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalIfDisableRecovery.setStatus("current")
_RuijiePortTypeChooseTable_Object = MibTable
ruijiePortTypeChooseTable = _RuijiePortTypeChooseTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 5)
)
if mibBuilder.loadTexts:
    ruijiePortTypeChooseTable.setStatus("current")
_RuijiePortTypeChooseEntry_Object = MibTableRow
ruijiePortTypeChooseEntry = _RuijiePortTypeChooseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 5, 1)
)
ruijiePortTypeChooseEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijiePortTypeChooseIndex"),
)
if mibBuilder.loadTexts:
    ruijiePortTypeChooseEntry.setStatus("current")
_RuijiePortTypeChooseIndex_Type = IfIndex
_RuijiePortTypeChooseIndex_Object = MibTableColumn
ruijiePortTypeChooseIndex = _RuijiePortTypeChooseIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 5, 1, 1),
    _RuijiePortTypeChooseIndex_Type()
)
ruijiePortTypeChooseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePortTypeChooseIndex.setStatus("current")


class _RuijiePortTypeChooseType_Type(Integer32):
    """Custom type ruijiePortTypeChooseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("copper", 2))
    )


_RuijiePortTypeChooseType_Type.__name__ = "Integer32"
_RuijiePortTypeChooseType_Object = MibTableColumn
ruijiePortTypeChooseType = _RuijiePortTypeChooseType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 5, 1, 2),
    _RuijiePortTypeChooseType_Type()
)
ruijiePortTypeChooseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePortTypeChooseType.setStatus("current")
_RuijieIfMTUTable_Object = MibTable
ruijieIfMTUTable = _RuijieIfMTUTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieIfMTUTable.setStatus("current")
_RuijieIfMTUEntry_Object = MibTableRow
ruijieIfMTUEntry = _RuijieIfMTUEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 6, 1)
)
ruijieIfMTUEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfMTUIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfMTUEntry.setStatus("current")
_RuijieIfMTUIndex_Type = IfIndex
_RuijieIfMTUIndex_Object = MibTableColumn
ruijieIfMTUIndex = _RuijieIfMTUIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 6, 1, 1),
    _RuijieIfMTUIndex_Type()
)
ruijieIfMTUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfMTUIndex.setStatus("current")
_RuijieIfMTU_Type = Integer32
_RuijieIfMTU_Object = MibTableColumn
ruijieIfMTU = _RuijieIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 6, 1, 2),
    _RuijieIfMTU_Type()
)
ruijieIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfMTU.setStatus("current")
_RuijieIfAvailableBWTable_Object = MibTable
ruijieIfAvailableBWTable = _RuijieIfAvailableBWTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieIfAvailableBWTable.setStatus("current")
_RuijieIfAvailableBWEntry_Object = MibTableRow
ruijieIfAvailableBWEntry = _RuijieIfAvailableBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 7, 1)
)
ruijieIfAvailableBWEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfAvailableBWIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfAvailableBWEntry.setStatus("current")
_RuijieIfAvailableBWIfIndex_Type = IfIndex
_RuijieIfAvailableBWIfIndex_Object = MibTableColumn
ruijieIfAvailableBWIfIndex = _RuijieIfAvailableBWIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 7, 1, 1),
    _RuijieIfAvailableBWIfIndex_Type()
)
ruijieIfAvailableBWIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfAvailableBWIfIndex.setStatus("current")
_RuijieIfAvailableBWIfBW_Type = Gauge32
_RuijieIfAvailableBWIfBW_Object = MibTableColumn
ruijieIfAvailableBWIfBW = _RuijieIfAvailableBWIfBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 7, 1, 2),
    _RuijieIfAvailableBWIfBW_Type()
)
ruijieIfAvailableBWIfBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfAvailableBWIfBW.setStatus("current")
_RuijieIfSVICreatTable_Object = MibTable
ruijieIfSVICreatTable = _RuijieIfSVICreatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieIfSVICreatTable.setStatus("current")
_RuijieIfSVICreatEntry_Object = MibTableRow
ruijieIfSVICreatEntry = _RuijieIfSVICreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 8, 1)
)
ruijieIfSVICreatEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfSVICreatVlanNum"),
)
if mibBuilder.loadTexts:
    ruijieIfSVICreatEntry.setStatus("current")


class _RuijieIfSVICreatVlanNum_Type(Integer32):
    """Custom type ruijieIfSVICreatVlanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieIfSVICreatVlanNum_Type.__name__ = "Integer32"
_RuijieIfSVICreatVlanNum_Object = MibTableColumn
ruijieIfSVICreatVlanNum = _RuijieIfSVICreatVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 8, 1, 1),
    _RuijieIfSVICreatVlanNum_Type()
)
ruijieIfSVICreatVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfSVICreatVlanNum.setStatus("current")


class _RuijieIfHandleSVI_Type(Integer32):
    """Custom type ruijieIfHandleSVI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("create", 0),
          ("delete", 1))
    )


_RuijieIfHandleSVI_Type.__name__ = "Integer32"
_RuijieIfHandleSVI_Object = MibTableColumn
ruijieIfHandleSVI = _RuijieIfHandleSVI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 8, 1, 2),
    _RuijieIfHandleSVI_Type()
)
ruijieIfHandleSVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfHandleSVI.setStatus("current")
_RuijieIfPhyIntNum_Type = Integer32
_RuijieIfPhyIntNum_Object = MibScalar
ruijieIfPhyIntNum = _RuijieIfPhyIntNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 9),
    _RuijieIfPhyIntNum_Type()
)
ruijieIfPhyIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfPhyIntNum.setStatus("current")
_RuijieIfLinkUPTimesTable_Object = MibTable
ruijieIfLinkUPTimesTable = _RuijieIfLinkUPTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieIfLinkUPTimesTable.setStatus("current")
_RuijieIfLinkUPTimesEntry_Object = MibTableRow
ruijieIfLinkUPTimesEntry = _RuijieIfLinkUPTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 10, 1)
)
ruijieIfLinkUPTimesEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfLinkUPTimesEntry.setStatus("current")


class _RuijieInterfaceIndex_Type(Integer32):
    """Custom type ruijieInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieInterfaceIndex_Type.__name__ = "Integer32"
_RuijieInterfaceIndex_Object = MibTableColumn
ruijieInterfaceIndex = _RuijieInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 10, 1, 1),
    _RuijieInterfaceIndex_Type()
)
ruijieInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInterfaceIndex.setStatus("current")
_RuijieIfLinkUPTimes_Type = Integer32
_RuijieIfLinkUPTimes_Object = MibTableColumn
ruijieIfLinkUPTimes = _RuijieIfLinkUPTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 10, 1, 2),
    _RuijieIfLinkUPTimes_Type()
)
ruijieIfLinkUPTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkUPTimes.setStatus("current")
_RuijieIfEncapsulationTable_Object = MibTable
ruijieIfEncapsulationTable = _RuijieIfEncapsulationTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieIfEncapsulationTable.setStatus("current")
_RuijieIfEncapsulationEntry_Object = MibTableRow
ruijieIfEncapsulationEntry = _RuijieIfEncapsulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 11, 1)
)
ruijieIfEncapsulationEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfEncapsulationIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfEncapsulationEntry.setStatus("current")
_RuijieIfEncapsulationIndex_Type = IfIndex
_RuijieIfEncapsulationIndex_Object = MibTableColumn
ruijieIfEncapsulationIndex = _RuijieIfEncapsulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 11, 1, 1),
    _RuijieIfEncapsulationIndex_Type()
)
ruijieIfEncapsulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfEncapsulationIndex.setStatus("current")
_RuijieIfEncapsulationVlan_Type = VlanId
_RuijieIfEncapsulationVlan_Object = MibTableColumn
ruijieIfEncapsulationVlan = _RuijieIfEncapsulationVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 11, 1, 2),
    _RuijieIfEncapsulationVlan_Type()
)
ruijieIfEncapsulationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfEncapsulationVlan.setStatus("current")
_RuijieApIfNumberTable_Object = MibTable
ruijieApIfNumberTable = _RuijieApIfNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 12)
)
if mibBuilder.loadTexts:
    ruijieApIfNumberTable.setStatus("current")
_RuijieApIfNumberEntry_Object = MibTableRow
ruijieApIfNumberEntry = _RuijieApIfNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 12, 1)
)
ruijieApIfNumberEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieApPhyAddress"),
)
if mibBuilder.loadTexts:
    ruijieApIfNumberEntry.setStatus("current")


class _RuijieApPhyAddress_Type(PhysAddress):
    """Custom type ruijieApPhyAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RuijieApPhyAddress_Type.__name__ = "PhysAddress"
_RuijieApPhyAddress_Object = MibTableColumn
ruijieApPhyAddress = _RuijieApPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 12, 1, 1),
    _RuijieApPhyAddress_Type()
)
ruijieApPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApPhyAddress.setStatus("current")
_RuijieApIfNumber_Type = Integer32
_RuijieApIfNumber_Object = MibTableColumn
ruijieApIfNumber = _RuijieApIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 12, 1, 2),
    _RuijieApIfNumber_Type()
)
ruijieApIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfNumber.setStatus("current")
_RuijieApIfPhyIntNum_Type = Integer32
_RuijieApIfPhyIntNum_Object = MibTableColumn
ruijieApIfPhyIntNum = _RuijieApIfPhyIntNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 12, 1, 3),
    _RuijieApIfPhyIntNum_Type()
)
ruijieApIfPhyIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfPhyIntNum.setStatus("current")
_RuijieApIfTable_Object = MibTable
ruijieApIfTable = _RuijieApIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieApIfTable.setStatus("current")
_RuijieApIfEntry_Object = MibTableRow
ruijieApIfEntry = _RuijieApIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1)
)
ruijieApIfEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieApPhysAddress"),
    (0, "RUIJIE-INTERFACE-MIB", "ruijieApIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieApIfEntry.setStatus("current")


class _RuijieApPhysAddress_Type(PhysAddress):
    """Custom type ruijieApPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RuijieApPhysAddress_Type.__name__ = "PhysAddress"
_RuijieApPhysAddress_Object = MibTableColumn
ruijieApPhysAddress = _RuijieApPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 1),
    _RuijieApPhysAddress_Type()
)
ruijieApPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApPhysAddress.setStatus("current")
_RuijieApIfIndex_Type = IfIndex
_RuijieApIfIndex_Object = MibTableColumn
ruijieApIfIndex = _RuijieApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 2),
    _RuijieApIfIndex_Type()
)
ruijieApIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfIndex.setStatus("current")


class _RuijieApIfDescr_Type(DisplayString):
    """Custom type ruijieApIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieApIfDescr_Type.__name__ = "DisplayString"
_RuijieApIfDescr_Object = MibTableColumn
ruijieApIfDescr = _RuijieApIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 3),
    _RuijieApIfDescr_Type()
)
ruijieApIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfDescr.setStatus("current")
_RuijieApIfType_Type = IANAifType
_RuijieApIfType_Object = MibTableColumn
ruijieApIfType = _RuijieApIfType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 4),
    _RuijieApIfType_Type()
)
ruijieApIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfType.setStatus("current")
_RuijieApIfMtu_Type = Integer32
_RuijieApIfMtu_Object = MibTableColumn
ruijieApIfMtu = _RuijieApIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 5),
    _RuijieApIfMtu_Type()
)
ruijieApIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfMtu.setStatus("current")
_RuijieApIfSpeed_Type = Gauge32
_RuijieApIfSpeed_Object = MibTableColumn
ruijieApIfSpeed = _RuijieApIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 6),
    _RuijieApIfSpeed_Type()
)
ruijieApIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfSpeed.setStatus("current")


class _RuijieApIfPhysAddress_Type(PhysAddress):
    """Custom type ruijieApIfPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RuijieApIfPhysAddress_Type.__name__ = "PhysAddress"
_RuijieApIfPhysAddress_Object = MibTableColumn
ruijieApIfPhysAddress = _RuijieApIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 7),
    _RuijieApIfPhysAddress_Type()
)
ruijieApIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfPhysAddress.setStatus("current")


class _RuijieApIfAdminStatus_Type(Integer32):
    """Custom type ruijieApIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("admindown", 2),
          ("testing", 3))
    )


_RuijieApIfAdminStatus_Type.__name__ = "Integer32"
_RuijieApIfAdminStatus_Object = MibTableColumn
ruijieApIfAdminStatus = _RuijieApIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 8),
    _RuijieApIfAdminStatus_Type()
)
ruijieApIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApIfAdminStatus.setStatus("current")


class _RuijieApIfOperStatus_Type(Integer32):
    """Custom type ruijieApIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("admindown", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_RuijieApIfOperStatus_Type.__name__ = "Integer32"
_RuijieApIfOperStatus_Object = MibTableColumn
ruijieApIfOperStatus = _RuijieApIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 9),
    _RuijieApIfOperStatus_Type()
)
ruijieApIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOperStatus.setStatus("current")
_RuijieApIfLastChange_Type = TimeTicks
_RuijieApIfLastChange_Object = MibTableColumn
ruijieApIfLastChange = _RuijieApIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 10),
    _RuijieApIfLastChange_Type()
)
ruijieApIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfLastChange.setStatus("current")
_RuijieApIfInOctets_Type = Counter64
_RuijieApIfInOctets_Object = MibTableColumn
ruijieApIfInOctets = _RuijieApIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 11),
    _RuijieApIfInOctets_Type()
)
ruijieApIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInOctets.setStatus("current")
_RuijieApIfInUcastPkts_Type = Counter64
_RuijieApIfInUcastPkts_Object = MibTableColumn
ruijieApIfInUcastPkts = _RuijieApIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 12),
    _RuijieApIfInUcastPkts_Type()
)
ruijieApIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInUcastPkts.setStatus("current")
_RuijieApIfInNUcastPkts_Type = Counter64
_RuijieApIfInNUcastPkts_Object = MibTableColumn
ruijieApIfInNUcastPkts = _RuijieApIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 13),
    _RuijieApIfInNUcastPkts_Type()
)
ruijieApIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInNUcastPkts.setStatus("deprecated")
_RuijieApIfInDiscards_Type = Counter32
_RuijieApIfInDiscards_Object = MibTableColumn
ruijieApIfInDiscards = _RuijieApIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 14),
    _RuijieApIfInDiscards_Type()
)
ruijieApIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInDiscards.setStatus("current")
_RuijieApIfInErrors_Type = Counter32
_RuijieApIfInErrors_Object = MibTableColumn
ruijieApIfInErrors = _RuijieApIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 15),
    _RuijieApIfInErrors_Type()
)
ruijieApIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInErrors.setStatus("current")
_RuijieApIfInUnknownProtos_Type = Counter32
_RuijieApIfInUnknownProtos_Object = MibTableColumn
ruijieApIfInUnknownProtos = _RuijieApIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 16),
    _RuijieApIfInUnknownProtos_Type()
)
ruijieApIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInUnknownProtos.setStatus("current")
_RuijieApIfOutOctets_Type = Counter64
_RuijieApIfOutOctets_Object = MibTableColumn
ruijieApIfOutOctets = _RuijieApIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 17),
    _RuijieApIfOutOctets_Type()
)
ruijieApIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutOctets.setStatus("current")
_RuijieApIfOutUcastPkts_Type = Counter64
_RuijieApIfOutUcastPkts_Object = MibTableColumn
ruijieApIfOutUcastPkts = _RuijieApIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 18),
    _RuijieApIfOutUcastPkts_Type()
)
ruijieApIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutUcastPkts.setStatus("current")
_RuijieApIfOutNUcastPkts_Type = Counter64
_RuijieApIfOutNUcastPkts_Object = MibTableColumn
ruijieApIfOutNUcastPkts = _RuijieApIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 19),
    _RuijieApIfOutNUcastPkts_Type()
)
ruijieApIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutNUcastPkts.setStatus("deprecated")
_RuijieApIfOutDiscards_Type = Counter32
_RuijieApIfOutDiscards_Object = MibTableColumn
ruijieApIfOutDiscards = _RuijieApIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 20),
    _RuijieApIfOutDiscards_Type()
)
ruijieApIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutDiscards.setStatus("current")
_RuijieApIfOutErrors_Type = Counter32
_RuijieApIfOutErrors_Object = MibTableColumn
ruijieApIfOutErrors = _RuijieApIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 21),
    _RuijieApIfOutErrors_Type()
)
ruijieApIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutErrors.setStatus("current")
_RuijieApIfOutQLen_Type = Gauge32
_RuijieApIfOutQLen_Object = MibTableColumn
ruijieApIfOutQLen = _RuijieApIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 22),
    _RuijieApIfOutQLen_Type()
)
ruijieApIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutQLen.setStatus("deprecated")
_RuijieApIfLinkUPTimes_Type = Integer32
_RuijieApIfLinkUPTimes_Object = MibTableColumn
ruijieApIfLinkUPTimes = _RuijieApIfLinkUPTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 23),
    _RuijieApIfLinkUPTimes_Type()
)
ruijieApIfLinkUPTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfLinkUPTimes.setStatus("current")
_RuijieApIfInDataOctets_Type = Counter64
_RuijieApIfInDataOctets_Object = MibTableColumn
ruijieApIfInDataOctets = _RuijieApIfInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 24),
    _RuijieApIfInDataOctets_Type()
)
ruijieApIfInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInDataOctets.setStatus("current")
_RuijieApIfOutDataOctets_Type = Counter64
_RuijieApIfOutDataOctets_Object = MibTableColumn
ruijieApIfOutDataOctets = _RuijieApIfOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 25),
    _RuijieApIfOutDataOctets_Type()
)
ruijieApIfOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutDataOctets.setStatus("current")
_RuijieApIfMgmtUploadOctets_Type = Counter32
_RuijieApIfMgmtUploadOctets_Object = MibTableColumn
ruijieApIfMgmtUploadOctets = _RuijieApIfMgmtUploadOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 26),
    _RuijieApIfMgmtUploadOctets_Type()
)
ruijieApIfMgmtUploadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfMgmtUploadOctets.setStatus("current")
_RuijieApIfMgmtDownloadOctets_Type = Counter32
_RuijieApIfMgmtDownloadOctets_Object = MibTableColumn
ruijieApIfMgmtDownloadOctets = _RuijieApIfMgmtDownloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 27),
    _RuijieApIfMgmtDownloadOctets_Type()
)
ruijieApIfMgmtDownloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfMgmtDownloadOctets.setStatus("current")
_RuijieApIfSpeedw_Type = Integer32
_RuijieApIfSpeedw_Object = MibTableColumn
ruijieApIfSpeedw = _RuijieApIfSpeedw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 28),
    _RuijieApIfSpeedw_Type()
)
ruijieApIfSpeedw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfSpeedw.setStatus("current")
_RuijieApIfMtuw_Type = Integer32
_RuijieApIfMtuw_Object = MibTableColumn
ruijieApIfMtuw = _RuijieApIfMtuw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 29),
    _RuijieApIfMtuw_Type()
)
ruijieApIfMtuw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfMtuw.setStatus("current")
_RuijieApIfPhysAddressw_Type = MacAddress
_RuijieApIfPhysAddressw_Object = MibTableColumn
ruijieApIfPhysAddressw = _RuijieApIfPhysAddressw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 30),
    _RuijieApIfPhysAddressw_Type()
)
ruijieApIfPhysAddressw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfPhysAddressw.setStatus("current")
_RuijieApIfInUcastPktsw_Type = Counter32
_RuijieApIfInUcastPktsw_Object = MibTableColumn
ruijieApIfInUcastPktsw = _RuijieApIfInUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 31),
    _RuijieApIfInUcastPktsw_Type()
)
ruijieApIfInUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInUcastPktsw.setStatus("current")
_RuijieApIfInNUcastPktsw_Type = Counter32
_RuijieApIfInNUcastPktsw_Object = MibTableColumn
ruijieApIfInNUcastPktsw = _RuijieApIfInNUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 32),
    _RuijieApIfInNUcastPktsw_Type()
)
ruijieApIfInNUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInNUcastPktsw.setStatus("deprecated")
_RuijieApIfOutUcastPktsw_Type = Counter32
_RuijieApIfOutUcastPktsw_Object = MibTableColumn
ruijieApIfOutUcastPktsw = _RuijieApIfOutUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 33),
    _RuijieApIfOutUcastPktsw_Type()
)
ruijieApIfOutUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutUcastPktsw.setStatus("current")
_RuijieApIfOutNUcastPktsw_Type = Counter32
_RuijieApIfOutNUcastPktsw_Object = MibTableColumn
ruijieApIfOutNUcastPktsw = _RuijieApIfOutNUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 34),
    _RuijieApIfOutNUcastPktsw_Type()
)
ruijieApIfOutNUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutNUcastPktsw.setStatus("deprecated")
_RuijieApIfLinkUPTimesw_Type = Counter32
_RuijieApIfLinkUPTimesw_Object = MibTableColumn
ruijieApIfLinkUPTimesw = _RuijieApIfLinkUPTimesw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 35),
    _RuijieApIfLinkUPTimesw_Type()
)
ruijieApIfLinkUPTimesw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfLinkUPTimesw.setStatus("current")
_RuijieApIfInPkts_Type = Counter64
_RuijieApIfInPkts_Object = MibTableColumn
ruijieApIfInPkts = _RuijieApIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 36),
    _RuijieApIfInPkts_Type()
)
ruijieApIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInPkts.setStatus("current")
_RuijieApIfInFlow_Type = Counter32
_RuijieApIfInFlow_Object = MibTableColumn
ruijieApIfInFlow = _RuijieApIfInFlow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 37),
    _RuijieApIfInFlow_Type()
)
ruijieApIfInFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInFlow.setStatus("current")
_RuijieApIfOutFlow_Type = Counter32
_RuijieApIfOutFlow_Object = MibTableColumn
ruijieApIfOutFlow = _RuijieApIfOutFlow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 38),
    _RuijieApIfOutFlow_Type()
)
ruijieApIfOutFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutFlow.setStatus("current")
_RuijieApIfInBrdcastPkts_Type = Counter64
_RuijieApIfInBrdcastPkts_Object = MibTableColumn
ruijieApIfInBrdcastPkts = _RuijieApIfInBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 39),
    _RuijieApIfInBrdcastPkts_Type()
)
ruijieApIfInBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInBrdcastPkts.setStatus("current")
_RuijieApIfOutBrdcastPkts_Type = Counter64
_RuijieApIfOutBrdcastPkts_Object = MibTableColumn
ruijieApIfOutBrdcastPkts = _RuijieApIfOutBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 40),
    _RuijieApIfOutBrdcastPkts_Type()
)
ruijieApIfOutBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutBrdcastPkts.setStatus("current")
_RuijieApIfInMulcastPkts_Type = Counter64
_RuijieApIfInMulcastPkts_Object = MibTableColumn
ruijieApIfInMulcastPkts = _RuijieApIfInMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 41),
    _RuijieApIfInMulcastPkts_Type()
)
ruijieApIfInMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInMulcastPkts.setStatus("current")
_RuijieApIfOutMulcastPkts_Type = Counter64
_RuijieApIfOutMulcastPkts_Object = MibTableColumn
ruijieApIfOutMulcastPkts = _RuijieApIfOutMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 42),
    _RuijieApIfOutMulcastPkts_Type()
)
ruijieApIfOutMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutMulcastPkts.setStatus("current")
_RuijieApIfInPayloadOctets_Type = Counter64
_RuijieApIfInPayloadOctets_Object = MibTableColumn
ruijieApIfInPayloadOctets = _RuijieApIfInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 43),
    _RuijieApIfInPayloadOctets_Type()
)
ruijieApIfInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInPayloadOctets.setStatus("current")
_RuijieApIfOutPayloadOctets_Type = Counter64
_RuijieApIfOutPayloadOctets_Object = MibTableColumn
ruijieApIfOutPayloadOctets = _RuijieApIfOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 44),
    _RuijieApIfOutPayloadOctets_Type()
)
ruijieApIfOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutPayloadOctets.setStatus("current")


class _RuijieApIfAlias_Type(DisplayString):
    """Custom type ruijieApIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieApIfAlias_Type.__name__ = "DisplayString"
_RuijieApIfAlias_Object = MibTableColumn
ruijieApIfAlias = _RuijieApIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 45),
    _RuijieApIfAlias_Type()
)
ruijieApIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfAlias.setStatus("current")
_RuijieApIfInDateRate_Type = Counter64
_RuijieApIfInDateRate_Object = MibTableColumn
ruijieApIfInDateRate = _RuijieApIfInDateRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 46),
    _RuijieApIfInDateRate_Type()
)
ruijieApIfInDateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfInDateRate.setStatus("current")
_RuijieApIfOutDateRate_Type = Counter64
_RuijieApIfOutDateRate_Object = MibTableColumn
ruijieApIfOutDateRate = _RuijieApIfOutDateRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 47),
    _RuijieApIfOutDateRate_Type()
)
ruijieApIfOutDateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutDateRate.setStatus("current")
_RuijieApifInNormalPkts_Type = Counter64
_RuijieApifInNormalPkts_Object = MibTableColumn
ruijieApifInNormalPkts = _RuijieApifInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 48),
    _RuijieApifInNormalPkts_Type()
)
ruijieApifInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApifInNormalPkts.setStatus("current")
_RuijieApIfOutPkts_Type = Counter64
_RuijieApIfOutPkts_Object = MibTableColumn
ruijieApIfOutPkts = _RuijieApIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 13, 1, 49),
    _RuijieApIfOutPkts_Type()
)
ruijieApIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIfOutPkts.setStatus("current")
_RuijieIfLinkTable_Object = MibTable
ruijieIfLinkTable = _RuijieIfLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14)
)
if mibBuilder.loadTexts:
    ruijieIfLinkTable.setStatus("current")
_RuijieIfLinkEntry_Object = MibTableRow
ruijieIfLinkEntry = _RuijieIfLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1)
)
ruijieIfLinkEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfLinkIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfLinkEntry.setStatus("current")
_RuijieIfLinkIndex_Type = IfIndex
_RuijieIfLinkIndex_Object = MibTableColumn
ruijieIfLinkIndex = _RuijieIfLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 1),
    _RuijieIfLinkIndex_Type()
)
ruijieIfLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkIndex.setStatus("current")
_RuijieIfUplinkInOctets_Type = Counter32
_RuijieIfUplinkInOctets_Object = MibTableColumn
ruijieIfUplinkInOctets = _RuijieIfUplinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 2),
    _RuijieIfUplinkInOctets_Type()
)
ruijieIfUplinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkInOctets.setStatus("current")
_RuijieIfUplinkInUcastPkts_Type = Counter32
_RuijieIfUplinkInUcastPkts_Object = MibTableColumn
ruijieIfUplinkInUcastPkts = _RuijieIfUplinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 3),
    _RuijieIfUplinkInUcastPkts_Type()
)
ruijieIfUplinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkInUcastPkts.setStatus("current")
_RuijieIfUplinkInNUcastPkts_Type = Counter32
_RuijieIfUplinkInNUcastPkts_Object = MibTableColumn
ruijieIfUplinkInNUcastPkts = _RuijieIfUplinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 4),
    _RuijieIfUplinkInNUcastPkts_Type()
)
ruijieIfUplinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkInNUcastPkts.setStatus("deprecated")
_RuijieIfUplinkInDiscards_Type = Counter32
_RuijieIfUplinkInDiscards_Object = MibTableColumn
ruijieIfUplinkInDiscards = _RuijieIfUplinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 5),
    _RuijieIfUplinkInDiscards_Type()
)
ruijieIfUplinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkInDiscards.setStatus("current")
_RuijieIfUplinkInErrors_Type = Counter32
_RuijieIfUplinkInErrors_Object = MibTableColumn
ruijieIfUplinkInErrors = _RuijieIfUplinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 6),
    _RuijieIfUplinkInErrors_Type()
)
ruijieIfUplinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkInErrors.setStatus("current")
_RuijieIfUplinkOutOctets_Type = Counter32
_RuijieIfUplinkOutOctets_Object = MibTableColumn
ruijieIfUplinkOutOctets = _RuijieIfUplinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 7),
    _RuijieIfUplinkOutOctets_Type()
)
ruijieIfUplinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkOutOctets.setStatus("current")
_RuijieIfUplinkOutUcastPkts_Type = Counter32
_RuijieIfUplinkOutUcastPkts_Object = MibTableColumn
ruijieIfUplinkOutUcastPkts = _RuijieIfUplinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 8),
    _RuijieIfUplinkOutUcastPkts_Type()
)
ruijieIfUplinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkOutUcastPkts.setStatus("current")
_RuijieIfUplinkOutNUcastPkts_Type = Counter32
_RuijieIfUplinkOutNUcastPkts_Object = MibTableColumn
ruijieIfUplinkOutNUcastPkts = _RuijieIfUplinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 9),
    _RuijieIfUplinkOutNUcastPkts_Type()
)
ruijieIfUplinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkOutNUcastPkts.setStatus("deprecated")
_RuijieIfUplinkOutDiscards_Type = Counter32
_RuijieIfUplinkOutDiscards_Object = MibTableColumn
ruijieIfUplinkOutDiscards = _RuijieIfUplinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 10),
    _RuijieIfUplinkOutDiscards_Type()
)
ruijieIfUplinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkOutDiscards.setStatus("current")
_RuijieIfUplinkOutErrors_Type = Counter32
_RuijieIfUplinkOutErrors_Object = MibTableColumn
ruijieIfUplinkOutErrors = _RuijieIfUplinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 11),
    _RuijieIfUplinkOutErrors_Type()
)
ruijieIfUplinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkOutErrors.setStatus("current")
_RuijieIfDownlinkInOctets_Type = Counter32
_RuijieIfDownlinkInOctets_Object = MibTableColumn
ruijieIfDownlinkInOctets = _RuijieIfDownlinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 12),
    _RuijieIfDownlinkInOctets_Type()
)
ruijieIfDownlinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkInOctets.setStatus("current")
_RuijieIfDownlinkInUcastPkts_Type = Counter32
_RuijieIfDownlinkInUcastPkts_Object = MibTableColumn
ruijieIfDownlinkInUcastPkts = _RuijieIfDownlinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 13),
    _RuijieIfDownlinkInUcastPkts_Type()
)
ruijieIfDownlinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkInUcastPkts.setStatus("current")
_RuijieIfDownlinkInNUcastPkts_Type = Counter32
_RuijieIfDownlinkInNUcastPkts_Object = MibTableColumn
ruijieIfDownlinkInNUcastPkts = _RuijieIfDownlinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 14),
    _RuijieIfDownlinkInNUcastPkts_Type()
)
ruijieIfDownlinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkInNUcastPkts.setStatus("deprecated")
_RuijieIfDownlinkInDiscards_Type = Counter32
_RuijieIfDownlinkInDiscards_Object = MibTableColumn
ruijieIfDownlinkInDiscards = _RuijieIfDownlinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 15),
    _RuijieIfDownlinkInDiscards_Type()
)
ruijieIfDownlinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkInDiscards.setStatus("current")
_RuijieIfDownlinkInErrors_Type = Counter32
_RuijieIfDownlinkInErrors_Object = MibTableColumn
ruijieIfDownlinkInErrors = _RuijieIfDownlinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 16),
    _RuijieIfDownlinkInErrors_Type()
)
ruijieIfDownlinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkInErrors.setStatus("current")
_RuijieIfDownlinkOutOctets_Type = Counter32
_RuijieIfDownlinkOutOctets_Object = MibTableColumn
ruijieIfDownlinkOutOctets = _RuijieIfDownlinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 17),
    _RuijieIfDownlinkOutOctets_Type()
)
ruijieIfDownlinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkOutOctets.setStatus("current")
_RuijieIfDownlinkOutUcastPkts_Type = Counter32
_RuijieIfDownlinkOutUcastPkts_Object = MibTableColumn
ruijieIfDownlinkOutUcastPkts = _RuijieIfDownlinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 18),
    _RuijieIfDownlinkOutUcastPkts_Type()
)
ruijieIfDownlinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkOutUcastPkts.setStatus("current")
_RuijieIfDownlinkOutNUcastPkts_Type = Counter32
_RuijieIfDownlinkOutNUcastPkts_Object = MibTableColumn
ruijieIfDownlinkOutNUcastPkts = _RuijieIfDownlinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 19),
    _RuijieIfDownlinkOutNUcastPkts_Type()
)
ruijieIfDownlinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkOutNUcastPkts.setStatus("deprecated")
_RuijieIfDownlinkOutDiscards_Type = Counter32
_RuijieIfDownlinkOutDiscards_Object = MibTableColumn
ruijieIfDownlinkOutDiscards = _RuijieIfDownlinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 20),
    _RuijieIfDownlinkOutDiscards_Type()
)
ruijieIfDownlinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkOutDiscards.setStatus("current")
_RuijieIfDownlinkOutErrors_Type = Counter32
_RuijieIfDownlinkOutErrors_Object = MibTableColumn
ruijieIfDownlinkOutErrors = _RuijieIfDownlinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 21),
    _RuijieIfDownlinkOutErrors_Type()
)
ruijieIfDownlinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkOutErrors.setStatus("current")
_RuijieIfUplinkInBcastPkts_Type = Counter64
_RuijieIfUplinkInBcastPkts_Object = MibTableColumn
ruijieIfUplinkInBcastPkts = _RuijieIfUplinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 22),
    _RuijieIfUplinkInBcastPkts_Type()
)
ruijieIfUplinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkInBcastPkts.setStatus("current")
_RuijieIfUplinkOutBcastPkts_Type = Counter64
_RuijieIfUplinkOutBcastPkts_Object = MibTableColumn
ruijieIfUplinkOutBcastPkts = _RuijieIfUplinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 23),
    _RuijieIfUplinkOutBcastPkts_Type()
)
ruijieIfUplinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUplinkOutBcastPkts.setStatus("current")
_RuijieIfDownlinkInBcastPkts_Type = Counter64
_RuijieIfDownlinkInBcastPkts_Object = MibTableColumn
ruijieIfDownlinkInBcastPkts = _RuijieIfDownlinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 24),
    _RuijieIfDownlinkInBcastPkts_Type()
)
ruijieIfDownlinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkInBcastPkts.setStatus("current")
_RuijieIfDownlinkOutBcastPkts_Type = Counter64
_RuijieIfDownlinkOutBcastPkts_Object = MibTableColumn
ruijieIfDownlinkOutBcastPkts = _RuijieIfDownlinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 14, 1, 25),
    _RuijieIfDownlinkOutBcastPkts_Type()
)
ruijieIfDownlinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDownlinkOutBcastPkts.setStatus("current")
_RuijieIfTrafficStatisticsObjects_ObjectIdentity = ObjectIdentity
ruijieIfTrafficStatisticsObjects = _RuijieIfTrafficStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15)
)
_RuijieIfLinkTrafficStatistics_ObjectIdentity = ObjectIdentity
ruijieIfLinkTrafficStatistics = _RuijieIfLinkTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1)
)
_RuijieIfLinkTrafficTable_Object = MibTable
ruijieIfLinkTrafficTable = _RuijieIfLinkTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIfLinkTrafficTable.setStatus("current")
_RuijieIfLinkTrafficEntry_Object = MibTableRow
ruijieIfLinkTrafficEntry = _RuijieIfLinkTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1)
)
ruijieIfLinkTrafficEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfLinkTrafficIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfLinkTrafficEntry.setStatus("current")
_RuijieIfLinkTrafficIndex_Type = Unsigned32
_RuijieIfLinkTrafficIndex_Object = MibTableColumn
ruijieIfLinkTrafficIndex = _RuijieIfLinkTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 1),
    _RuijieIfLinkTrafficIndex_Type()
)
ruijieIfLinkTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkTrafficIndex.setStatus("current")


class _RuijieIfLinkAvgRate_Type(Counter32):
    """Custom type ruijieIfLinkAvgRate based on Counter32"""
    defaultValue = 0


_RuijieIfLinkAvgRate_Type.__name__ = "Counter32"
_RuijieIfLinkAvgRate_Object = MibTableColumn
ruijieIfLinkAvgRate = _RuijieIfLinkAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 2),
    _RuijieIfLinkAvgRate_Type()
)
ruijieIfLinkAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkAvgRate.setStatus("current")


class _RuijieIfLinkPeakRate_Type(Counter32):
    """Custom type ruijieIfLinkPeakRate based on Counter32"""
    defaultValue = 0


_RuijieIfLinkPeakRate_Type.__name__ = "Counter32"
_RuijieIfLinkPeakRate_Object = MibTableColumn
ruijieIfLinkPeakRate = _RuijieIfLinkPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 3),
    _RuijieIfLinkPeakRate_Type()
)
ruijieIfLinkPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkPeakRate.setStatus("current")


class _RuijieIfLinkAvgBWUtilization_Type(Integer32):
    """Custom type ruijieIfLinkAvgBWUtilization based on Integer32"""
    defaultValue = 0


_RuijieIfLinkAvgBWUtilization_Type.__name__ = "Integer32"
_RuijieIfLinkAvgBWUtilization_Object = MibTableColumn
ruijieIfLinkAvgBWUtilization = _RuijieIfLinkAvgBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 4),
    _RuijieIfLinkAvgBWUtilization_Type()
)
ruijieIfLinkAvgBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkAvgBWUtilization.setStatus("current")


class _RuijieIfLinkPeakBWUtilization_Type(Integer32):
    """Custom type ruijieIfLinkPeakBWUtilization based on Integer32"""
    defaultValue = 0


_RuijieIfLinkPeakBWUtilization_Type.__name__ = "Integer32"
_RuijieIfLinkPeakBWUtilization_Object = MibTableColumn
ruijieIfLinkPeakBWUtilization = _RuijieIfLinkPeakBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 5),
    _RuijieIfLinkPeakBWUtilization_Type()
)
ruijieIfLinkPeakBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfLinkPeakBWUtilization.setStatus("current")
_RuijieIfLinkQosStatistics_ObjectIdentity = ObjectIdentity
ruijieIfLinkQosStatistics = _RuijieIfLinkQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2)
)
_RuijieLinkQosCtlTable_Object = MibTable
ruijieLinkQosCtlTable = _RuijieLinkQosCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieLinkQosCtlTable.setStatus("current")
_RuijieLinkQosCtlEntry_Object = MibTableRow
ruijieLinkQosCtlEntry = _RuijieLinkQosCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1)
)
ruijieLinkQosCtlEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieLinkQosCtlOwnerIndex"),
    (0, "RUIJIE-INTERFACE-MIB", "ruijieLinkQosCtlTestName"),
)
if mibBuilder.loadTexts:
    ruijieLinkQosCtlEntry.setStatus("current")


class _RuijieLinkQosCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type ruijieLinkQosCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieLinkQosCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_RuijieLinkQosCtlOwnerIndex_Object = MibTableColumn
ruijieLinkQosCtlOwnerIndex = _RuijieLinkQosCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 1),
    _RuijieLinkQosCtlOwnerIndex_Type()
)
ruijieLinkQosCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieLinkQosCtlOwnerIndex.setStatus("current")


class _RuijieLinkQosCtlTestName_Type(SnmpAdminString):
    """Custom type ruijieLinkQosCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieLinkQosCtlTestName_Type.__name__ = "SnmpAdminString"
_RuijieLinkQosCtlTestName_Object = MibTableColumn
ruijieLinkQosCtlTestName = _RuijieLinkQosCtlTestName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 2),
    _RuijieLinkQosCtlTestName_Type()
)
ruijieLinkQosCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieLinkQosCtlTestName.setStatus("current")


class _RuijieLinkQosCtlTargetAddressType_Type(InetAddressType):
    """Custom type ruijieLinkQosCtlTargetAddressType based on InetAddressType"""
    defaultValue = 0


_RuijieLinkQosCtlTargetAddressType_Type.__name__ = "InetAddressType"
_RuijieLinkQosCtlTargetAddressType_Object = MibTableColumn
ruijieLinkQosCtlTargetAddressType = _RuijieLinkQosCtlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 3),
    _RuijieLinkQosCtlTargetAddressType_Type()
)
ruijieLinkQosCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieLinkQosCtlTargetAddressType.setStatus("current")


class _RuijieLinkQosCtlTargetAddress_Type(InetAddress):
    """Custom type ruijieLinkQosCtlTargetAddress based on InetAddress"""
    defaultHexValue = ""


_RuijieLinkQosCtlTargetAddress_Type.__name__ = "InetAddress"
_RuijieLinkQosCtlTargetAddress_Object = MibTableColumn
ruijieLinkQosCtlTargetAddress = _RuijieLinkQosCtlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 4),
    _RuijieLinkQosCtlTargetAddress_Type()
)
ruijieLinkQosCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieLinkQosCtlTargetAddress.setStatus("current")


class _RuijieLinkQosCtlAdminStatus_Type(Integer32):
    """Custom type ruijieLinkQosCtlAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RuijieLinkQosCtlAdminStatus_Type.__name__ = "Integer32"
_RuijieLinkQosCtlAdminStatus_Object = MibTableColumn
ruijieLinkQosCtlAdminStatus = _RuijieLinkQosCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 5),
    _RuijieLinkQosCtlAdminStatus_Type()
)
ruijieLinkQosCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieLinkQosCtlAdminStatus.setStatus("current")
_RuijieLinkQosCtlRowStatus_Type = RowStatus
_RuijieLinkQosCtlRowStatus_Object = MibTableColumn
ruijieLinkQosCtlRowStatus = _RuijieLinkQosCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 6),
    _RuijieLinkQosCtlRowStatus_Type()
)
ruijieLinkQosCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieLinkQosCtlRowStatus.setStatus("current")
_RuijieLinkQosResultsTable_Object = MibTable
ruijieLinkQosResultsTable = _RuijieLinkQosResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieLinkQosResultsTable.setStatus("current")
_RuijieLinkQosResultsEntry_Object = MibTableRow
ruijieLinkQosResultsEntry = _RuijieLinkQosResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1)
)
ruijieLinkQosResultsEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieLinkQosCtlOwnerIndex"),
    (0, "RUIJIE-INTERFACE-MIB", "ruijieLinkQosCtlTestName"),
)
if mibBuilder.loadTexts:
    ruijieLinkQosResultsEntry.setStatus("current")


class _RuijieLinkQosResultsOperStatus_Type(Integer32):
    """Custom type ruijieLinkQosResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("completed", 3))
    )


_RuijieLinkQosResultsOperStatus_Type.__name__ = "Integer32"
_RuijieLinkQosResultsOperStatus_Object = MibTableColumn
ruijieLinkQosResultsOperStatus = _RuijieLinkQosResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 1),
    _RuijieLinkQosResultsOperStatus_Type()
)
ruijieLinkQosResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsOperStatus.setStatus("current")


class _RuijieLinkQosResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type ruijieLinkQosResultsIpTargetAddressType based on InetAddressType"""
    defaultValue = 0


_RuijieLinkQosResultsIpTargetAddressType_Type.__name__ = "InetAddressType"
_RuijieLinkQosResultsIpTargetAddressType_Object = MibTableColumn
ruijieLinkQosResultsIpTargetAddressType = _RuijieLinkQosResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 2),
    _RuijieLinkQosResultsIpTargetAddressType_Type()
)
ruijieLinkQosResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsIpTargetAddressType.setStatus("current")


class _RuijieLinkQosResultsIpTargetAddress_Type(InetAddress):
    """Custom type ruijieLinkQosResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_RuijieLinkQosResultsIpTargetAddress_Type.__name__ = "InetAddress"
_RuijieLinkQosResultsIpTargetAddress_Object = MibTableColumn
ruijieLinkQosResultsIpTargetAddress = _RuijieLinkQosResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 3),
    _RuijieLinkQosResultsIpTargetAddress_Type()
)
ruijieLinkQosResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsIpTargetAddress.setStatus("current")
_RuijieLinkQosResultsMaxRtt_Type = Unsigned32
_RuijieLinkQosResultsMaxRtt_Object = MibTableColumn
ruijieLinkQosResultsMaxRtt = _RuijieLinkQosResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 4),
    _RuijieLinkQosResultsMaxRtt_Type()
)
ruijieLinkQosResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsMaxRtt.setUnits("milliseconds")
_RuijieLinkQosResultsMinRtt_Type = Unsigned32
_RuijieLinkQosResultsMinRtt_Object = MibTableColumn
ruijieLinkQosResultsMinRtt = _RuijieLinkQosResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 5),
    _RuijieLinkQosResultsMinRtt_Type()
)
ruijieLinkQosResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsMinRtt.setUnits("milliseconds")
_RuijieLinkQosResultsAverageRtt_Type = Unsigned32
_RuijieLinkQosResultsAverageRtt_Object = MibTableColumn
ruijieLinkQosResultsAverageRtt = _RuijieLinkQosResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 6),
    _RuijieLinkQosResultsAverageRtt_Type()
)
ruijieLinkQosResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsAverageRtt.setUnits("milliseconds")
_RuijieLinkQosResultsDelayJitter_Type = Unsigned32
_RuijieLinkQosResultsDelayJitter_Object = MibTableColumn
ruijieLinkQosResultsDelayJitter = _RuijieLinkQosResultsDelayJitter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 7),
    _RuijieLinkQosResultsDelayJitter_Type()
)
ruijieLinkQosResultsDelayJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsDelayJitter.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsDelayJitter.setUnits("milliseconds")
_RuijieLinkQosResultsPktsLossRate_Type = Unsigned32
_RuijieLinkQosResultsPktsLossRate_Object = MibTableColumn
ruijieLinkQosResultsPktsLossRate = _RuijieLinkQosResultsPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 8),
    _RuijieLinkQosResultsPktsLossRate_Type()
)
ruijieLinkQosResultsPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsPktsLossRate.setStatus("current")
_RuijieLinkQosResultsNetworkAF_Type = Unsigned32
_RuijieLinkQosResultsNetworkAF_Object = MibTableColumn
ruijieLinkQosResultsNetworkAF = _RuijieLinkQosResultsNetworkAF_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 9),
    _RuijieLinkQosResultsNetworkAF_Type()
)
ruijieLinkQosResultsNetworkAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkQosResultsNetworkAF.setStatus("current")
_RuijieIfDeviceTrafficStatistics_ObjectIdentity = ObjectIdentity
ruijieIfDeviceTrafficStatistics = _RuijieIfDeviceTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3)
)
_RuijieIfDeviceTrafficTable_Object = MibTable
ruijieIfDeviceTrafficTable = _RuijieIfDeviceTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieIfDeviceTrafficTable.setStatus("current")
_RuijieIfDeviceTrafficEntry_Object = MibTableRow
ruijieIfDeviceTrafficEntry = _RuijieIfDeviceTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1)
)
ruijieIfDeviceTrafficEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfDeviceTrafficIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfDeviceTrafficEntry.setStatus("current")
_RuijieIfDeviceTrafficIndex_Type = Unsigned32
_RuijieIfDeviceTrafficIndex_Object = MibTableColumn
ruijieIfDeviceTrafficIndex = _RuijieIfDeviceTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 1),
    _RuijieIfDeviceTrafficIndex_Type()
)
ruijieIfDeviceTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDeviceTrafficIndex.setStatus("current")
_RuijieIfFC_Type = Integer32
_RuijieIfFC_Object = MibTableColumn
ruijieIfFC = _RuijieIfFC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 2),
    _RuijieIfFC_Type()
)
ruijieIfFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFC.setStatus("current")
_RuijieIfFCTransRate_Type = Counter32
_RuijieIfFCTransRate_Object = MibTableColumn
ruijieIfFCTransRate = _RuijieIfFCTransRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 3),
    _RuijieIfFCTransRate_Type()
)
ruijieIfFCTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFCTransRate.setStatus("current")
_RuijieIfFCTransPktsNum_Type = Counter64
_RuijieIfFCTransPktsNum_Object = MibTableColumn
ruijieIfFCTransPktsNum = _RuijieIfFCTransPktsNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 4),
    _RuijieIfFCTransPktsNum_Type()
)
ruijieIfFCTransPktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFCTransPktsNum.setStatus("current")
_RuijieIfFCDiscardRate_Type = Counter32
_RuijieIfFCDiscardRate_Object = MibTableColumn
ruijieIfFCDiscardRate = _RuijieIfFCDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 5),
    _RuijieIfFCDiscardRate_Type()
)
ruijieIfFCDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFCDiscardRate.setStatus("current")
_RuijieIfFCDiscardPktsNum_Type = Counter64
_RuijieIfFCDiscardPktsNum_Object = MibTableColumn
ruijieIfFCDiscardPktsNum = _RuijieIfFCDiscardPktsNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 6),
    _RuijieIfFCDiscardPktsNum_Type()
)
ruijieIfFCDiscardPktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFCDiscardPktsNum.setStatus("current")
_RuijieIfFCPktsLossRate_Type = Integer32
_RuijieIfFCPktsLossRate_Object = MibTableColumn
ruijieIfFCPktsLossRate = _RuijieIfFCPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 7),
    _RuijieIfFCPktsLossRate_Type()
)
ruijieIfFCPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFCPktsLossRate.setStatus("current")
_RuijieIfFCBandwidthRate_Type = Counter32
_RuijieIfFCBandwidthRate_Object = MibTableColumn
ruijieIfFCBandwidthRate = _RuijieIfFCBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 8),
    _RuijieIfFCBandwidthRate_Type()
)
ruijieIfFCBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFCBandwidthRate.setStatus("current")
_RuijieIfFCBandwidthPercentage_Type = Integer32
_RuijieIfFCBandwidthPercentage_Object = MibTableColumn
ruijieIfFCBandwidthPercentage = _RuijieIfFCBandwidthPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 9),
    _RuijieIfFCBandwidthPercentage_Type()
)
ruijieIfFCBandwidthPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFCBandwidthPercentage.setStatus("current")
_RuijieIfDeviceFCGathers_Type = Integer32
_RuijieIfDeviceFCGathers_Object = MibTableColumn
ruijieIfDeviceFCGathers = _RuijieIfDeviceFCGathers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 10),
    _RuijieIfDeviceFCGathers_Type()
)
ruijieIfDeviceFCGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDeviceFCGathers.setStatus("current")
_RuijieIfFullMeshFCGathers_Type = Integer32
_RuijieIfFullMeshFCGathers_Object = MibTableColumn
ruijieIfFullMeshFCGathers = _RuijieIfFullMeshFCGathers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 11),
    _RuijieIfFullMeshFCGathers_Type()
)
ruijieIfFullMeshFCGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFullMeshFCGathers.setStatus("current")
_RuijieIfClassBasedGathers_Type = Integer32
_RuijieIfClassBasedGathers_Object = MibTableColumn
ruijieIfClassBasedGathers = _RuijieIfClassBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 12),
    _RuijieIfClassBasedGathers_Type()
)
ruijieIfClassBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfClassBasedGathers.setStatus("current")
_RuijieIfNodeBasedGathers_Type = Integer32
_RuijieIfNodeBasedGathers_Object = MibTableColumn
ruijieIfNodeBasedGathers = _RuijieIfNodeBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 13),
    _RuijieIfNodeBasedGathers_Type()
)
ruijieIfNodeBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfNodeBasedGathers.setStatus("current")
_RuijieIfNodeClassBasedGathers_Type = Integer32
_RuijieIfNodeClassBasedGathers_Object = MibTableColumn
ruijieIfNodeClassBasedGathers = _RuijieIfNodeClassBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 14),
    _RuijieIfNodeClassBasedGathers_Type()
)
ruijieIfNodeClassBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfNodeClassBasedGathers.setStatus("current")
_RuijieIfNodeFCBasedGathers_Type = Integer32
_RuijieIfNodeFCBasedGathers_Object = MibTableColumn
ruijieIfNodeFCBasedGathers = _RuijieIfNodeFCBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 15),
    _RuijieIfNodeFCBasedGathers_Type()
)
ruijieIfNodeFCBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfNodeFCBasedGathers.setStatus("current")
_RuijieIfNodeDeviceFCBasedGathers_Type = Integer32
_RuijieIfNodeDeviceFCBasedGathers_Object = MibTableColumn
ruijieIfNodeDeviceFCBasedGathers = _RuijieIfNodeDeviceFCBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 16),
    _RuijieIfNodeDeviceFCBasedGathers_Type()
)
ruijieIfNodeDeviceFCBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfNodeDeviceFCBasedGathers.setStatus("current")
_RuijieIfPhyTable_Object = MibTable
ruijieIfPhyTable = _RuijieIfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 16)
)
if mibBuilder.loadTexts:
    ruijieIfPhyTable.setStatus("current")
_RuijieIfPhyEntry_Object = MibTableRow
ruijieIfPhyEntry = _RuijieIfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 16, 1)
)
ruijieIfPhyEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfPhyIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfPhyEntry.setStatus("current")
_RuijieIfPhyIndex_Type = IfIndex
_RuijieIfPhyIndex_Object = MibTableColumn
ruijieIfPhyIndex = _RuijieIfPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 16, 1, 1),
    _RuijieIfPhyIndex_Type()
)
ruijieIfPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfPhyIndex.setStatus("current")


class _RuijieifPhyOperStatus_Type(Integer32):
    """Custom type ruijieifPhyOperStatus based on Integer32"""
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
          ("admindown", 2))
    )


_RuijieifPhyOperStatus_Type.__name__ = "Integer32"
_RuijieifPhyOperStatus_Object = MibTableColumn
ruijieifPhyOperStatus = _RuijieifPhyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 16, 1, 2),
    _RuijieifPhyOperStatus_Type()
)
ruijieifPhyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieifPhyOperStatus.setStatus("current")
_RuijieIfPeakRateTable_Object = MibTable
ruijieIfPeakRateTable = _RuijieIfPeakRateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 17)
)
if mibBuilder.loadTexts:
    ruijieIfPeakRateTable.setStatus("current")
_RuijieIfPeakRateEntry_Object = MibTableRow
ruijieIfPeakRateEntry = _RuijieIfPeakRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 17, 1)
)
ruijieIfPeakRateEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfPeakRateIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfPeakRateEntry.setStatus("current")
_RuijieIfPeakRateIndex_Type = IfIndex
_RuijieIfPeakRateIndex_Object = MibTableColumn
ruijieIfPeakRateIndex = _RuijieIfPeakRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 17, 1, 1),
    _RuijieIfPeakRateIndex_Type()
)
ruijieIfPeakRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfPeakRateIndex.setStatus("current")
_RuijieIfRxPeakRate_Type = Counter64
_RuijieIfRxPeakRate_Object = MibTableColumn
ruijieIfRxPeakRate = _RuijieIfRxPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 17, 1, 2),
    _RuijieIfRxPeakRate_Type()
)
ruijieIfRxPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfRxPeakRate.setStatus("current")
_RuijieIfRxPeakRateTime_Type = DisplayString
_RuijieIfRxPeakRateTime_Object = MibTableColumn
ruijieIfRxPeakRateTime = _RuijieIfRxPeakRateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 17, 1, 3),
    _RuijieIfRxPeakRateTime_Type()
)
ruijieIfRxPeakRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfRxPeakRateTime.setStatus("current")
_RuijieIfTxPeakRate_Type = Counter64
_RuijieIfTxPeakRate_Object = MibTableColumn
ruijieIfTxPeakRate = _RuijieIfTxPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 17, 1, 4),
    _RuijieIfTxPeakRate_Type()
)
ruijieIfTxPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfTxPeakRate.setStatus("current")
_RuijieIfTxPeakRateTime_Type = DisplayString
_RuijieIfTxPeakRateTime_Object = MibTableColumn
ruijieIfTxPeakRateTime = _RuijieIfTxPeakRateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 17, 1, 5),
    _RuijieIfTxPeakRateTime_Type()
)
ruijieIfTxPeakRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfTxPeakRateTime.setStatus("current")
_RuijieApInfoTable_Object = MibTable
ruijieApInfoTable = _RuijieApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 18)
)
if mibBuilder.loadTexts:
    ruijieApInfoTable.setStatus("current")
_RuijieApInfoEntry_Object = MibTableRow
ruijieApInfoEntry = _RuijieApInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 18, 1)
)
ruijieApInfoEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieApInfoAddress"),
)
if mibBuilder.loadTexts:
    ruijieApInfoEntry.setStatus("current")


class _RuijieApInfoAddress_Type(PhysAddress):
    """Custom type ruijieApInfoAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RuijieApInfoAddress_Type.__name__ = "PhysAddress"
_RuijieApInfoAddress_Object = MibTableColumn
ruijieApInfoAddress = _RuijieApInfoAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 18, 1, 1),
    _RuijieApInfoAddress_Type()
)
ruijieApInfoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApInfoAddress.setStatus("current")
_RuijieApInfoWireInRate_Type = Counter64
_RuijieApInfoWireInRate_Object = MibTableColumn
ruijieApInfoWireInRate = _RuijieApInfoWireInRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 18, 1, 2),
    _RuijieApInfoWireInRate_Type()
)
ruijieApInfoWireInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApInfoWireInRate.setStatus("current")
_RuijieApInfoWireOutRate_Type = Counter64
_RuijieApInfoWireOutRate_Object = MibTableColumn
ruijieApInfoWireOutRate = _RuijieApInfoWireOutRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 18, 1, 3),
    _RuijieApInfoWireOutRate_Type()
)
ruijieApInfoWireOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApInfoWireOutRate.setStatus("current")
_RuijieApInfoWireInOctets_Type = Counter64
_RuijieApInfoWireInOctets_Object = MibTableColumn
ruijieApInfoWireInOctets = _RuijieApInfoWireInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 18, 1, 4),
    _RuijieApInfoWireInOctets_Type()
)
ruijieApInfoWireInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApInfoWireInOctets.setStatus("current")
_RuijieApInfoWireOutOctets_Type = Counter64
_RuijieApInfoWireOutOctets_Object = MibTableColumn
ruijieApInfoWireOutOctets = _RuijieApInfoWireOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 18, 1, 5),
    _RuijieApInfoWireOutOctets_Type()
)
ruijieApInfoWireOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApInfoWireOutOctets.setStatus("current")
_RuijieIfDropTable_Object = MibTable
ruijieIfDropTable = _RuijieIfDropTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19)
)
if mibBuilder.loadTexts:
    ruijieIfDropTable.setStatus("current")
_RuijieIfDropEntry_Object = MibTableRow
ruijieIfDropEntry = _RuijieIfDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1)
)
ruijieIfDropEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfDropIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfDropEntry.setStatus("current")
_RuijieIfDropIndex_Type = Unsigned32
_RuijieIfDropIndex_Object = MibTableColumn
ruijieIfDropIndex = _RuijieIfDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 1),
    _RuijieIfDropIndex_Type()
)
ruijieIfDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfDropIndex.setStatus("current")
_RuijieIfInDropPkts_Type = Counter64
_RuijieIfInDropPkts_Object = MibTableColumn
ruijieIfInDropPkts = _RuijieIfInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 2),
    _RuijieIfInDropPkts_Type()
)
ruijieIfInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInDropPkts.setStatus("current")
_RuijieIfInResLackPkts_Type = Counter64
_RuijieIfInResLackPkts_Object = MibTableColumn
ruijieIfInResLackPkts = _RuijieIfInResLackPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 3),
    _RuijieIfInResLackPkts_Type()
)
ruijieIfInResLackPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInResLackPkts.setStatus("current")
_RuijieIfInQosDropPkts_Type = Counter64
_RuijieIfInQosDropPkts_Object = MibTableColumn
ruijieIfInQosDropPkts = _RuijieIfInQosDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 4),
    _RuijieIfInQosDropPkts_Type()
)
ruijieIfInQosDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInQosDropPkts.setStatus("current")
_RuijieIfFwdEntryDropPkts_Type = Counter64
_RuijieIfFwdEntryDropPkts_Object = MibTableColumn
ruijieIfFwdEntryDropPkts = _RuijieIfFwdEntryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 5),
    _RuijieIfFwdEntryDropPkts_Type()
)
ruijieIfFwdEntryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFwdEntryDropPkts.setStatus("current")
_RuijieIfOutDropPkts_Type = Counter64
_RuijieIfOutDropPkts_Object = MibTableColumn
ruijieIfOutDropPkts = _RuijieIfOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 6),
    _RuijieIfOutDropPkts_Type()
)
ruijieIfOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutDropPkts.setStatus("current")
_RuijieIfOutResLackPkts_Type = Counter64
_RuijieIfOutResLackPkts_Object = MibTableColumn
ruijieIfOutResLackPkts = _RuijieIfOutResLackPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 7),
    _RuijieIfOutResLackPkts_Type()
)
ruijieIfOutResLackPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutResLackPkts.setStatus("current")
_RuijieIfNoBufferCount_Type = Counter64
_RuijieIfNoBufferCount_Object = MibTableColumn
ruijieIfNoBufferCount = _RuijieIfNoBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 8),
    _RuijieIfNoBufferCount_Type()
)
ruijieIfNoBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfNoBufferCount.setStatus("current")
_RuijieIfOBMDropPkts_Type = Counter64
_RuijieIfOBMDropPkts_Object = MibTableColumn
ruijieIfOBMDropPkts = _RuijieIfOBMDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 9),
    _RuijieIfOBMDropPkts_Type()
)
ruijieIfOBMDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOBMDropPkts.setStatus("current")
_RuijieIfInErrorPkts_Type = Counter64
_RuijieIfInErrorPkts_Object = MibTableColumn
ruijieIfInErrorPkts = _RuijieIfInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 10),
    _RuijieIfInErrorPkts_Type()
)
ruijieIfInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfInErrorPkts.setStatus("current")
_RuijieIfOutErrorPkts_Type = Counter64
_RuijieIfOutErrorPkts_Object = MibTableColumn
ruijieIfOutErrorPkts = _RuijieIfOutErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 19, 1, 11),
    _RuijieIfOutErrorPkts_Type()
)
ruijieIfOutErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOutErrorPkts.setStatus("current")
_RuijieEthIfTable_Object = MibTable
ruijieEthIfTable = _RuijieEthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20)
)
if mibBuilder.loadTexts:
    ruijieEthIfTable.setStatus("current")
_RuijieEthStaEntry_Object = MibTableRow
ruijieEthStaEntry = _RuijieEthStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1)
)
ruijieEthStaEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieEthIndex"),
)
if mibBuilder.loadTexts:
    ruijieEthStaEntry.setStatus("current")
_RuijieEthIndex_Type = Unsigned32
_RuijieEthIndex_Object = MibTableColumn
ruijieEthIndex = _RuijieEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 1),
    _RuijieEthIndex_Type()
)
ruijieEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthIndex.setStatus("current")
_RuijieEthDiscard_Type = Counter64
_RuijieEthDiscard_Object = MibTableColumn
ruijieEthDiscard = _RuijieEthDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 2),
    _RuijieEthDiscard_Type()
)
ruijieEthDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDiscard.setStatus("current")
_RuijieEthBandwidthUsage_Type = DisplayString
_RuijieEthBandwidthUsage_Object = MibTableColumn
ruijieEthBandwidthUsage = _RuijieEthBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 3),
    _RuijieEthBandwidthUsage_Type()
)
ruijieEthBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthBandwidthUsage.setStatus("current")
_RuijieEthInOctets_Type = Counter64
_RuijieEthInOctets_Object = MibTableColumn
ruijieEthInOctets = _RuijieEthInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 4),
    _RuijieEthInOctets_Type()
)
ruijieEthInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInOctets.setStatus("current")
_RuijieEthInPkts_Type = Counter64
_RuijieEthInPkts_Object = MibTableColumn
ruijieEthInPkts = _RuijieEthInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 5),
    _RuijieEthInPkts_Type()
)
ruijieEthInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInPkts.setStatus("current")
_RuijieEthInBroadcastPkts_Type = Counter64
_RuijieEthInBroadcastPkts_Object = MibTableColumn
ruijieEthInBroadcastPkts = _RuijieEthInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 6),
    _RuijieEthInBroadcastPkts_Type()
)
ruijieEthInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInBroadcastPkts.setStatus("current")
_RuijieEthInMulticastPkts_Type = Counter64
_RuijieEthInMulticastPkts_Object = MibTableColumn
ruijieEthInMulticastPkts = _RuijieEthInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 7),
    _RuijieEthInMulticastPkts_Type()
)
ruijieEthInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInMulticastPkts.setStatus("current")
_RuijieEthInUcastPkts_Type = Counter64
_RuijieEthInUcastPkts_Object = MibTableColumn
ruijieEthInUcastPkts = _RuijieEthInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 8),
    _RuijieEthInUcastPkts_Type()
)
ruijieEthInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInUcastPkts.setStatus("current")
_RuijieEthInNUcastPkts_Type = Counter64
_RuijieEthInNUcastPkts_Object = MibTableColumn
ruijieEthInNUcastPkts = _RuijieEthInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 9),
    _RuijieEthInNUcastPkts_Type()
)
ruijieEthInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInNUcastPkts.setStatus("current")
_RuijieEthInResLackPkts_Type = Counter64
_RuijieEthInResLackPkts_Object = MibTableColumn
ruijieEthInResLackPkts = _RuijieEthInResLackPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 10),
    _RuijieEthInResLackPkts_Type()
)
ruijieEthInResLackPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInResLackPkts.setStatus("current")
_RuijieEthInDropPkts_Type = Counter64
_RuijieEthInDropPkts_Object = MibTableColumn
ruijieEthInDropPkts = _RuijieEthInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 11),
    _RuijieEthInDropPkts_Type()
)
ruijieEthInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInDropPkts.setStatus("current")
_RuijieEthInErrors_Type = Counter64
_RuijieEthInErrors_Object = MibTableColumn
ruijieEthInErrors = _RuijieEthInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 12),
    _RuijieEthInErrors_Type()
)
ruijieEthInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInErrors.setStatus("current")
_RuijieEthOBMDropPkts_Type = Counter64
_RuijieEthOBMDropPkts_Object = MibTableColumn
ruijieEthOBMDropPkts = _RuijieEthOBMDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 13),
    _RuijieEthOBMDropPkts_Type()
)
ruijieEthOBMDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOBMDropPkts.setStatus("current")
_RuijieEthNoBufferCount_Type = Counter64
_RuijieEthNoBufferCount_Object = MibTableColumn
ruijieEthNoBufferCount = _RuijieEthNoBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 14),
    _RuijieEthNoBufferCount_Type()
)
ruijieEthNoBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthNoBufferCount.setStatus("current")
_RuijieEthFwdEntryDropPkts_Type = Counter64
_RuijieEthFwdEntryDropPkts_Object = MibTableColumn
ruijieEthFwdEntryDropPkts = _RuijieEthFwdEntryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 15),
    _RuijieEthFwdEntryDropPkts_Type()
)
ruijieEthFwdEntryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthFwdEntryDropPkts.setStatus("current")
_RuijieEthInQosDropPkts_Type = Counter64
_RuijieEthInQosDropPkts_Object = MibTableColumn
ruijieEthInQosDropPkts = _RuijieEthInQosDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 16),
    _RuijieEthInQosDropPkts_Type()
)
ruijieEthInQosDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInQosDropPkts.setStatus("current")
_RuijieEthInUnknownProtos_Type = Counter64
_RuijieEthInUnknownProtos_Object = MibTableColumn
ruijieEthInUnknownProtos = _RuijieEthInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 17),
    _RuijieEthInUnknownProtos_Type()
)
ruijieEthInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInUnknownProtos.setStatus("current")
_RuijieEthInDropPktsRate_Type = DisplayString
_RuijieEthInDropPktsRate_Object = MibTableColumn
ruijieEthInDropPktsRate = _RuijieEthInDropPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 18),
    _RuijieEthInDropPktsRate_Type()
)
ruijieEthInDropPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInDropPktsRate.setStatus("current")
_RuijieEthInErrorPktsRate_Type = DisplayString
_RuijieEthInErrorPktsRate_Object = MibTableColumn
ruijieEthInErrorPktsRate = _RuijieEthInErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 19),
    _RuijieEthInErrorPktsRate_Type()
)
ruijieEthInErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInErrorPktsRate.setStatus("current")
_RuijieEthInPktRate_Type = Counter64
_RuijieEthInPktRate_Object = MibTableColumn
ruijieEthInPktRate = _RuijieEthInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 20),
    _RuijieEthInPktRate_Type()
)
ruijieEthInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInPktRate.setStatus("current")
_RuijieEthInBitsRate_Type = Counter64
_RuijieEthInBitsRate_Object = MibTableColumn
ruijieEthInBitsRate = _RuijieEthInBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 21),
    _RuijieEthInBitsRate_Type()
)
ruijieEthInBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInBitsRate.setStatus("current")
_RuijieEthInBandwidthUsage_Type = DisplayString
_RuijieEthInBandwidthUsage_Object = MibTableColumn
ruijieEthInBandwidthUsage = _RuijieEthInBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 22),
    _RuijieEthInBandwidthUsage_Type()
)
ruijieEthInBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthInBandwidthUsage.setStatus("current")
_RuijieEthRxPeakRate_Type = Counter64
_RuijieEthRxPeakRate_Object = MibTableColumn
ruijieEthRxPeakRate = _RuijieEthRxPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 23),
    _RuijieEthRxPeakRate_Type()
)
ruijieEthRxPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthRxPeakRate.setStatus("current")
_RuijieEthRxPeakRateTime_Type = DisplayString
_RuijieEthRxPeakRateTime_Object = MibTableColumn
ruijieEthRxPeakRateTime = _RuijieEthRxPeakRateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 24),
    _RuijieEthRxPeakRateTime_Type()
)
ruijieEthRxPeakRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthRxPeakRateTime.setStatus("current")
_RuijieEthOutOctets_Type = Counter64
_RuijieEthOutOctets_Object = MibTableColumn
ruijieEthOutOctets = _RuijieEthOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 25),
    _RuijieEthOutOctets_Type()
)
ruijieEthOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutOctets.setStatus("current")
_RuijieEthOutPkts_Type = Counter64
_RuijieEthOutPkts_Object = MibTableColumn
ruijieEthOutPkts = _RuijieEthOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 26),
    _RuijieEthOutPkts_Type()
)
ruijieEthOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutPkts.setStatus("current")
_RuijieEthOutBroadcastPkts_Type = Counter64
_RuijieEthOutBroadcastPkts_Object = MibTableColumn
ruijieEthOutBroadcastPkts = _RuijieEthOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 27),
    _RuijieEthOutBroadcastPkts_Type()
)
ruijieEthOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutBroadcastPkts.setStatus("current")
_RuijieEthOutMulticastPkts_Type = Counter64
_RuijieEthOutMulticastPkts_Object = MibTableColumn
ruijieEthOutMulticastPkts = _RuijieEthOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 28),
    _RuijieEthOutMulticastPkts_Type()
)
ruijieEthOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutMulticastPkts.setStatus("current")
_RuijieEthOutUcastPkts_Type = Counter64
_RuijieEthOutUcastPkts_Object = MibTableColumn
ruijieEthOutUcastPkts = _RuijieEthOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 29),
    _RuijieEthOutUcastPkts_Type()
)
ruijieEthOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutUcastPkts.setStatus("current")
_RuijieEthOutNUcastPkts_Type = Counter64
_RuijieEthOutNUcastPkts_Object = MibTableColumn
ruijieEthOutNUcastPkts = _RuijieEthOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 30),
    _RuijieEthOutNUcastPkts_Type()
)
ruijieEthOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutNUcastPkts.setStatus("current")
_RuijieEthOutResLackPkts_Type = Counter64
_RuijieEthOutResLackPkts_Object = MibTableColumn
ruijieEthOutResLackPkts = _RuijieEthOutResLackPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 31),
    _RuijieEthOutResLackPkts_Type()
)
ruijieEthOutResLackPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutResLackPkts.setStatus("current")
_RuijieEthOutDropPkts_Type = Counter64
_RuijieEthOutDropPkts_Object = MibTableColumn
ruijieEthOutDropPkts = _RuijieEthOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 32),
    _RuijieEthOutDropPkts_Type()
)
ruijieEthOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutDropPkts.setStatus("current")
_RuijieEthOutErrors_Type = Counter64
_RuijieEthOutErrors_Object = MibTableColumn
ruijieEthOutErrors = _RuijieEthOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 33),
    _RuijieEthOutErrors_Type()
)
ruijieEthOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutErrors.setStatus("current")
_RuijieEthOutCollisionPkts_Type = Counter64
_RuijieEthOutCollisionPkts_Object = MibTableColumn
ruijieEthOutCollisionPkts = _RuijieEthOutCollisionPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 34),
    _RuijieEthOutCollisionPkts_Type()
)
ruijieEthOutCollisionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutCollisionPkts.setStatus("current")
_RuijieEthOutDropPktsRate_Type = DisplayString
_RuijieEthOutDropPktsRate_Object = MibTableColumn
ruijieEthOutDropPktsRate = _RuijieEthOutDropPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 35),
    _RuijieEthOutDropPktsRate_Type()
)
ruijieEthOutDropPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutDropPktsRate.setStatus("current")
_RuijieEthOutErrorPktsRate_Type = DisplayString
_RuijieEthOutErrorPktsRate_Object = MibTableColumn
ruijieEthOutErrorPktsRate = _RuijieEthOutErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 36),
    _RuijieEthOutErrorPktsRate_Type()
)
ruijieEthOutErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutErrorPktsRate.setStatus("current")
_RuijieEthOutPktRate_Type = Counter64
_RuijieEthOutPktRate_Object = MibTableColumn
ruijieEthOutPktRate = _RuijieEthOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 37),
    _RuijieEthOutPktRate_Type()
)
ruijieEthOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutPktRate.setStatus("current")
_RuijieEthOutBitsRate_Type = Counter64
_RuijieEthOutBitsRate_Object = MibTableColumn
ruijieEthOutBitsRate = _RuijieEthOutBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 38),
    _RuijieEthOutBitsRate_Type()
)
ruijieEthOutBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutBitsRate.setStatus("current")
_RuijieEthOutBandwidthUsage_Type = DisplayString
_RuijieEthOutBandwidthUsage_Object = MibTableColumn
ruijieEthOutBandwidthUsage = _RuijieEthOutBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 39),
    _RuijieEthOutBandwidthUsage_Type()
)
ruijieEthOutBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthOutBandwidthUsage.setStatus("current")
_RuijieEthTxPeakRate_Type = Counter64
_RuijieEthTxPeakRate_Object = MibTableColumn
ruijieEthTxPeakRate = _RuijieEthTxPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 40),
    _RuijieEthTxPeakRate_Type()
)
ruijieEthTxPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthTxPeakRate.setStatus("current")
_RuijieEthTxPeakRateTime_Type = DisplayString
_RuijieEthTxPeakRateTime_Object = MibTableColumn
ruijieEthTxPeakRateTime = _RuijieEthTxPeakRateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 41),
    _RuijieEthTxPeakRateTime_Type()
)
ruijieEthTxPeakRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthTxPeakRateTime.setStatus("current")
_RuijieEthUplinkInOctets_Type = Counter64
_RuijieEthUplinkInOctets_Object = MibTableColumn
ruijieEthUplinkInOctets = _RuijieEthUplinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 42),
    _RuijieEthUplinkInOctets_Type()
)
ruijieEthUplinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkInOctets.setStatus("current")
_RuijieEthUplinkInUcastPkts_Type = Counter64
_RuijieEthUplinkInUcastPkts_Object = MibTableColumn
ruijieEthUplinkInUcastPkts = _RuijieEthUplinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 43),
    _RuijieEthUplinkInUcastPkts_Type()
)
ruijieEthUplinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkInUcastPkts.setStatus("current")
_RuijieEthUplinkInNUcastPkts_Type = Counter64
_RuijieEthUplinkInNUcastPkts_Object = MibTableColumn
ruijieEthUplinkInNUcastPkts = _RuijieEthUplinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 44),
    _RuijieEthUplinkInNUcastPkts_Type()
)
ruijieEthUplinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkInNUcastPkts.setStatus("deprecated")
_RuijieEthUplinkInDiscards_Type = Counter64
_RuijieEthUplinkInDiscards_Object = MibTableColumn
ruijieEthUplinkInDiscards = _RuijieEthUplinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 45),
    _RuijieEthUplinkInDiscards_Type()
)
ruijieEthUplinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkInDiscards.setStatus("current")
_RuijieEthUplinkInErrors_Type = Counter64
_RuijieEthUplinkInErrors_Object = MibTableColumn
ruijieEthUplinkInErrors = _RuijieEthUplinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 46),
    _RuijieEthUplinkInErrors_Type()
)
ruijieEthUplinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkInErrors.setStatus("current")
_RuijieEthUplinkOutOctets_Type = Counter64
_RuijieEthUplinkOutOctets_Object = MibTableColumn
ruijieEthUplinkOutOctets = _RuijieEthUplinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 47),
    _RuijieEthUplinkOutOctets_Type()
)
ruijieEthUplinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkOutOctets.setStatus("current")
_RuijieEthUplinkOutUcastPkts_Type = Counter64
_RuijieEthUplinkOutUcastPkts_Object = MibTableColumn
ruijieEthUplinkOutUcastPkts = _RuijieEthUplinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 48),
    _RuijieEthUplinkOutUcastPkts_Type()
)
ruijieEthUplinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkOutUcastPkts.setStatus("current")
_RuijieEthUplinkOutNUcastPkts_Type = Counter64
_RuijieEthUplinkOutNUcastPkts_Object = MibTableColumn
ruijieEthUplinkOutNUcastPkts = _RuijieEthUplinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 49),
    _RuijieEthUplinkOutNUcastPkts_Type()
)
ruijieEthUplinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkOutNUcastPkts.setStatus("deprecated")
_RuijieEthUplinkOutDiscards_Type = Counter64
_RuijieEthUplinkOutDiscards_Object = MibTableColumn
ruijieEthUplinkOutDiscards = _RuijieEthUplinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 50),
    _RuijieEthUplinkOutDiscards_Type()
)
ruijieEthUplinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkOutDiscards.setStatus("current")
_RuijieEthUplinkOutErrors_Type = Counter64
_RuijieEthUplinkOutErrors_Object = MibTableColumn
ruijieEthUplinkOutErrors = _RuijieEthUplinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 51),
    _RuijieEthUplinkOutErrors_Type()
)
ruijieEthUplinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkOutErrors.setStatus("current")
_RuijieEthUplinkInBcastPkts_Type = Counter64
_RuijieEthUplinkInBcastPkts_Object = MibTableColumn
ruijieEthUplinkInBcastPkts = _RuijieEthUplinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 52),
    _RuijieEthUplinkInBcastPkts_Type()
)
ruijieEthUplinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkInBcastPkts.setStatus("current")
_RuijieEthUplinkOutBcastPkts_Type = Counter64
_RuijieEthUplinkOutBcastPkts_Object = MibTableColumn
ruijieEthUplinkOutBcastPkts = _RuijieEthUplinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 53),
    _RuijieEthUplinkOutBcastPkts_Type()
)
ruijieEthUplinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthUplinkOutBcastPkts.setStatus("current")
_RuijieEthDownlinkInOctets_Type = Counter64
_RuijieEthDownlinkInOctets_Object = MibTableColumn
ruijieEthDownlinkInOctets = _RuijieEthDownlinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 54),
    _RuijieEthDownlinkInOctets_Type()
)
ruijieEthDownlinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkInOctets.setStatus("current")
_RuijieEthDownlinkInUcastPkts_Type = Counter64
_RuijieEthDownlinkInUcastPkts_Object = MibTableColumn
ruijieEthDownlinkInUcastPkts = _RuijieEthDownlinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 55),
    _RuijieEthDownlinkInUcastPkts_Type()
)
ruijieEthDownlinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkInUcastPkts.setStatus("current")
_RuijieEthDownlinkInNUcastPkts_Type = Counter64
_RuijieEthDownlinkInNUcastPkts_Object = MibTableColumn
ruijieEthDownlinkInNUcastPkts = _RuijieEthDownlinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 56),
    _RuijieEthDownlinkInNUcastPkts_Type()
)
ruijieEthDownlinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkInNUcastPkts.setStatus("deprecated")
_RuijieEthDownlinkInDiscards_Type = Counter64
_RuijieEthDownlinkInDiscards_Object = MibTableColumn
ruijieEthDownlinkInDiscards = _RuijieEthDownlinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 57),
    _RuijieEthDownlinkInDiscards_Type()
)
ruijieEthDownlinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkInDiscards.setStatus("current")
_RuijieEthDownlinkInErrors_Type = Counter64
_RuijieEthDownlinkInErrors_Object = MibTableColumn
ruijieEthDownlinkInErrors = _RuijieEthDownlinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 58),
    _RuijieEthDownlinkInErrors_Type()
)
ruijieEthDownlinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkInErrors.setStatus("current")
_RuijieEthDownlinkOutOctets_Type = Counter64
_RuijieEthDownlinkOutOctets_Object = MibTableColumn
ruijieEthDownlinkOutOctets = _RuijieEthDownlinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 59),
    _RuijieEthDownlinkOutOctets_Type()
)
ruijieEthDownlinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkOutOctets.setStatus("current")
_RuijieEthDownlinkOutUcastPkts_Type = Counter64
_RuijieEthDownlinkOutUcastPkts_Object = MibTableColumn
ruijieEthDownlinkOutUcastPkts = _RuijieEthDownlinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 60),
    _RuijieEthDownlinkOutUcastPkts_Type()
)
ruijieEthDownlinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkOutUcastPkts.setStatus("current")
_RuijieEthDownlinkOutNUcastPkts_Type = Counter64
_RuijieEthDownlinkOutNUcastPkts_Object = MibTableColumn
ruijieEthDownlinkOutNUcastPkts = _RuijieEthDownlinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 61),
    _RuijieEthDownlinkOutNUcastPkts_Type()
)
ruijieEthDownlinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkOutNUcastPkts.setStatus("deprecated")
_RuijieEthDownlinkOutDiscards_Type = Counter64
_RuijieEthDownlinkOutDiscards_Object = MibTableColumn
ruijieEthDownlinkOutDiscards = _RuijieEthDownlinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 62),
    _RuijieEthDownlinkOutDiscards_Type()
)
ruijieEthDownlinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkOutDiscards.setStatus("current")
_RuijieEthDownlinkOutErrors_Type = Counter64
_RuijieEthDownlinkOutErrors_Object = MibTableColumn
ruijieEthDownlinkOutErrors = _RuijieEthDownlinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 63),
    _RuijieEthDownlinkOutErrors_Type()
)
ruijieEthDownlinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkOutErrors.setStatus("current")
_RuijieEthDownlinkInBcastPkts_Type = Counter64
_RuijieEthDownlinkInBcastPkts_Object = MibTableColumn
ruijieEthDownlinkInBcastPkts = _RuijieEthDownlinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 64),
    _RuijieEthDownlinkInBcastPkts_Type()
)
ruijieEthDownlinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkInBcastPkts.setStatus("current")
_RuijieEthDownlinkOutBcastPkts_Type = Counter64
_RuijieEthDownlinkOutBcastPkts_Object = MibTableColumn
ruijieEthDownlinkOutBcastPkts = _RuijieEthDownlinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 65),
    _RuijieEthDownlinkOutBcastPkts_Type()
)
ruijieEthDownlinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthDownlinkOutBcastPkts.setStatus("current")
_RuijieEthBitErrorRate_Type = DisplayString
_RuijieEthBitErrorRate_Object = MibTableColumn
ruijieEthBitErrorRate = _RuijieEthBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 20, 1, 66),
    _RuijieEthBitErrorRate_Type()
)
ruijieEthBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEthBitErrorRate.setStatus("current")
_RuijieIfOMCTable_Object = MibTable
ruijieIfOMCTable = _RuijieIfOMCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21)
)
if mibBuilder.loadTexts:
    ruijieIfOMCTable.setStatus("current")
_RuijieIfOMCEntry_Object = MibTableRow
ruijieIfOMCEntry = _RuijieIfOMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1)
)
ruijieIfOMCEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfOMCIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfOMCEntry.setStatus("current")
_RuijieIfOMCIndex_Type = InterfaceIndex
_RuijieIfOMCIndex_Object = MibTableColumn
ruijieIfOMCIndex = _RuijieIfOMCIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 1),
    _RuijieIfOMCIndex_Type()
)
ruijieIfOMCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCIndex.setStatus("current")


class _RuijieIfOMCNativeName_Type(DisplayString):
    """Custom type ruijieIfOMCNativeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieIfOMCNativeName_Type.__name__ = "DisplayString"
_RuijieIfOMCNativeName_Object = MibTableColumn
ruijieIfOMCNativeName = _RuijieIfOMCNativeName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 2),
    _RuijieIfOMCNativeName_Type()
)
ruijieIfOMCNativeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfOMCNativeName.setStatus("current")


class _RuijieIfOMCPhysicalOrLogical_Type(Integer32):
    """Custom type ruijieIfOMCPhysicalOrLogical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ptp", 2),
          ("ftp", 3))
    )


_RuijieIfOMCPhysicalOrLogical_Type.__name__ = "Integer32"
_RuijieIfOMCPhysicalOrLogical_Object = MibTableColumn
ruijieIfOMCPhysicalOrLogical = _RuijieIfOMCPhysicalOrLogical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 3),
    _RuijieIfOMCPhysicalOrLogical_Type()
)
ruijieIfOMCPhysicalOrLogical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCPhysicalOrLogical.setStatus("current")


class _RuijieIfOMCPortType_Type(Integer32):
    """Custom type ruijieIfOMCPortType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("eth", 2),
          ("pos", 3),
          ("lag", 4),
          ("ve", 5),
          ("trunk", 6),
          ("vlan", 7),
          ("other", 8))
    )


_RuijieIfOMCPortType_Type.__name__ = "Integer32"
_RuijieIfOMCPortType_Object = MibTableColumn
ruijieIfOMCPortType = _RuijieIfOMCPortType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 4),
    _RuijieIfOMCPortType_Type()
)
ruijieIfOMCPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCPortType.setStatus("current")


class _RuijieIfOMCPortSubType_Type(DisplayString):
    """Custom type ruijieIfOMCPortSubType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieIfOMCPortSubType_Type.__name__ = "DisplayString"
_RuijieIfOMCPortSubType_Object = MibTableColumn
ruijieIfOMCPortSubType = _RuijieIfOMCPortSubType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 5),
    _RuijieIfOMCPortSubType_Type()
)
ruijieIfOMCPortSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCPortSubType.setStatus("current")


class _RuijieIfOMCSignalType_Type(Integer32):
    """Custom type ruijieIfOMCSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("optical", 2),
          ("electrical", 3),
          ("invalid", 4))
    )


_RuijieIfOMCSignalType_Type.__name__ = "Integer32"
_RuijieIfOMCSignalType_Object = MibTableColumn
ruijieIfOMCSignalType = _RuijieIfOMCSignalType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 6),
    _RuijieIfOMCSignalType_Type()
)
ruijieIfOMCSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCSignalType.setStatus("current")
_RuijieIfOMCSlotInformation_Type = DisplayString
_RuijieIfOMCSlotInformation_Object = MibTableColumn
ruijieIfOMCSlotInformation = _RuijieIfOMCSlotInformation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 7),
    _RuijieIfOMCSlotInformation_Type()
)
ruijieIfOMCSlotInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCSlotInformation.setStatus("current")


class _RuijieIfOMCCVID_Type(DisplayString):
    """Custom type ruijieIfOMCCVID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RuijieIfOMCCVID_Type.__name__ = "DisplayString"
_RuijieIfOMCCVID_Object = MibTableColumn
ruijieIfOMCCVID = _RuijieIfOMCCVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 21, 1, 8),
    _RuijieIfOMCCVID_Type()
)
ruijieIfOMCCVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCCVID.setStatus("current")
_RuijieIfOMCBindMainTable_Object = MibTable
ruijieIfOMCBindMainTable = _RuijieIfOMCBindMainTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 22)
)
if mibBuilder.loadTexts:
    ruijieIfOMCBindMainTable.setStatus("current")
_RuijieIfOMCBindMainEntry_Object = MibTableRow
ruijieIfOMCBindMainEntry = _RuijieIfOMCBindMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 22, 1)
)
ruijieIfOMCBindMainEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfOMCBindMainIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfOMCBindMainEntry.setStatus("current")
_RuijieIfOMCBindMainIndex_Type = InterfaceIndex
_RuijieIfOMCBindMainIndex_Object = MibTableColumn
ruijieIfOMCBindMainIndex = _RuijieIfOMCBindMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 22, 1, 1),
    _RuijieIfOMCBindMainIndex_Type()
)
ruijieIfOMCBindMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCBindMainIndex.setStatus("current")


class _RuijieIfOMCBindType_Type(Integer32):
    """Custom type ruijieIfOMCBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("logicAndPhy", 2),
          ("subAndMain", 3))
    )


_RuijieIfOMCBindType_Type.__name__ = "Integer32"
_RuijieIfOMCBindType_Object = MibTableColumn
ruijieIfOMCBindType = _RuijieIfOMCBindType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 22, 1, 2),
    _RuijieIfOMCBindType_Type()
)
ruijieIfOMCBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOMCBindType.setStatus("current")
_RuijieIfSubInterfaceTable_Object = MibTable
ruijieIfSubInterfaceTable = _RuijieIfSubInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 24)
)
if mibBuilder.loadTexts:
    ruijieIfSubInterfaceTable.setStatus("current")
_RuijieIfSubInterfaceEntry_Object = MibTableRow
ruijieIfSubInterfaceEntry = _RuijieIfSubInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 24, 1)
)
ruijieIfSubInterfaceEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfSubInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfSubInterfaceEntry.setStatus("current")
_RuijieIfSubInterfaceIndex_Type = InterfaceIndex
_RuijieIfSubInterfaceIndex_Object = MibTableColumn
ruijieIfSubInterfaceIndex = _RuijieIfSubInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 24, 1, 1),
    _RuijieIfSubInterfaceIndex_Type()
)
ruijieIfSubInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfSubInterfaceIndex.setStatus("current")
_RuijieIfMainInterface_Type = Integer32
_RuijieIfMainInterface_Object = MibTableColumn
ruijieIfMainInterface = _RuijieIfMainInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 1, 24, 1, 2),
    _RuijieIfMainInterface_Type()
)
ruijieIfMainInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfMainInterface.setStatus("current")
_RuijieInterfaceTraps_ObjectIdentity = ObjectIdentity
ruijieInterfaceTraps = _RuijieInterfaceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2)
)


class _LineDetectStatus_Type(Integer32):
    """Custom type lineDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("open", 2),
          ("short", 3))
    )


_LineDetectStatus_Type.__name__ = "Integer32"
_LineDetectStatus_Object = MibScalar
lineDetectStatus = _LineDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 1),
    _LineDetectStatus_Type()
)
lineDetectStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectStatus.setStatus("current")
_LineDetectPosition_Type = Integer32
_LineDetectPosition_Object = MibScalar
lineDetectPosition = _LineDetectPosition_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 2),
    _LineDetectPosition_Type()
)
lineDetectPosition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectPosition.setStatus("current")
_RuijieIfInBwUsageRisingThreshold_Type = Integer32
_RuijieIfInBwUsageRisingThreshold_Object = MibScalar
ruijieIfInBwUsageRisingThreshold = _RuijieIfInBwUsageRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 4),
    _RuijieIfInBwUsageRisingThreshold_Type()
)
ruijieIfInBwUsageRisingThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIfInBwUsageRisingThreshold.setStatus("current")
_RuijieIfOutBwUsageRisingThreshold_Type = Integer32
_RuijieIfOutBwUsageRisingThreshold_Object = MibScalar
ruijieIfOutBwUsageRisingThreshold = _RuijieIfOutBwUsageRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 5),
    _RuijieIfOutBwUsageRisingThreshold_Type()
)
ruijieIfOutBwUsageRisingThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIfOutBwUsageRisingThreshold.setStatus("current")
_RuijieIfInBwUsageResumeThreshold_Type = Integer32
_RuijieIfInBwUsageResumeThreshold_Object = MibScalar
ruijieIfInBwUsageResumeThreshold = _RuijieIfInBwUsageResumeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 6),
    _RuijieIfInBwUsageResumeThreshold_Type()
)
ruijieIfInBwUsageResumeThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIfInBwUsageResumeThreshold.setStatus("current")
_RuijieIfOutBwUsageResumeThreshold_Type = Integer32
_RuijieIfOutBwUsageResumeThreshold_Object = MibScalar
ruijieIfOutBwUsageResumeThreshold = _RuijieIfOutBwUsageResumeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 7),
    _RuijieIfOutBwUsageResumeThreshold_Type()
)
ruijieIfOutBwUsageResumeThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIfOutBwUsageResumeThreshold.setStatus("current")


class _RuijieIfErrdisableReason_Type(DisplayString):
    """Custom type ruijieIfErrdisableReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieIfErrdisableReason_Type.__name__ = "DisplayString"
_RuijieIfErrdisableReason_Object = MibScalar
ruijieIfErrdisableReason = _RuijieIfErrdisableReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 14),
    _RuijieIfErrdisableReason_Type()
)
ruijieIfErrdisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfErrdisableReason.setStatus("current")


class _RuijieLicenseInstanceName_Type(DisplayString):
    """Custom type ruijieLicenseInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieLicenseInstanceName_Type.__name__ = "DisplayString"
_RuijieLicenseInstanceName_Object = MibScalar
ruijieLicenseInstanceName = _RuijieLicenseInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 17),
    _RuijieLicenseInstanceName_Type()
)
ruijieLicenseInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieLicenseInstanceName.setStatus("current")


class _RuijieIfPortSpeed_Type(DisplayString):
    """Custom type ruijieIfPortSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieIfPortSpeed_Type.__name__ = "DisplayString"
_RuijieIfPortSpeed_Object = MibScalar
ruijieIfPortSpeed = _RuijieIfPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 21),
    _RuijieIfPortSpeed_Type()
)
ruijieIfPortSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIfPortSpeed.setStatus("current")


class _RuijieIfHardwareAlarmType_Type(Integer32):
    """Custom type ruijieIfHardwareAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("uControllerException", 2))
    )


_RuijieIfHardwareAlarmType_Type.__name__ = "Integer32"
_RuijieIfHardwareAlarmType_Object = MibScalar
ruijieIfHardwareAlarmType = _RuijieIfHardwareAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 23),
    _RuijieIfHardwareAlarmType_Type()
)
ruijieIfHardwareAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIfHardwareAlarmType.setStatus("current")


class _RuijieIfHardwareAlarmDesc_Type(DisplayString):
    """Custom type ruijieIfHardwareAlarmDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieIfHardwareAlarmDesc_Type.__name__ = "DisplayString"
_RuijieIfHardwareAlarmDesc_Object = MibScalar
ruijieIfHardwareAlarmDesc = _RuijieIfHardwareAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 24),
    _RuijieIfHardwareAlarmDesc_Type()
)
ruijieIfHardwareAlarmDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIfHardwareAlarmDesc.setStatus("current")
_RuijieInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
ruijieInterfaceMIBConformance = _RuijieInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3)
)
_RuijieInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieInterfaceMIBCompliances = _RuijieInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 1)
)
_RuijieInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
ruijieInterfaceMIBGroups = _RuijieInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 2)
)

# Managed Objects groups

ruijieInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 2, 1)
)
ruijieInterfaceMIBGroup.setObjects(
      *(("RUIJIE-INTERFACE-MIB", "ruijieIfIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfPortType"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfFlowControlAdminStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfFlowControlOperStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfAdminSpeed"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfAdminDuplex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOperSpeed"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOperDuplex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfManageStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfIpBroadcast"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfLayer"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfMode"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfCounterClear"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfEntryStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfMediumType"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownCounter"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfBcastInhibit"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfNegotiation"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfPhysAddress"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfAdminSpeedRW"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfAdminDuplexRW"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfModeRW"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfSpeed"),
        ("RUIJIE-INTERFACE-MIB", "ruijieifAdminStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieifOperStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUpDownTimes"),
        ("RUIJIE-INTERFACE-MIB", "ruijieifAdminStatusw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieifOperStatusw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieifSpeedw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieifMacAddress"),
        ("RUIJIE-INTERFACE-MIB", "ruijieifLastChange"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDiscard"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfBandwidthUsage"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInBitsRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInPktRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutBitsRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutPktRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInBandwidthUsage"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutBandwidthUsage"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInErrorPktsRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutErrorPktsRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInDropPktsRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutDropPktsRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfIpIfIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfIpId"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfIp"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfIpMask"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfIpEntryStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfStatusIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfStatusLoopBackExamine"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfErrorStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieGlobalIfDisableRecovery"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfSVICreatVlanNum"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfHandleSVI"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfEncapsulationIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfEncapsulationVlan"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApPhyAddress"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfNumber"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfPhyIntNum"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApPhysAddress"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfType"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfMtu"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfSpeed"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfPhysAddress"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfAdminStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOperStatus"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfLastChange"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInDiscards"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInErrors"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInUnknownProtos"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutDiscards"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutErrors"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutQLen"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfLinkUPTimes"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInDataOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutDataOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfMgmtUploadOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfMgmtDownloadOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfSpeedw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfMtuw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfPhysAddressw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInUcastPktsw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInNUcastPktsw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutUcastPktsw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutNUcastPktsw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfLinkUPTimesw"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInFlow"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutFlow"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInBrdcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutBrdcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInMulcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutMulcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInPayloadOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutPayloadOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfAlias"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfInDateRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutDateRate"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApifInNormalPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieApIfOutPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfLinkIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkInOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkInUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkInNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkInDiscards"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkInErrors"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkOutOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkOutUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkOutNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkOutDiscards"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkOutErrors"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkInOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkInUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkInNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkInDiscards"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkInErrors"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkOutOctets"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkOutUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkOutNUcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkOutDiscards"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkOutErrors"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkInBcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfUplinkOutBcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkInBcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfDownlinkOutBcastPkts"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfNeighborIP"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfNeighborIPv6"))
)
if mibBuilder.loadTexts:
    ruijieInterfaceMIBGroup.setStatus("current")

ruijiePortTypeChooseMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 2, 2)
)
ruijiePortTypeChooseMibGroup.setObjects(
      *(("RUIJIE-INTERFACE-MIB", "ruijiePortTypeChooseIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijiePortTypeChooseType"))
)
if mibBuilder.loadTexts:
    ruijiePortTypeChooseMibGroup.setStatus("current")

ruijieIfMTUMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 2, 3)
)
ruijieIfMTUMibGroup.setObjects(
      *(("RUIJIE-INTERFACE-MIB", "ruijieIfMTUIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfMTU"))
)
if mibBuilder.loadTexts:
    ruijieIfMTUMibGroup.setStatus("current")

ruijieIfLineDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 2, 4)
)
ruijieIfLineDetectGroup.setObjects(
    ("RUIJIE-INTERFACE-MIB", "ruijieIfLineDetect")
)
if mibBuilder.loadTexts:
    ruijieIfLineDetectGroup.setStatus("current")

ruijieIfAvailableBWMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 2, 5)
)
ruijieIfAvailableBWMibGroup.setObjects(
      *(("RUIJIE-INTERFACE-MIB", "ruijieIfAvailableBWIfIndex"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfAvailableBWIfBW"))
)
if mibBuilder.loadTexts:
    ruijieIfAvailableBWMibGroup.setStatus("current")


# Notification objects

lineQualityDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 3)
)
lineQualityDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUIJIE-INTERFACE-MIB", "lineDetectStatus"),
        ("RUIJIE-INTERFACE-MIB", "lineDetectPosition"))
)
if mibBuilder.loadTexts:
    lineQualityDetect.setStatus(
        "current"
    )

ruijieIfInBwUsageRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 8)
)
ruijieIfInBwUsageRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInBandwidthUsage"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInBwUsageRisingThreshold"))
)
if mibBuilder.loadTexts:
    ruijieIfInBwUsageRising.setStatus(
        "current"
    )

ruijieIfInBwUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 9)
)
ruijieIfInBwUsageResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInBandwidthUsage"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfInBwUsageResumeThreshold"))
)
if mibBuilder.loadTexts:
    ruijieIfInBwUsageResume.setStatus(
        "current"
    )

ruijieIfOutBwUsageRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 10)
)
ruijieIfOutBwUsageRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutBandwidthUsage"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutBwUsageRisingThreshold"))
)
if mibBuilder.loadTexts:
    ruijieIfOutBwUsageRising.setStatus(
        "current"
    )

ruijieIfOutBwUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 11)
)
ruijieIfOutBwUsageResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutBandwidthUsage"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfOutBwUsageResumeThreshold"))
)
if mibBuilder.loadTexts:
    ruijieIfOutBwUsageResume.setStatus(
        "current"
    )

ruijieIfLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 12)
)
ruijieIfLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    ruijieIfLinkDown.setStatus(
        "current"
    )

ruijieIfLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 13)
)
ruijieIfLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    ruijieIfLinkUp.setStatus(
        "current"
    )

ruijieIfErrdisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 15)
)
ruijieIfErrdisable.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfErrdisableReason"))
)
if mibBuilder.loadTexts:
    ruijieIfErrdisable.setStatus(
        "current"
    )

ruijieIfErrdisableResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 16)
)
ruijieIfErrdisableResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfErrdisableReason"))
)
if mibBuilder.loadTexts:
    ruijieIfErrdisableResume.setStatus(
        "current"
    )

ruijieIfInGracePeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 18)
)
ruijieIfInGracePeriod.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieLicenseInstanceName"))
)
if mibBuilder.loadTexts:
    ruijieIfInGracePeriod.setStatus(
        "current"
    )

ruijieIfInGracePeriodResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 19)
)
ruijieIfInGracePeriodResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieLicenseInstanceName"))
)
if mibBuilder.loadTexts:
    ruijieIfInGracePeriodResume.setStatus(
        "current"
    )

ruijieIfDither = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 20)
)
ruijieIfDither.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ruijieIfDither.setStatus(
        "current"
    )

ruijieIfPortSpeedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 22)
)
ruijieIfPortSpeedChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfPortSpeed"))
)
if mibBuilder.loadTexts:
    ruijieIfPortSpeedChange.setStatus(
        "current"
    )

ruijieIfHardwareAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 25)
)
ruijieIfHardwareAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfHardwareAlarmType"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfHardwareAlarmDesc"))
)
if mibBuilder.loadTexts:
    ruijieIfHardwareAlarm.setStatus(
        "current"
    )

ruijieIfHardwareAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 2, 26)
)
ruijieIfHardwareAlarmResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfHardwareAlarmType"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfHardwareAlarmDesc"))
)
if mibBuilder.loadTexts:
    ruijieIfHardwareAlarmResume.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 3, 1, 1)
)
ruijieInterfaceMIBCompliance.setObjects(
      *(("RUIJIE-INTERFACE-MIB", "ruijieInterfaceMIBGroup"),
        ("RUIJIE-INTERFACE-MIB", "ruijiePortTypeChooseMibGroup"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfMTUMibGroup"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfLineDetectGroup"),
        ("RUIJIE-INTERFACE-MIB", "ruijieIfAvailableBWMibGroup"))
)
if mibBuilder.loadTexts:
    ruijieInterfaceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-INTERFACE-MIB",
    **{"ruijieInterfaceMIB": ruijieInterfaceMIB,
       "ruijieIfConfigMIBObjects": ruijieIfConfigMIBObjects,
       "ruijieIfTable": ruijieIfTable,
       "ruijieIfEntry": ruijieIfEntry,
       "ruijieIfIndex": ruijieIfIndex,
       "ruijieIfPortType": ruijieIfPortType,
       "ruijieIfFlowControlAdminStatus": ruijieIfFlowControlAdminStatus,
       "ruijieIfFlowControlOperStatus": ruijieIfFlowControlOperStatus,
       "ruijieIfAdminSpeed": ruijieIfAdminSpeed,
       "ruijieIfAdminDuplex": ruijieIfAdminDuplex,
       "ruijieIfOperSpeed": ruijieIfOperSpeed,
       "ruijieIfOperDuplex": ruijieIfOperDuplex,
       "ruijieIfManageStatus": ruijieIfManageStatus,
       "ruijieIfIpBroadcast": ruijieIfIpBroadcast,
       "ruijieIfLayer": ruijieIfLayer,
       "ruijieIfMode": ruijieIfMode,
       "ruijieIfCounterClear": ruijieIfCounterClear,
       "ruijieIfEntryStatus": ruijieIfEntryStatus,
       "ruijieIfMediumType": ruijieIfMediumType,
       "ruijieIfDownCounter": ruijieIfDownCounter,
       "ruijieIfInOctets": ruijieIfInOctets,
       "ruijieIfOutOctets": ruijieIfOutOctets,
       "ruijieIfBcastInhibit": ruijieIfBcastInhibit,
       "ruijieIfNegotiation": ruijieIfNegotiation,
       "ruijieIfPhysAddress": ruijieIfPhysAddress,
       "ruijieIfAdminSpeedRW": ruijieIfAdminSpeedRW,
       "ruijieIfAdminDuplexRW": ruijieIfAdminDuplexRW,
       "ruijieIfModeRW": ruijieIfModeRW,
       "ruijieIfSpeed": ruijieIfSpeed,
       "ruijieifAdminStatus": ruijieifAdminStatus,
       "ruijieifOperStatus": ruijieifOperStatus,
       "ruijieIfInNUcastPkts": ruijieIfInNUcastPkts,
       "ruijieIfOutNUcastPkts": ruijieIfOutNUcastPkts,
       "ruijieIfUpDownTimes": ruijieIfUpDownTimes,
       "ruijieifAdminStatusw": ruijieifAdminStatusw,
       "ruijieifOperStatusw": ruijieifOperStatusw,
       "ruijieifSpeedw": ruijieifSpeedw,
       "ruijieifMacAddress": ruijieifMacAddress,
       "ruijieifLastChange": ruijieifLastChange,
       "ruijieIfInPkts": ruijieIfInPkts,
       "ruijieIfDiscard": ruijieIfDiscard,
       "ruijieIfBandwidthUsage": ruijieIfBandwidthUsage,
       "ruijieIfInBitsRate": ruijieIfInBitsRate,
       "ruijieIfInPktRate": ruijieIfInPktRate,
       "ruijieIfOutBitsRate": ruijieIfOutBitsRate,
       "ruijieIfOutPktRate": ruijieIfOutPktRate,
       "ruijieIfInBandwidthUsage": ruijieIfInBandwidthUsage,
       "ruijieIfOutBandwidthUsage": ruijieIfOutBandwidthUsage,
       "ruijieIfInErrorPktsRate": ruijieIfInErrorPktsRate,
       "ruijieIfOutErrorPktsRate": ruijieIfOutErrorPktsRate,
       "ruijieIfInDropPktsRate": ruijieIfInDropPktsRate,
       "ruijieIfOutDropPktsRate": ruijieIfOutDropPktsRate,
       "ruijieIfOutNoBuffer": ruijieIfOutNoBuffer,
       "ruijieIfOutPkts": ruijieIfOutPkts,
       "ruijieIfNeighborIP": ruijieIfNeighborIP,
       "ruijieIfNeighborIPv6": ruijieIfNeighborIPv6,
       "ruijieIfIsSubPort": ruijieIfIsSubPort,
       "ruijieIfDemux": ruijieIfDemux,
       "ruijieIfDemuxChannelId": ruijieIfDemuxChannelId,
       "ruijieIfInFecCorrect": ruijieIfInFecCorrect,
       "ruijieIfInFecUnCorrect": ruijieIfInFecUnCorrect,
       "ruijieIfLinkDownReason": ruijieIfLinkDownReason,
       "ruijieIfIpTable": ruijieIfIpTable,
       "ruijieIfIpEntry": ruijieIfIpEntry,
       "ruijieIfIpIfIndex": ruijieIfIpIfIndex,
       "ruijieIfIpId": ruijieIfIpId,
       "ruijieIfIp": ruijieIfIp,
       "ruijieIfIpMask": ruijieIfIpMask,
       "ruijieIfIpEntryStatus": ruijieIfIpEntryStatus,
       "ruijieIfStatusTable": ruijieIfStatusTable,
       "ruijieIfStatusEntry": ruijieIfStatusEntry,
       "ruijieIfStatusIndex": ruijieIfStatusIndex,
       "ruijieIfStatusLoopBackExamine": ruijieIfStatusLoopBackExamine,
       "ruijieIfErrorStatus": ruijieIfErrorStatus,
       "ruijieIfLineDetect": ruijieIfLineDetect,
       "ruijieGlobalIfDisableRecovery": ruijieGlobalIfDisableRecovery,
       "ruijiePortTypeChooseTable": ruijiePortTypeChooseTable,
       "ruijiePortTypeChooseEntry": ruijiePortTypeChooseEntry,
       "ruijiePortTypeChooseIndex": ruijiePortTypeChooseIndex,
       "ruijiePortTypeChooseType": ruijiePortTypeChooseType,
       "ruijieIfMTUTable": ruijieIfMTUTable,
       "ruijieIfMTUEntry": ruijieIfMTUEntry,
       "ruijieIfMTUIndex": ruijieIfMTUIndex,
       "ruijieIfMTU": ruijieIfMTU,
       "ruijieIfAvailableBWTable": ruijieIfAvailableBWTable,
       "ruijieIfAvailableBWEntry": ruijieIfAvailableBWEntry,
       "ruijieIfAvailableBWIfIndex": ruijieIfAvailableBWIfIndex,
       "ruijieIfAvailableBWIfBW": ruijieIfAvailableBWIfBW,
       "ruijieIfSVICreatTable": ruijieIfSVICreatTable,
       "ruijieIfSVICreatEntry": ruijieIfSVICreatEntry,
       "ruijieIfSVICreatVlanNum": ruijieIfSVICreatVlanNum,
       "ruijieIfHandleSVI": ruijieIfHandleSVI,
       "ruijieIfPhyIntNum": ruijieIfPhyIntNum,
       "ruijieIfLinkUPTimesTable": ruijieIfLinkUPTimesTable,
       "ruijieIfLinkUPTimesEntry": ruijieIfLinkUPTimesEntry,
       "ruijieInterfaceIndex": ruijieInterfaceIndex,
       "ruijieIfLinkUPTimes": ruijieIfLinkUPTimes,
       "ruijieIfEncapsulationTable": ruijieIfEncapsulationTable,
       "ruijieIfEncapsulationEntry": ruijieIfEncapsulationEntry,
       "ruijieIfEncapsulationIndex": ruijieIfEncapsulationIndex,
       "ruijieIfEncapsulationVlan": ruijieIfEncapsulationVlan,
       "ruijieApIfNumberTable": ruijieApIfNumberTable,
       "ruijieApIfNumberEntry": ruijieApIfNumberEntry,
       "ruijieApPhyAddress": ruijieApPhyAddress,
       "ruijieApIfNumber": ruijieApIfNumber,
       "ruijieApIfPhyIntNum": ruijieApIfPhyIntNum,
       "ruijieApIfTable": ruijieApIfTable,
       "ruijieApIfEntry": ruijieApIfEntry,
       "ruijieApPhysAddress": ruijieApPhysAddress,
       "ruijieApIfIndex": ruijieApIfIndex,
       "ruijieApIfDescr": ruijieApIfDescr,
       "ruijieApIfType": ruijieApIfType,
       "ruijieApIfMtu": ruijieApIfMtu,
       "ruijieApIfSpeed": ruijieApIfSpeed,
       "ruijieApIfPhysAddress": ruijieApIfPhysAddress,
       "ruijieApIfAdminStatus": ruijieApIfAdminStatus,
       "ruijieApIfOperStatus": ruijieApIfOperStatus,
       "ruijieApIfLastChange": ruijieApIfLastChange,
       "ruijieApIfInOctets": ruijieApIfInOctets,
       "ruijieApIfInUcastPkts": ruijieApIfInUcastPkts,
       "ruijieApIfInNUcastPkts": ruijieApIfInNUcastPkts,
       "ruijieApIfInDiscards": ruijieApIfInDiscards,
       "ruijieApIfInErrors": ruijieApIfInErrors,
       "ruijieApIfInUnknownProtos": ruijieApIfInUnknownProtos,
       "ruijieApIfOutOctets": ruijieApIfOutOctets,
       "ruijieApIfOutUcastPkts": ruijieApIfOutUcastPkts,
       "ruijieApIfOutNUcastPkts": ruijieApIfOutNUcastPkts,
       "ruijieApIfOutDiscards": ruijieApIfOutDiscards,
       "ruijieApIfOutErrors": ruijieApIfOutErrors,
       "ruijieApIfOutQLen": ruijieApIfOutQLen,
       "ruijieApIfLinkUPTimes": ruijieApIfLinkUPTimes,
       "ruijieApIfInDataOctets": ruijieApIfInDataOctets,
       "ruijieApIfOutDataOctets": ruijieApIfOutDataOctets,
       "ruijieApIfMgmtUploadOctets": ruijieApIfMgmtUploadOctets,
       "ruijieApIfMgmtDownloadOctets": ruijieApIfMgmtDownloadOctets,
       "ruijieApIfSpeedw": ruijieApIfSpeedw,
       "ruijieApIfMtuw": ruijieApIfMtuw,
       "ruijieApIfPhysAddressw": ruijieApIfPhysAddressw,
       "ruijieApIfInUcastPktsw": ruijieApIfInUcastPktsw,
       "ruijieApIfInNUcastPktsw": ruijieApIfInNUcastPktsw,
       "ruijieApIfOutUcastPktsw": ruijieApIfOutUcastPktsw,
       "ruijieApIfOutNUcastPktsw": ruijieApIfOutNUcastPktsw,
       "ruijieApIfLinkUPTimesw": ruijieApIfLinkUPTimesw,
       "ruijieApIfInPkts": ruijieApIfInPkts,
       "ruijieApIfInFlow": ruijieApIfInFlow,
       "ruijieApIfOutFlow": ruijieApIfOutFlow,
       "ruijieApIfInBrdcastPkts": ruijieApIfInBrdcastPkts,
       "ruijieApIfOutBrdcastPkts": ruijieApIfOutBrdcastPkts,
       "ruijieApIfInMulcastPkts": ruijieApIfInMulcastPkts,
       "ruijieApIfOutMulcastPkts": ruijieApIfOutMulcastPkts,
       "ruijieApIfInPayloadOctets": ruijieApIfInPayloadOctets,
       "ruijieApIfOutPayloadOctets": ruijieApIfOutPayloadOctets,
       "ruijieApIfAlias": ruijieApIfAlias,
       "ruijieApIfInDateRate": ruijieApIfInDateRate,
       "ruijieApIfOutDateRate": ruijieApIfOutDateRate,
       "ruijieApifInNormalPkts": ruijieApifInNormalPkts,
       "ruijieApIfOutPkts": ruijieApIfOutPkts,
       "ruijieIfLinkTable": ruijieIfLinkTable,
       "ruijieIfLinkEntry": ruijieIfLinkEntry,
       "ruijieIfLinkIndex": ruijieIfLinkIndex,
       "ruijieIfUplinkInOctets": ruijieIfUplinkInOctets,
       "ruijieIfUplinkInUcastPkts": ruijieIfUplinkInUcastPkts,
       "ruijieIfUplinkInNUcastPkts": ruijieIfUplinkInNUcastPkts,
       "ruijieIfUplinkInDiscards": ruijieIfUplinkInDiscards,
       "ruijieIfUplinkInErrors": ruijieIfUplinkInErrors,
       "ruijieIfUplinkOutOctets": ruijieIfUplinkOutOctets,
       "ruijieIfUplinkOutUcastPkts": ruijieIfUplinkOutUcastPkts,
       "ruijieIfUplinkOutNUcastPkts": ruijieIfUplinkOutNUcastPkts,
       "ruijieIfUplinkOutDiscards": ruijieIfUplinkOutDiscards,
       "ruijieIfUplinkOutErrors": ruijieIfUplinkOutErrors,
       "ruijieIfDownlinkInOctets": ruijieIfDownlinkInOctets,
       "ruijieIfDownlinkInUcastPkts": ruijieIfDownlinkInUcastPkts,
       "ruijieIfDownlinkInNUcastPkts": ruijieIfDownlinkInNUcastPkts,
       "ruijieIfDownlinkInDiscards": ruijieIfDownlinkInDiscards,
       "ruijieIfDownlinkInErrors": ruijieIfDownlinkInErrors,
       "ruijieIfDownlinkOutOctets": ruijieIfDownlinkOutOctets,
       "ruijieIfDownlinkOutUcastPkts": ruijieIfDownlinkOutUcastPkts,
       "ruijieIfDownlinkOutNUcastPkts": ruijieIfDownlinkOutNUcastPkts,
       "ruijieIfDownlinkOutDiscards": ruijieIfDownlinkOutDiscards,
       "ruijieIfDownlinkOutErrors": ruijieIfDownlinkOutErrors,
       "ruijieIfUplinkInBcastPkts": ruijieIfUplinkInBcastPkts,
       "ruijieIfUplinkOutBcastPkts": ruijieIfUplinkOutBcastPkts,
       "ruijieIfDownlinkInBcastPkts": ruijieIfDownlinkInBcastPkts,
       "ruijieIfDownlinkOutBcastPkts": ruijieIfDownlinkOutBcastPkts,
       "ruijieIfTrafficStatisticsObjects": ruijieIfTrafficStatisticsObjects,
       "ruijieIfLinkTrafficStatistics": ruijieIfLinkTrafficStatistics,
       "ruijieIfLinkTrafficTable": ruijieIfLinkTrafficTable,
       "ruijieIfLinkTrafficEntry": ruijieIfLinkTrafficEntry,
       "ruijieIfLinkTrafficIndex": ruijieIfLinkTrafficIndex,
       "ruijieIfLinkAvgRate": ruijieIfLinkAvgRate,
       "ruijieIfLinkPeakRate": ruijieIfLinkPeakRate,
       "ruijieIfLinkAvgBWUtilization": ruijieIfLinkAvgBWUtilization,
       "ruijieIfLinkPeakBWUtilization": ruijieIfLinkPeakBWUtilization,
       "ruijieIfLinkQosStatistics": ruijieIfLinkQosStatistics,
       "ruijieLinkQosCtlTable": ruijieLinkQosCtlTable,
       "ruijieLinkQosCtlEntry": ruijieLinkQosCtlEntry,
       "ruijieLinkQosCtlOwnerIndex": ruijieLinkQosCtlOwnerIndex,
       "ruijieLinkQosCtlTestName": ruijieLinkQosCtlTestName,
       "ruijieLinkQosCtlTargetAddressType": ruijieLinkQosCtlTargetAddressType,
       "ruijieLinkQosCtlTargetAddress": ruijieLinkQosCtlTargetAddress,
       "ruijieLinkQosCtlAdminStatus": ruijieLinkQosCtlAdminStatus,
       "ruijieLinkQosCtlRowStatus": ruijieLinkQosCtlRowStatus,
       "ruijieLinkQosResultsTable": ruijieLinkQosResultsTable,
       "ruijieLinkQosResultsEntry": ruijieLinkQosResultsEntry,
       "ruijieLinkQosResultsOperStatus": ruijieLinkQosResultsOperStatus,
       "ruijieLinkQosResultsIpTargetAddressType": ruijieLinkQosResultsIpTargetAddressType,
       "ruijieLinkQosResultsIpTargetAddress": ruijieLinkQosResultsIpTargetAddress,
       "ruijieLinkQosResultsMaxRtt": ruijieLinkQosResultsMaxRtt,
       "ruijieLinkQosResultsMinRtt": ruijieLinkQosResultsMinRtt,
       "ruijieLinkQosResultsAverageRtt": ruijieLinkQosResultsAverageRtt,
       "ruijieLinkQosResultsDelayJitter": ruijieLinkQosResultsDelayJitter,
       "ruijieLinkQosResultsPktsLossRate": ruijieLinkQosResultsPktsLossRate,
       "ruijieLinkQosResultsNetworkAF": ruijieLinkQosResultsNetworkAF,
       "ruijieIfDeviceTrafficStatistics": ruijieIfDeviceTrafficStatistics,
       "ruijieIfDeviceTrafficTable": ruijieIfDeviceTrafficTable,
       "ruijieIfDeviceTrafficEntry": ruijieIfDeviceTrafficEntry,
       "ruijieIfDeviceTrafficIndex": ruijieIfDeviceTrafficIndex,
       "ruijieIfFC": ruijieIfFC,
       "ruijieIfFCTransRate": ruijieIfFCTransRate,
       "ruijieIfFCTransPktsNum": ruijieIfFCTransPktsNum,
       "ruijieIfFCDiscardRate": ruijieIfFCDiscardRate,
       "ruijieIfFCDiscardPktsNum": ruijieIfFCDiscardPktsNum,
       "ruijieIfFCPktsLossRate": ruijieIfFCPktsLossRate,
       "ruijieIfFCBandwidthRate": ruijieIfFCBandwidthRate,
       "ruijieIfFCBandwidthPercentage": ruijieIfFCBandwidthPercentage,
       "ruijieIfDeviceFCGathers": ruijieIfDeviceFCGathers,
       "ruijieIfFullMeshFCGathers": ruijieIfFullMeshFCGathers,
       "ruijieIfClassBasedGathers": ruijieIfClassBasedGathers,
       "ruijieIfNodeBasedGathers": ruijieIfNodeBasedGathers,
       "ruijieIfNodeClassBasedGathers": ruijieIfNodeClassBasedGathers,
       "ruijieIfNodeFCBasedGathers": ruijieIfNodeFCBasedGathers,
       "ruijieIfNodeDeviceFCBasedGathers": ruijieIfNodeDeviceFCBasedGathers,
       "ruijieIfPhyTable": ruijieIfPhyTable,
       "ruijieIfPhyEntry": ruijieIfPhyEntry,
       "ruijieIfPhyIndex": ruijieIfPhyIndex,
       "ruijieifPhyOperStatus": ruijieifPhyOperStatus,
       "ruijieIfPeakRateTable": ruijieIfPeakRateTable,
       "ruijieIfPeakRateEntry": ruijieIfPeakRateEntry,
       "ruijieIfPeakRateIndex": ruijieIfPeakRateIndex,
       "ruijieIfRxPeakRate": ruijieIfRxPeakRate,
       "ruijieIfRxPeakRateTime": ruijieIfRxPeakRateTime,
       "ruijieIfTxPeakRate": ruijieIfTxPeakRate,
       "ruijieIfTxPeakRateTime": ruijieIfTxPeakRateTime,
       "ruijieApInfoTable": ruijieApInfoTable,
       "ruijieApInfoEntry": ruijieApInfoEntry,
       "ruijieApInfoAddress": ruijieApInfoAddress,
       "ruijieApInfoWireInRate": ruijieApInfoWireInRate,
       "ruijieApInfoWireOutRate": ruijieApInfoWireOutRate,
       "ruijieApInfoWireInOctets": ruijieApInfoWireInOctets,
       "ruijieApInfoWireOutOctets": ruijieApInfoWireOutOctets,
       "ruijieIfDropTable": ruijieIfDropTable,
       "ruijieIfDropEntry": ruijieIfDropEntry,
       "ruijieIfDropIndex": ruijieIfDropIndex,
       "ruijieIfInDropPkts": ruijieIfInDropPkts,
       "ruijieIfInResLackPkts": ruijieIfInResLackPkts,
       "ruijieIfInQosDropPkts": ruijieIfInQosDropPkts,
       "ruijieIfFwdEntryDropPkts": ruijieIfFwdEntryDropPkts,
       "ruijieIfOutDropPkts": ruijieIfOutDropPkts,
       "ruijieIfOutResLackPkts": ruijieIfOutResLackPkts,
       "ruijieIfNoBufferCount": ruijieIfNoBufferCount,
       "ruijieIfOBMDropPkts": ruijieIfOBMDropPkts,
       "ruijieIfInErrorPkts": ruijieIfInErrorPkts,
       "ruijieIfOutErrorPkts": ruijieIfOutErrorPkts,
       "ruijieEthIfTable": ruijieEthIfTable,
       "ruijieEthStaEntry": ruijieEthStaEntry,
       "ruijieEthIndex": ruijieEthIndex,
       "ruijieEthDiscard": ruijieEthDiscard,
       "ruijieEthBandwidthUsage": ruijieEthBandwidthUsage,
       "ruijieEthInOctets": ruijieEthInOctets,
       "ruijieEthInPkts": ruijieEthInPkts,
       "ruijieEthInBroadcastPkts": ruijieEthInBroadcastPkts,
       "ruijieEthInMulticastPkts": ruijieEthInMulticastPkts,
       "ruijieEthInUcastPkts": ruijieEthInUcastPkts,
       "ruijieEthInNUcastPkts": ruijieEthInNUcastPkts,
       "ruijieEthInResLackPkts": ruijieEthInResLackPkts,
       "ruijieEthInDropPkts": ruijieEthInDropPkts,
       "ruijieEthInErrors": ruijieEthInErrors,
       "ruijieEthOBMDropPkts": ruijieEthOBMDropPkts,
       "ruijieEthNoBufferCount": ruijieEthNoBufferCount,
       "ruijieEthFwdEntryDropPkts": ruijieEthFwdEntryDropPkts,
       "ruijieEthInQosDropPkts": ruijieEthInQosDropPkts,
       "ruijieEthInUnknownProtos": ruijieEthInUnknownProtos,
       "ruijieEthInDropPktsRate": ruijieEthInDropPktsRate,
       "ruijieEthInErrorPktsRate": ruijieEthInErrorPktsRate,
       "ruijieEthInPktRate": ruijieEthInPktRate,
       "ruijieEthInBitsRate": ruijieEthInBitsRate,
       "ruijieEthInBandwidthUsage": ruijieEthInBandwidthUsage,
       "ruijieEthRxPeakRate": ruijieEthRxPeakRate,
       "ruijieEthRxPeakRateTime": ruijieEthRxPeakRateTime,
       "ruijieEthOutOctets": ruijieEthOutOctets,
       "ruijieEthOutPkts": ruijieEthOutPkts,
       "ruijieEthOutBroadcastPkts": ruijieEthOutBroadcastPkts,
       "ruijieEthOutMulticastPkts": ruijieEthOutMulticastPkts,
       "ruijieEthOutUcastPkts": ruijieEthOutUcastPkts,
       "ruijieEthOutNUcastPkts": ruijieEthOutNUcastPkts,
       "ruijieEthOutResLackPkts": ruijieEthOutResLackPkts,
       "ruijieEthOutDropPkts": ruijieEthOutDropPkts,
       "ruijieEthOutErrors": ruijieEthOutErrors,
       "ruijieEthOutCollisionPkts": ruijieEthOutCollisionPkts,
       "ruijieEthOutDropPktsRate": ruijieEthOutDropPktsRate,
       "ruijieEthOutErrorPktsRate": ruijieEthOutErrorPktsRate,
       "ruijieEthOutPktRate": ruijieEthOutPktRate,
       "ruijieEthOutBitsRate": ruijieEthOutBitsRate,
       "ruijieEthOutBandwidthUsage": ruijieEthOutBandwidthUsage,
       "ruijieEthTxPeakRate": ruijieEthTxPeakRate,
       "ruijieEthTxPeakRateTime": ruijieEthTxPeakRateTime,
       "ruijieEthUplinkInOctets": ruijieEthUplinkInOctets,
       "ruijieEthUplinkInUcastPkts": ruijieEthUplinkInUcastPkts,
       "ruijieEthUplinkInNUcastPkts": ruijieEthUplinkInNUcastPkts,
       "ruijieEthUplinkInDiscards": ruijieEthUplinkInDiscards,
       "ruijieEthUplinkInErrors": ruijieEthUplinkInErrors,
       "ruijieEthUplinkOutOctets": ruijieEthUplinkOutOctets,
       "ruijieEthUplinkOutUcastPkts": ruijieEthUplinkOutUcastPkts,
       "ruijieEthUplinkOutNUcastPkts": ruijieEthUplinkOutNUcastPkts,
       "ruijieEthUplinkOutDiscards": ruijieEthUplinkOutDiscards,
       "ruijieEthUplinkOutErrors": ruijieEthUplinkOutErrors,
       "ruijieEthUplinkInBcastPkts": ruijieEthUplinkInBcastPkts,
       "ruijieEthUplinkOutBcastPkts": ruijieEthUplinkOutBcastPkts,
       "ruijieEthDownlinkInOctets": ruijieEthDownlinkInOctets,
       "ruijieEthDownlinkInUcastPkts": ruijieEthDownlinkInUcastPkts,
       "ruijieEthDownlinkInNUcastPkts": ruijieEthDownlinkInNUcastPkts,
       "ruijieEthDownlinkInDiscards": ruijieEthDownlinkInDiscards,
       "ruijieEthDownlinkInErrors": ruijieEthDownlinkInErrors,
       "ruijieEthDownlinkOutOctets": ruijieEthDownlinkOutOctets,
       "ruijieEthDownlinkOutUcastPkts": ruijieEthDownlinkOutUcastPkts,
       "ruijieEthDownlinkOutNUcastPkts": ruijieEthDownlinkOutNUcastPkts,
       "ruijieEthDownlinkOutDiscards": ruijieEthDownlinkOutDiscards,
       "ruijieEthDownlinkOutErrors": ruijieEthDownlinkOutErrors,
       "ruijieEthDownlinkInBcastPkts": ruijieEthDownlinkInBcastPkts,
       "ruijieEthDownlinkOutBcastPkts": ruijieEthDownlinkOutBcastPkts,
       "ruijieEthBitErrorRate": ruijieEthBitErrorRate,
       "ruijieIfOMCTable": ruijieIfOMCTable,
       "ruijieIfOMCEntry": ruijieIfOMCEntry,
       "ruijieIfOMCIndex": ruijieIfOMCIndex,
       "ruijieIfOMCNativeName": ruijieIfOMCNativeName,
       "ruijieIfOMCPhysicalOrLogical": ruijieIfOMCPhysicalOrLogical,
       "ruijieIfOMCPortType": ruijieIfOMCPortType,
       "ruijieIfOMCPortSubType": ruijieIfOMCPortSubType,
       "ruijieIfOMCSignalType": ruijieIfOMCSignalType,
       "ruijieIfOMCSlotInformation": ruijieIfOMCSlotInformation,
       "ruijieIfOMCCVID": ruijieIfOMCCVID,
       "ruijieIfOMCBindMainTable": ruijieIfOMCBindMainTable,
       "ruijieIfOMCBindMainEntry": ruijieIfOMCBindMainEntry,
       "ruijieIfOMCBindMainIndex": ruijieIfOMCBindMainIndex,
       "ruijieIfOMCBindType": ruijieIfOMCBindType,
       "ruijieIfSubInterfaceTable": ruijieIfSubInterfaceTable,
       "ruijieIfSubInterfaceEntry": ruijieIfSubInterfaceEntry,
       "ruijieIfSubInterfaceIndex": ruijieIfSubInterfaceIndex,
       "ruijieIfMainInterface": ruijieIfMainInterface,
       "ruijieInterfaceTraps": ruijieInterfaceTraps,
       "lineDetectStatus": lineDetectStatus,
       "lineDetectPosition": lineDetectPosition,
       "lineQualityDetect": lineQualityDetect,
       "ruijieIfInBwUsageRisingThreshold": ruijieIfInBwUsageRisingThreshold,
       "ruijieIfOutBwUsageRisingThreshold": ruijieIfOutBwUsageRisingThreshold,
       "ruijieIfInBwUsageResumeThreshold": ruijieIfInBwUsageResumeThreshold,
       "ruijieIfOutBwUsageResumeThreshold": ruijieIfOutBwUsageResumeThreshold,
       "ruijieIfInBwUsageRising": ruijieIfInBwUsageRising,
       "ruijieIfInBwUsageResume": ruijieIfInBwUsageResume,
       "ruijieIfOutBwUsageRising": ruijieIfOutBwUsageRising,
       "ruijieIfOutBwUsageResume": ruijieIfOutBwUsageResume,
       "ruijieIfLinkDown": ruijieIfLinkDown,
       "ruijieIfLinkUp": ruijieIfLinkUp,
       "ruijieIfErrdisableReason": ruijieIfErrdisableReason,
       "ruijieIfErrdisable": ruijieIfErrdisable,
       "ruijieIfErrdisableResume": ruijieIfErrdisableResume,
       "ruijieLicenseInstanceName": ruijieLicenseInstanceName,
       "ruijieIfInGracePeriod": ruijieIfInGracePeriod,
       "ruijieIfInGracePeriodResume": ruijieIfInGracePeriodResume,
       "ruijieIfDither": ruijieIfDither,
       "ruijieIfPortSpeed": ruijieIfPortSpeed,
       "ruijieIfPortSpeedChange": ruijieIfPortSpeedChange,
       "ruijieIfHardwareAlarmType": ruijieIfHardwareAlarmType,
       "ruijieIfHardwareAlarmDesc": ruijieIfHardwareAlarmDesc,
       "ruijieIfHardwareAlarm": ruijieIfHardwareAlarm,
       "ruijieIfHardwareAlarmResume": ruijieIfHardwareAlarmResume,
       "ruijieInterfaceMIBConformance": ruijieInterfaceMIBConformance,
       "ruijieInterfaceMIBCompliances": ruijieInterfaceMIBCompliances,
       "ruijieInterfaceMIBCompliance": ruijieInterfaceMIBCompliance,
       "ruijieInterfaceMIBGroups": ruijieInterfaceMIBGroups,
       "ruijieInterfaceMIBGroup": ruijieInterfaceMIBGroup,
       "ruijiePortTypeChooseMibGroup": ruijiePortTypeChooseMibGroup,
       "ruijieIfMTUMibGroup": ruijieIfMTUMibGroup,
       "ruijieIfLineDetectGroup": ruijieIfLineDetectGroup,
       "ruijieIfAvailableBWMibGroup": ruijieIfAvailableBWMibGroup}
)
