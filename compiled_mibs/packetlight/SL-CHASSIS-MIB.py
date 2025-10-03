# SNMP MIB module (SL-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:44 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slChassis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlChassisInfo_ObjectIdentity = ObjectIdentity
slChassisInfo = _SlChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1)
)
_SlChassisInfoNodeSlotId_Type = Integer32
_SlChassisInfoNodeSlotId_Object = MibScalar
slChassisInfoNodeSlotId = _SlChassisInfoNodeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 1),
    _SlChassisInfoNodeSlotId_Type()
)
slChassisInfoNodeSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slChassisInfoNodeSlotId.setStatus("current")


class _SlChassisInfoNodeRole_Type(Integer32):
    """Custom type slChassisInfoNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gneNode", 1),
          ("internalSlotNode", 2),
          ("none", 3))
    )


_SlChassisInfoNodeRole_Type.__name__ = "Integer32"
_SlChassisInfoNodeRole_Object = MibScalar
slChassisInfoNodeRole = _SlChassisInfoNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 2),
    _SlChassisInfoNodeRole_Type()
)
slChassisInfoNodeRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slChassisInfoNodeRole.setStatus("current")
_SlChassisInfoLanVrrpIp_Type = IpAddress
_SlChassisInfoLanVrrpIp_Object = MibScalar
slChassisInfoLanVrrpIp = _SlChassisInfoLanVrrpIp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 3),
    _SlChassisInfoLanVrrpIp_Type()
)
slChassisInfoLanVrrpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slChassisInfoLanVrrpIp.setStatus("current")
_SlChassisInfoOscVrrpIp_Type = IpAddress
_SlChassisInfoOscVrrpIp_Object = MibScalar
slChassisInfoOscVrrpIp = _SlChassisInfoOscVrrpIp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 4),
    _SlChassisInfoOscVrrpIp_Type()
)
slChassisInfoOscVrrpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slChassisInfoOscVrrpIp.setStatus("current")


class _SlChassisInfoTopology_Type(Integer32):
    """Custom type slChassisInfoTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("osc", 1),
          ("lan", 2),
          ("simple", 3))
    )


_SlChassisInfoTopology_Type.__name__ = "Integer32"
_SlChassisInfoTopology_Object = MibScalar
slChassisInfoTopology = _SlChassisInfoTopology_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 5),
    _SlChassisInfoTopology_Type()
)
slChassisInfoTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slChassisInfoTopology.setStatus("current")


class _SlChassisInfoVrrpEnable_Type(Integer32):
    """Custom type slChassisInfoVrrpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SlChassisInfoVrrpEnable_Type.__name__ = "Integer32"
_SlChassisInfoVrrpEnable_Object = MibScalar
slChassisInfoVrrpEnable = _SlChassisInfoVrrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 6),
    _SlChassisInfoVrrpEnable_Type()
)
slChassisInfoVrrpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slChassisInfoVrrpEnable.setStatus("current")
_SlChassisSlot_ObjectIdentity = ObjectIdentity
slChassisSlot = _SlChassisSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2)
)
_SlChassisSlotTable_Object = MibTable
slChassisSlotTable = _SlChassisSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1)
)
if mibBuilder.loadTexts:
    slChassisSlotTable.setStatus("current")
_SlChassisSlotEntry_Object = MibTableRow
slChassisSlotEntry = _SlChassisSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1)
)
slChassisSlotEntry.setIndexNames(
    (0, "SL-CHASSIS-MIB", "slChassisSlotId"),
)
if mibBuilder.loadTexts:
    slChassisSlotEntry.setStatus("current")
_SlChassisSlotId_Type = Integer32
_SlChassisSlotId_Object = MibTableColumn
slChassisSlotId = _SlChassisSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 1),
    _SlChassisSlotId_Type()
)
slChassisSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotId.setStatus("current")


class _SlChassisSlotRole_Type(Integer32):
    """Custom type slChassisSlotRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gneNode", 1),
          ("internalNode", 2))
    )


_SlChassisSlotRole_Type.__name__ = "Integer32"
_SlChassisSlotRole_Object = MibTableColumn
slChassisSlotRole = _SlChassisSlotRole_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 2),
    _SlChassisSlotRole_Type()
)
slChassisSlotRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotRole.setStatus("current")
_SlChassisSlotInternalIp_Type = IpAddress
_SlChassisSlotInternalIp_Object = MibTableColumn
slChassisSlotInternalIp = _SlChassisSlotInternalIp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 3),
    _SlChassisSlotInternalIp_Type()
)
slChassisSlotInternalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotInternalIp.setStatus("current")
_SlChassisSlotProductType_Type = ObjectIdentifier
_SlChassisSlotProductType_Object = MibTableColumn
slChassisSlotProductType = _SlChassisSlotProductType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 4),
    _SlChassisSlotProductType_Type()
)
slChassisSlotProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotProductType.setStatus("current")


class _SlChassisSlotSysName_Type(DisplayString):
    """Custom type slChassisSlotSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlChassisSlotSysName_Type.__name__ = "DisplayString"
_SlChassisSlotSysName_Object = MibTableColumn
slChassisSlotSysName = _SlChassisSlotSysName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 5),
    _SlChassisSlotSysName_Type()
)
slChassisSlotSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotSysName.setStatus("current")
_SlChassisSlotSnmp161Port_Type = Integer32
_SlChassisSlotSnmp161Port_Object = MibTableColumn
slChassisSlotSnmp161Port = _SlChassisSlotSnmp161Port_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 6),
    _SlChassisSlotSnmp161Port_Type()
)
slChassisSlotSnmp161Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotSnmp161Port.setStatus("current")
_SlChassisSlotSnmp162MinPort_Type = Integer32
_SlChassisSlotSnmp162MinPort_Object = MibTableColumn
slChassisSlotSnmp162MinPort = _SlChassisSlotSnmp162MinPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 7),
    _SlChassisSlotSnmp162MinPort_Type()
)
slChassisSlotSnmp162MinPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotSnmp162MinPort.setStatus("current")
_SlChassisSlotSnmp162MaxPort_Type = Integer32
_SlChassisSlotSnmp162MaxPort_Object = MibTableColumn
slChassisSlotSnmp162MaxPort = _SlChassisSlotSnmp162MaxPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 8),
    _SlChassisSlotSnmp162MaxPort_Type()
)
slChassisSlotSnmp162MaxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotSnmp162MaxPort.setStatus("current")
_SlChassisSlotHttpPort_Type = Integer32
_SlChassisSlotHttpPort_Object = MibTableColumn
slChassisSlotHttpPort = _SlChassisSlotHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 9),
    _SlChassisSlotHttpPort_Type()
)
slChassisSlotHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotHttpPort.setStatus("current")
_SlChassisSlotTelnetPort_Type = Integer32
_SlChassisSlotTelnetPort_Object = MibTableColumn
slChassisSlotTelnetPort = _SlChassisSlotTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 10),
    _SlChassisSlotTelnetPort_Type()
)
slChassisSlotTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotTelnetPort.setStatus("current")
_SlChassisSlotFtpPort_Type = Integer32
_SlChassisSlotFtpPort_Object = MibTableColumn
slChassisSlotFtpPort = _SlChassisSlotFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 12),
    _SlChassisSlotFtpPort_Type()
)
slChassisSlotFtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotFtpPort.setStatus("current")
_SlChassisSlotTL1Port_Type = Integer32
_SlChassisSlotTL1Port_Object = MibTableColumn
slChassisSlotTL1Port = _SlChassisSlotTL1Port_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 13),
    _SlChassisSlotTL1Port_Type()
)
slChassisSlotTL1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotTL1Port.setStatus("current")
_SlChassisSlotPingIdentifier_Type = Integer32
_SlChassisSlotPingIdentifier_Object = MibTableColumn
slChassisSlotPingIdentifier = _SlChassisSlotPingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 14),
    _SlChassisSlotPingIdentifier_Type()
)
slChassisSlotPingIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotPingIdentifier.setStatus("current")
_SlChassisSlotHttpsPort_Type = Integer32
_SlChassisSlotHttpsPort_Object = MibTableColumn
slChassisSlotHttpsPort = _SlChassisSlotHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 15),
    _SlChassisSlotHttpsPort_Type()
)
slChassisSlotHttpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotHttpsPort.setStatus("current")
_SlChassisSlotSshPort_Type = Integer32
_SlChassisSlotSshPort_Object = MibTableColumn
slChassisSlotSshPort = _SlChassisSlotSshPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 16),
    _SlChassisSlotSshPort_Type()
)
slChassisSlotSshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotSshPort.setStatus("current")
_SlChassisSlotSTL1Port_Type = Integer32
_SlChassisSlotSTL1Port_Object = MibTableColumn
slChassisSlotSTL1Port = _SlChassisSlotSTL1Port_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 17),
    _SlChassisSlotSTL1Port_Type()
)
slChassisSlotSTL1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slChassisSlotSTL1Port.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-CHASSIS-MIB",
    **{"slChassis": slChassis,
       "slChassisInfo": slChassisInfo,
       "slChassisInfoNodeSlotId": slChassisInfoNodeSlotId,
       "slChassisInfoNodeRole": slChassisInfoNodeRole,
       "slChassisInfoLanVrrpIp": slChassisInfoLanVrrpIp,
       "slChassisInfoOscVrrpIp": slChassisInfoOscVrrpIp,
       "slChassisInfoTopology": slChassisInfoTopology,
       "slChassisInfoVrrpEnable": slChassisInfoVrrpEnable,
       "slChassisSlot": slChassisSlot,
       "slChassisSlotTable": slChassisSlotTable,
       "slChassisSlotEntry": slChassisSlotEntry,
       "slChassisSlotId": slChassisSlotId,
       "slChassisSlotRole": slChassisSlotRole,
       "slChassisSlotInternalIp": slChassisSlotInternalIp,
       "slChassisSlotProductType": slChassisSlotProductType,
       "slChassisSlotSysName": slChassisSlotSysName,
       "slChassisSlotSnmp161Port": slChassisSlotSnmp161Port,
       "slChassisSlotSnmp162MinPort": slChassisSlotSnmp162MinPort,
       "slChassisSlotSnmp162MaxPort": slChassisSlotSnmp162MaxPort,
       "slChassisSlotHttpPort": slChassisSlotHttpPort,
       "slChassisSlotTelnetPort": slChassisSlotTelnetPort,
       "slChassisSlotFtpPort": slChassisSlotFtpPort,
       "slChassisSlotTL1Port": slChassisSlotTL1Port,
       "slChassisSlotPingIdentifier": slChassisSlotPingIdentifier,
       "slChassisSlotHttpsPort": slChassisSlotHttpsPort,
       "slChassisSlotSshPort": slChassisSlotSshPort,
       "slChassisSlotSTL1Port": slChassisSlotSTL1Port}
)
