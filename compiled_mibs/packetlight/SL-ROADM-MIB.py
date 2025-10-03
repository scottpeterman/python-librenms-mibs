# SNMP MIB module (SL-ROADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-ROADM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:03 2025
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

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slROADM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ROCHProvisioningType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("exp", 2),
          ("add", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SlROADMConfig_ObjectIdentity = ObjectIdentity
slROADMConfig = _SlROADMConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1)
)
_SlWSSConfigTable_Object = MibTable
slWSSConfigTable = _SlWSSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    slWSSConfigTable.setStatus("current")
_SlWSSConfigEntry_Object = MibTableRow
slWSSConfigEntry = _SlWSSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1)
)
slWSSConfigEntry.setIndexNames(
    (0, "SL-ROADM-MIB", "slWSSConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slWSSConfigEntry.setStatus("current")
_SlWSSConfigLineIndex_Type = InterfaceIndex
_SlWSSConfigLineIndex_Object = MibTableColumn
slWSSConfigLineIndex = _SlWSSConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 1),
    _SlWSSConfigLineIndex_Type()
)
slWSSConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigLineIndex.setStatus("current")
_SlWSSConfigOperStatus_Type = Integer32
_SlWSSConfigOperStatus_Object = MibTableColumn
slWSSConfigOperStatus = _SlWSSConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 2),
    _SlWSSConfigOperStatus_Type()
)
slWSSConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigOperStatus.setStatus("current")
_SlWSSConfigSwitchTemp_Type = Integer32
_SlWSSConfigSwitchTemp_Object = MibTableColumn
slWSSConfigSwitchTemp = _SlWSSConfigSwitchTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 3),
    _SlWSSConfigSwitchTemp_Type()
)
slWSSConfigSwitchTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigSwitchTemp.setStatus("current")
_SlWSSConfigBoardTemp_Type = Integer32
_SlWSSConfigBoardTemp_Object = MibTableColumn
slWSSConfigBoardTemp = _SlWSSConfigBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 4),
    _SlWSSConfigBoardTemp_Type()
)
slWSSConfigBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigBoardTemp.setStatus("current")
_SlWSSConfigCaseTemp_Type = Integer32
_SlWSSConfigCaseTemp_Object = MibTableColumn
slWSSConfigCaseTemp = _SlWSSConfigCaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 5),
    _SlWSSConfigCaseTemp_Type()
)
slWSSConfigCaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigCaseTemp.setStatus("current")
_SlWSSConfigUptime_Type = Integer32
_SlWSSConfigUptime_Object = MibTableColumn
slWSSConfigUptime = _SlWSSConfigUptime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 6),
    _SlWSSConfigUptime_Type()
)
slWSSConfigUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigUptime.setStatus("current")
_SlWSSConfigComFirstWl_Type = Integer32
_SlWSSConfigComFirstWl_Object = MibTableColumn
slWSSConfigComFirstWl = _SlWSSConfigComFirstWl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 7),
    _SlWSSConfigComFirstWl_Type()
)
slWSSConfigComFirstWl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slWSSConfigComFirstWl.setStatus("current")
_SlWSSConfigComChCount_Type = Integer32
_SlWSSConfigComChCount_Object = MibTableColumn
slWSSConfigComChCount = _SlWSSConfigComChCount_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 8),
    _SlWSSConfigComChCount_Type()
)
slWSSConfigComChCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slWSSConfigComChCount.setStatus("current")
_SlWSSConfigPowerLevel_Type = Integer32
_SlWSSConfigPowerLevel_Object = MibTableColumn
slWSSConfigPowerLevel = _SlWSSConfigPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 9),
    _SlWSSConfigPowerLevel_Type()
)
slWSSConfigPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigPowerLevel.setStatus("current")
_SlWSSConfigAttenLevel_Type = Integer32
_SlWSSConfigAttenLevel_Object = MibTableColumn
slWSSConfigAttenLevel = _SlWSSConfigAttenLevel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 10),
    _SlWSSConfigAttenLevel_Type()
)
slWSSConfigAttenLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slWSSConfigAttenLevel.setStatus("current")
_SlROCHConfigTable_Object = MibTable
slROCHConfigTable = _SlROCHConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    slROCHConfigTable.setStatus("current")
_SlROCHConfigEntry_Object = MibTableRow
slROCHConfigEntry = _SlROCHConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1)
)
slROCHConfigEntry.setIndexNames(
    (0, "SL-ROADM-MIB", "slROCHConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slROCHConfigEntry.setStatus("current")
_SlROCHConfigLineIndex_Type = InterfaceIndex
_SlROCHConfigLineIndex_Object = MibTableColumn
slROCHConfigLineIndex = _SlROCHConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 1),
    _SlROCHConfigLineIndex_Type()
)
slROCHConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slROCHConfigLineIndex.setStatus("current")
_SlROCHConfigProvisioning_Type = ROCHProvisioningType
_SlROCHConfigProvisioning_Object = MibTableColumn
slROCHConfigProvisioning = _SlROCHConfigProvisioning_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 2),
    _SlROCHConfigProvisioning_Type()
)
slROCHConfigProvisioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slROCHConfigProvisioning.setStatus("current")
_SlROCHConfigInPowerLevel_Type = Integer32
_SlROCHConfigInPowerLevel_Object = MibTableColumn
slROCHConfigInPowerLevel = _SlROCHConfigInPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 3),
    _SlROCHConfigInPowerLevel_Type()
)
slROCHConfigInPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slROCHConfigInPowerLevel.setStatus("current")
_SlROCHConfigOutPowerLevel_Type = Integer32
_SlROCHConfigOutPowerLevel_Object = MibTableColumn
slROCHConfigOutPowerLevel = _SlROCHConfigOutPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 4),
    _SlROCHConfigOutPowerLevel_Type()
)
slROCHConfigOutPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slROCHConfigOutPowerLevel.setStatus("current")
_SlROCHConfigChannelDetect_Type = Integer32
_SlROCHConfigChannelDetect_Object = MibTableColumn
slROCHConfigChannelDetect = _SlROCHConfigChannelDetect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 5),
    _SlROCHConfigChannelDetect_Type()
)
slROCHConfigChannelDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slROCHConfigChannelDetect.setStatus("current")
_SlROCHConfigChPowerFailHighThresh_Type = Integer32
_SlROCHConfigChPowerFailHighThresh_Object = MibTableColumn
slROCHConfigChPowerFailHighThresh = _SlROCHConfigChPowerFailHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 6),
    _SlROCHConfigChPowerFailHighThresh_Type()
)
slROCHConfigChPowerFailHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slROCHConfigChPowerFailHighThresh.setStatus("current")
_SlROCHConfigChPowerFailLowThresh_Type = Integer32
_SlROCHConfigChPowerFailLowThresh_Object = MibTableColumn
slROCHConfigChPowerFailLowThresh = _SlROCHConfigChPowerFailLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 7),
    _SlROCHConfigChPowerFailLowThresh_Type()
)
slROCHConfigChPowerFailLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slROCHConfigChPowerFailLowThresh.setStatus("current")
_SlROCHConfigChPowerDegHighThresh_Type = Integer32
_SlROCHConfigChPowerDegHighThresh_Object = MibTableColumn
slROCHConfigChPowerDegHighThresh = _SlROCHConfigChPowerDegHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 8),
    _SlROCHConfigChPowerDegHighThresh_Type()
)
slROCHConfigChPowerDegHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slROCHConfigChPowerDegHighThresh.setStatus("current")
_SlROCHConfigChPowerDegLowThresh_Type = Integer32
_SlROCHConfigChPowerDegLowThresh_Object = MibTableColumn
slROCHConfigChPowerDegLowThresh = _SlROCHConfigChPowerDegLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 9),
    _SlROCHConfigChPowerDegLowThresh_Type()
)
slROCHConfigChPowerDegLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slROCHConfigChPowerDegLowThresh.setStatus("current")
_SlROCHConfigChPowerHystHighThresh_Type = Integer32
_SlROCHConfigChPowerHystHighThresh_Object = MibTableColumn
slROCHConfigChPowerHystHighThresh = _SlROCHConfigChPowerHystHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 10),
    _SlROCHConfigChPowerHystHighThresh_Type()
)
slROCHConfigChPowerHystHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slROCHConfigChPowerHystHighThresh.setStatus("current")
_SlROCHConfigChPowerHystLowThresh_Type = Integer32
_SlROCHConfigChPowerHystLowThresh_Object = MibTableColumn
slROCHConfigChPowerHystLowThresh = _SlROCHConfigChPowerHystLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 11),
    _SlROCHConfigChPowerHystLowThresh_Type()
)
slROCHConfigChPowerHystLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slROCHConfigChPowerHystLowThresh.setStatus("current")
_SlROADMPm_ObjectIdentity = ObjectIdentity
slROADMPm = _SlROADMPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 2)
)
_SlROADMTraps_ObjectIdentity = ObjectIdentity
slROADMTraps = _SlROADMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-ROADM-MIB",
    **{"ROCHProvisioningType": ROCHProvisioningType,
       "slROADM": slROADM,
       "slROADMConfig": slROADMConfig,
       "slWSSConfigTable": slWSSConfigTable,
       "slWSSConfigEntry": slWSSConfigEntry,
       "slWSSConfigLineIndex": slWSSConfigLineIndex,
       "slWSSConfigOperStatus": slWSSConfigOperStatus,
       "slWSSConfigSwitchTemp": slWSSConfigSwitchTemp,
       "slWSSConfigBoardTemp": slWSSConfigBoardTemp,
       "slWSSConfigCaseTemp": slWSSConfigCaseTemp,
       "slWSSConfigUptime": slWSSConfigUptime,
       "slWSSConfigComFirstWl": slWSSConfigComFirstWl,
       "slWSSConfigComChCount": slWSSConfigComChCount,
       "slWSSConfigPowerLevel": slWSSConfigPowerLevel,
       "slWSSConfigAttenLevel": slWSSConfigAttenLevel,
       "slROCHConfigTable": slROCHConfigTable,
       "slROCHConfigEntry": slROCHConfigEntry,
       "slROCHConfigLineIndex": slROCHConfigLineIndex,
       "slROCHConfigProvisioning": slROCHConfigProvisioning,
       "slROCHConfigInPowerLevel": slROCHConfigInPowerLevel,
       "slROCHConfigOutPowerLevel": slROCHConfigOutPowerLevel,
       "slROCHConfigChannelDetect": slROCHConfigChannelDetect,
       "slROCHConfigChPowerFailHighThresh": slROCHConfigChPowerFailHighThresh,
       "slROCHConfigChPowerFailLowThresh": slROCHConfigChPowerFailLowThresh,
       "slROCHConfigChPowerDegHighThresh": slROCHConfigChPowerDegHighThresh,
       "slROCHConfigChPowerDegLowThresh": slROCHConfigChPowerDegLowThresh,
       "slROCHConfigChPowerHystHighThresh": slROCHConfigChPowerHystHighThresh,
       "slROCHConfigChPowerHystLowThresh": slROCHConfigChPowerHystLowThresh,
       "slROADMPm": slROADMPm,
       "slROADMTraps": slROADMTraps}
)
