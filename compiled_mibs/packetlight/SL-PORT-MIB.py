# SNMP MIB module (SL-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:00 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LedColor(TextualConvention, Integer32):
    status = "current"
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
        *(("off", 1),
          ("red", 2),
          ("yellow", 3),
          ("green", 4))
    )



class LedMode(TextualConvention, Integer32):
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
        *(("stable", 1),
          ("fastBlinking", 2),
          ("slowBlinking", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SlPortConfig_ObjectIdentity = ObjectIdentity
slPortConfig = _SlPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1)
)
_SlPortConfigTable_Object = MibTable
slPortConfigTable = _SlPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1)
)
if mibBuilder.loadTexts:
    slPortConfigTable.setStatus("current")
_SlPortConfigEntry_Object = MibTableRow
slPortConfigEntry = _SlPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1)
)
slPortConfigEntry.setIndexNames(
    (0, "SL-PORT-MIB", "slPortConfigIndex"),
)
if mibBuilder.loadTexts:
    slPortConfigEntry.setStatus("current")
_SlPortConfigIndex_Type = Integer32
_SlPortConfigIndex_Object = MibTableColumn
slPortConfigIndex = _SlPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 1),
    _SlPortConfigIndex_Type()
)
slPortConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPortConfigIndex.setStatus("current")
_SlPortConfigLedColor_Type = LedColor
_SlPortConfigLedColor_Object = MibTableColumn
slPortConfigLedColor = _SlPortConfigLedColor_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 2),
    _SlPortConfigLedColor_Type()
)
slPortConfigLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPortConfigLedColor.setStatus("current")
_SlPortConfigLedMode_Type = LedMode
_SlPortConfigLedMode_Object = MibTableColumn
slPortConfigLedMode = _SlPortConfigLedMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 3),
    _SlPortConfigLedMode_Type()
)
slPortConfigLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPortConfigLedMode.setStatus("current")
_SlPortConfigChangeType_Type = Integer32
_SlPortConfigChangeType_Object = MibTableColumn
slPortConfigChangeType = _SlPortConfigChangeType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 4),
    _SlPortConfigChangeType_Type()
)
slPortConfigChangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slPortConfigChangeType.setStatus("current")
_SlPortConfigAlarmMask_Type = TruthValue
_SlPortConfigAlarmMask_Object = MibTableColumn
slPortConfigAlarmMask = _SlPortConfigAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 5),
    _SlPortConfigAlarmMask_Type()
)
slPortConfigAlarmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slPortConfigAlarmMask.setStatus("current")
_SlPortConfigLabel_Type = DisplayString
_SlPortConfigLabel_Object = MibTableColumn
slPortConfigLabel = _SlPortConfigLabel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 6),
    _SlPortConfigLabel_Type()
)
slPortConfigLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPortConfigLabel.setStatus("current")
_SlPortConfigLastChange_Type = TimeTicks
_SlPortConfigLastChange_Object = MibScalar
slPortConfigLastChange = _SlPortConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 2),
    _SlPortConfigLastChange_Type()
)
slPortConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPortConfigLastChange.setStatus("current")
_SlPortNotification_ObjectIdentity = ObjectIdentity
slPortNotification = _SlPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2)
)

# Managed Objects groups


# Notification objects

slPortConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 1)
)
slPortConfigChanged.setObjects(
      *(("SL-PORT-MIB", "slPortConfigIndex"),
        ("SL-PORT-MIB", "slPortConfigLedColor"),
        ("SL-PORT-MIB", "slPortConfigLedMode"),
        ("SL-PORT-MIB", "slPortConfigChangeType"),
        ("SL-PORT-MIB", "slPortConfigAlarmMask"),
        ("SL-PORT-MIB", "slPortConfigLabel"))
)
if mibBuilder.loadTexts:
    slPortConfigChanged.setStatus(
        "current"
    )

slPortConfigChangedType = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 2)
)
slPortConfigChangedType.setObjects(
      *(("SL-PORT-MIB", "slPortConfigIndex"),
        ("SL-PORT-MIB", "slPortConfigChangeType"))
)
if mibBuilder.loadTexts:
    slPortConfigChangedType.setStatus(
        "current"
    )

slPortConfigChangedMask = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 3)
)
slPortConfigChangedMask.setObjects(
      *(("SL-PORT-MIB", "slPortConfigIndex"),
        ("SL-PORT-MIB", "slPortConfigAlarmMask"))
)
if mibBuilder.loadTexts:
    slPortConfigChangedMask.setStatus(
        "current"
    )

slPortConfigChangedLabel = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 4)
)
slPortConfigChangedLabel.setObjects(
      *(("SL-PORT-MIB", "slPortConfigIndex"),
        ("SL-PORT-MIB", "slPortConfigLabel"))
)
if mibBuilder.loadTexts:
    slPortConfigChangedLabel.setStatus(
        "current"
    )

slPortConfigChangedApsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 5)
)
slPortConfigChangedApsEnabled.setObjects(
    ("SL-PORT-MIB", "slPortConfigIndex")
)
if mibBuilder.loadTexts:
    slPortConfigChangedApsEnabled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-PORT-MIB",
    **{"LedColor": LedColor,
       "LedMode": LedMode,
       "slPort": slPort,
       "slPortConfig": slPortConfig,
       "slPortConfigTable": slPortConfigTable,
       "slPortConfigEntry": slPortConfigEntry,
       "slPortConfigIndex": slPortConfigIndex,
       "slPortConfigLedColor": slPortConfigLedColor,
       "slPortConfigLedMode": slPortConfigLedMode,
       "slPortConfigChangeType": slPortConfigChangeType,
       "slPortConfigAlarmMask": slPortConfigAlarmMask,
       "slPortConfigLabel": slPortConfigLabel,
       "slPortConfigLastChange": slPortConfigLastChange,
       "slPortNotification": slPortNotification,
       "slPortConfigChanged": slPortConfigChanged,
       "slPortConfigChangedType": slPortConfigChangedType,
       "slPortConfigChangedMask": slPortConfigChangedMask,
       "slPortConfigChangedLabel": slPortConfigChangedLabel,
       "slPortConfigChangedApsEnabled": slPortConfigChangedApsEnabled}
)
