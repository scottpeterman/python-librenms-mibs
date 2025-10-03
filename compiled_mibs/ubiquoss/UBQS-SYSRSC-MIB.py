# SNMP MIB module (UBQS-SYSRSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-SYSRSC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:34 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(ubiSystemMIB,) = mibBuilder.importSymbols(
    "UBQS-SYSTEM-MIB",
    "ubiSystemMIB")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiSystemMIBObjects_ObjectIdentity = ObjectIdentity
ubiSystemMIBObjects = _UbiSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1)
)
_UbiSysRscCpu_ObjectIdentity = ObjectIdentity
ubiSysRscCpu = _UbiSysRscCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 3)
)
_UbiCpuFiveSec_Type = Counter32
_UbiCpuFiveSec_Object = MibScalar
ubiCpuFiveSec = _UbiCpuFiveSec_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 3, 1),
    _UbiCpuFiveSec_Type()
)
ubiCpuFiveSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiCpuFiveSec.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiCpuFiveSec.setUnits("%")
_UbiCpuOneMin_Type = Counter32
_UbiCpuOneMin_Object = MibScalar
ubiCpuOneMin = _UbiCpuOneMin_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 3, 2),
    _UbiCpuOneMin_Type()
)
ubiCpuOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiCpuOneMin.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiCpuOneMin.setUnits("%")
_UbiCpuFiveMin_Type = Counter32
_UbiCpuFiveMin_Object = MibScalar
ubiCpuFiveMin = _UbiCpuFiveMin_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 3, 3),
    _UbiCpuFiveMin_Type()
)
ubiCpuFiveMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiCpuFiveMin.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiCpuFiveMin.setUnits("%")
_UbiCpuRisingThreshold_Type = Counter32
_UbiCpuRisingThreshold_Object = MibScalar
ubiCpuRisingThreshold = _UbiCpuRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 3, 4),
    _UbiCpuRisingThreshold_Type()
)
ubiCpuRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiCpuRisingThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiCpuRisingThreshold.setUnits("%")
_UbiCpuFallingThreshold_Type = Counter32
_UbiCpuFallingThreshold_Object = MibScalar
ubiCpuFallingThreshold = _UbiCpuFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 3, 5),
    _UbiCpuFallingThreshold_Type()
)
ubiCpuFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiCpuFallingThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiCpuFallingThreshold.setUnits("%")


class _UbiCpuLoadTimePeriod_Type(Integer32):
    """Custom type ubiCpuLoadTimePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiveSec", 1),
          ("oneMin", 2),
          ("fiveMin", 3))
    )


_UbiCpuLoadTimePeriod_Type.__name__ = "Integer32"
_UbiCpuLoadTimePeriod_Object = MibScalar
ubiCpuLoadTimePeriod = _UbiCpuLoadTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 3, 6),
    _UbiCpuLoadTimePeriod_Type()
)
ubiCpuLoadTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiCpuLoadTimePeriod.setStatus("mandatory")
_UbiSysRscMemory_ObjectIdentity = ObjectIdentity
ubiSysRscMemory = _UbiSysRscMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 4)
)
_UbiMemoryAlloc_Type = Counter32
_UbiMemoryAlloc_Object = MibScalar
ubiMemoryAlloc = _UbiMemoryAlloc_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 4, 1),
    _UbiMemoryAlloc_Type()
)
ubiMemoryAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiMemoryAlloc.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiMemoryAlloc.setUnits("kbyte")
_UbiMemoryFree_Type = Counter32
_UbiMemoryFree_Object = MibScalar
ubiMemoryFree = _UbiMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 4, 2),
    _UbiMemoryFree_Type()
)
ubiMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiMemoryFree.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiMemoryFree.setUnits("kbyte")
_UbiMemoryTotal_Type = Counter32
_UbiMemoryTotal_Object = MibScalar
ubiMemoryTotal = _UbiMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 4, 3),
    _UbiMemoryTotal_Type()
)
ubiMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiMemoryTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiMemoryTotal.setUnits("kbyte")
_UbiMemoryFreePercentage_Type = Counter32
_UbiMemoryFreePercentage_Object = MibScalar
ubiMemoryFreePercentage = _UbiMemoryFreePercentage_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 4, 4),
    _UbiMemoryFreePercentage_Type()
)
ubiMemoryFreePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiMemoryFreePercentage.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiMemoryFreePercentage.setUnits("%")
_UbiMemoryThreshold_Type = Counter32
_UbiMemoryThreshold_Object = MibScalar
ubiMemoryThreshold = _UbiMemoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 4, 5),
    _UbiMemoryThreshold_Type()
)
ubiMemoryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiMemoryThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    ubiMemoryThreshold.setUnits("%")
_UbiSysRscNotificationEnables_ObjectIdentity = ObjectIdentity
ubiSysRscNotificationEnables = _UbiSysRscNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 5)
)


class _UbiSysRscEnableCpuNotification_Type(TruthValue):
    """Custom type ubiSysRscEnableCpuNotification based on TruthValue"""
    defaultValue = 2


_UbiSysRscEnableCpuNotification_Type.__name__ = "TruthValue"
_UbiSysRscEnableCpuNotification_Object = MibScalar
ubiSysRscEnableCpuNotification = _UbiSysRscEnableCpuNotification_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 5, 1),
    _UbiSysRscEnableCpuNotification_Type()
)
ubiSysRscEnableCpuNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysRscEnableCpuNotification.setStatus("current")


class _UbiSysRscEnableMemoryNotification_Type(TruthValue):
    """Custom type ubiSysRscEnableMemoryNotification based on TruthValue"""
    defaultValue = 2


_UbiSysRscEnableMemoryNotification_Type.__name__ = "TruthValue"
_UbiSysRscEnableMemoryNotification_Object = MibScalar
ubiSysRscEnableMemoryNotification = _UbiSysRscEnableMemoryNotification_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 5, 2),
    _UbiSysRscEnableMemoryNotification_Type()
)
ubiSysRscEnableMemoryNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysRscEnableMemoryNotification.setStatus("current")
_UbiSystemMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiSystemMIBNotificationPrefix = _UbiSystemMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2)
)
_UbiSystemMIBNotifications_ObjectIdentity = ObjectIdentity
ubiSystemMIBNotifications = _UbiSystemMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 0)
)
_UbiSysRscMIBNotificationObjects_ObjectIdentity = ObjectIdentity
ubiSysRscMIBNotificationObjects = _UbiSysRscMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 1)
)
_UbiCpuAlarmValue_Type = Counter32
_UbiCpuAlarmValue_Object = MibScalar
ubiCpuAlarmValue = _UbiCpuAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 1, 1),
    _UbiCpuAlarmValue_Type()
)
ubiCpuAlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubiCpuAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    ubiCpuAlarmValue.setUnits("%")


class _UbiCpuAlarmState_Type(Integer32):
    """Custom type ubiCpuAlarmState based on Integer32"""
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
          ("high", 1),
          ("low", 2))
    )


_UbiCpuAlarmState_Type.__name__ = "Integer32"
_UbiCpuAlarmState_Object = MibScalar
ubiCpuAlarmState = _UbiCpuAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 1, 2),
    _UbiCpuAlarmState_Type()
)
ubiCpuAlarmState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubiCpuAlarmState.setStatus("current")

# Managed Objects groups


# Notification objects

ubiSysRscCpuRisingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 0, 1)
)
ubiSysRscCpuRisingNotification.setObjects(
      *(("UBQS-SYSRSC-MIB", "ubiCpuLoadTimePeriod"),
        ("UBQS-SYSRSC-MIB", "ubiCpuAlarmValue"),
        ("UBQS-SYSRSC-MIB", "ubiCpuRisingThreshold"),
        ("UBQS-SYSRSC-MIB", "ubiCpuAlarmState"))
)
if mibBuilder.loadTexts:
    ubiSysRscCpuRisingNotification.setStatus(
        "current"
    )

ubiSysRscCpuFallingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 0, 2)
)
ubiSysRscCpuFallingNotification.setObjects(
      *(("UBQS-SYSRSC-MIB", "ubiCpuLoadTimePeriod"),
        ("UBQS-SYSRSC-MIB", "ubiCpuAlarmValue"),
        ("UBQS-SYSRSC-MIB", "ubiCpuFallingThreshold"),
        ("UBQS-SYSRSC-MIB", "ubiCpuAlarmState"))
)
if mibBuilder.loadTexts:
    ubiSysRscCpuFallingNotification.setStatus(
        "current"
    )

ubiSysRscMemoryRisingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 0, 3)
)
ubiSysRscMemoryRisingNotification.setObjects(
      *(("UBQS-SYSRSC-MIB", "ubiMemoryFreePercentage"),
        ("UBQS-SYSRSC-MIB", "ubiMemoryThreshold"))
)
if mibBuilder.loadTexts:
    ubiSysRscMemoryRisingNotification.setStatus(
        "current"
    )

ubiSysRscMemoryFallingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2, 0, 4)
)
ubiSysRscMemoryFallingNotification.setObjects(
      *(("UBQS-SYSRSC-MIB", "ubiMemoryFreePercentage"),
        ("UBQS-SYSRSC-MIB", "ubiMemoryThreshold"))
)
if mibBuilder.loadTexts:
    ubiSysRscMemoryFallingNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-SYSRSC-MIB",
    **{"ubiSystemMIBObjects": ubiSystemMIBObjects,
       "ubiSysRscCpu": ubiSysRscCpu,
       "ubiCpuFiveSec": ubiCpuFiveSec,
       "ubiCpuOneMin": ubiCpuOneMin,
       "ubiCpuFiveMin": ubiCpuFiveMin,
       "ubiCpuRisingThreshold": ubiCpuRisingThreshold,
       "ubiCpuFallingThreshold": ubiCpuFallingThreshold,
       "ubiCpuLoadTimePeriod": ubiCpuLoadTimePeriod,
       "ubiSysRscMemory": ubiSysRscMemory,
       "ubiMemoryAlloc": ubiMemoryAlloc,
       "ubiMemoryFree": ubiMemoryFree,
       "ubiMemoryTotal": ubiMemoryTotal,
       "ubiMemoryFreePercentage": ubiMemoryFreePercentage,
       "ubiMemoryThreshold": ubiMemoryThreshold,
       "ubiSysRscNotificationEnables": ubiSysRscNotificationEnables,
       "ubiSysRscEnableCpuNotification": ubiSysRscEnableCpuNotification,
       "ubiSysRscEnableMemoryNotification": ubiSysRscEnableMemoryNotification,
       "ubiSystemMIBNotificationPrefix": ubiSystemMIBNotificationPrefix,
       "ubiSystemMIBNotifications": ubiSystemMIBNotifications,
       "ubiSysRscCpuRisingNotification": ubiSysRscCpuRisingNotification,
       "ubiSysRscCpuFallingNotification": ubiSysRscCpuFallingNotification,
       "ubiSysRscMemoryRisingNotification": ubiSysRscMemoryRisingNotification,
       "ubiSysRscMemoryFallingNotification": ubiSysRscMemoryFallingNotification,
       "ubiSysRscMIBNotificationObjects": ubiSysRscMIBNotificationObjects,
       "ubiCpuAlarmValue": ubiCpuAlarmValue,
       "ubiCpuAlarmState": ubiCpuAlarmState}
)
