# SNMP MIB module (RAISECOM-POWERMONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\RAISECOM-POWERMONITOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:02 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

raisecomPowerMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomPowerMonitorNotification_ObjectIdentity = ObjectIdentity
raisecomPowerMonitorNotification = _RaisecomPowerMonitorNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 1)
)
_RaisecomPowerMonitorMibObjects_ObjectIdentity = ObjectIdentity
raisecomPowerMonitorMibObjects = _RaisecomPowerMonitorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2)
)
_RaisecomPowerMonitorStateTable_Object = MibTable
raisecomPowerMonitorStateTable = _RaisecomPowerMonitorStateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomPowerMonitorStateTable.setStatus("current")
_RaisecomPowerMonitorStateEntry_Object = MibTableRow
raisecomPowerMonitorStateEntry = _RaisecomPowerMonitorStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1, 1)
)
raisecomPowerMonitorStateEntry.setIndexNames(
    (0, "RAISECOM-POWERMONITOR-MIB", "raisecomPowerIndex"),
)
if mibBuilder.loadTexts:
    raisecomPowerMonitorStateEntry.setStatus("current")
_RaisecomPowerIndex_Type = Unsigned32
_RaisecomPowerIndex_Object = MibTableColumn
raisecomPowerIndex = _RaisecomPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1, 1, 1),
    _RaisecomPowerIndex_Type()
)
raisecomPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomPowerIndex.setStatus("current")
_RaisecomPowerSerialNumber_Type = OctetString
_RaisecomPowerSerialNumber_Object = MibTableColumn
raisecomPowerSerialNumber = _RaisecomPowerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1, 1, 2),
    _RaisecomPowerSerialNumber_Type()
)
raisecomPowerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPowerSerialNumber.setStatus("current")


class _RaisecomPowerType_Type(Integer32):
    """Custom type raisecomPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_RaisecomPowerType_Type.__name__ = "Integer32"
_RaisecomPowerType_Object = MibTableColumn
raisecomPowerType = _RaisecomPowerType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1, 1, 3),
    _RaisecomPowerType_Type()
)
raisecomPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPowerType.setStatus("current")
_RaisecomPowerVoltReference_Type = Integer32
_RaisecomPowerVoltReference_Object = MibTableColumn
raisecomPowerVoltReference = _RaisecomPowerVoltReference_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1, 1, 4),
    _RaisecomPowerVoltReference_Type()
)
raisecomPowerVoltReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPowerVoltReference.setStatus("current")
_RaisecomPowerVoltValue_Type = Integer32
_RaisecomPowerVoltValue_Object = MibTableColumn
raisecomPowerVoltValue = _RaisecomPowerVoltValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1, 1, 5),
    _RaisecomPowerVoltValue_Type()
)
raisecomPowerVoltValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPowerVoltValue.setStatus("current")


class _RaisecomPowerStatus_Type(Integer32):
    """Custom type raisecomPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2),
          ("power-on", 3))
    )


_RaisecomPowerStatus_Type.__name__ = "Integer32"
_RaisecomPowerStatus_Object = MibTableColumn
raisecomPowerStatus = _RaisecomPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 2, 1, 1, 6),
    _RaisecomPowerStatus_Type()
)
raisecomPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPowerStatus.setStatus("current")

# Managed Objects groups


# Notification objects

raisecomPowerVoltNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 1, 1)
)
raisecomPowerVoltNormal.setObjects(
      *(("RAISECOM-POWERMONITOR-MIB", "raisecomPowerIndex"),
        ("RAISECOM-POWERMONITOR-MIB", "raisecomPowerVoltReference"),
        ("RAISECOM-POWERMONITOR-MIB", "raisecomPowerVoltValue"))
)
if mibBuilder.loadTexts:
    raisecomPowerVoltNormal.setStatus(
        "current"
    )

raisecomPowerVoltAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 1, 2)
)
raisecomPowerVoltAbnormal.setObjects(
      *(("RAISECOM-POWERMONITOR-MIB", "raisecomPowerIndex"),
        ("RAISECOM-POWERMONITOR-MIB", "raisecomPowerVoltReference"),
        ("RAISECOM-POWERMONITOR-MIB", "raisecomPowerVoltValue"))
)
if mibBuilder.loadTexts:
    raisecomPowerVoltAbnormal.setStatus(
        "current"
    )

raisecomPowerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 1, 3)
)
raisecomPowerStatusTrap.setObjects(
      *(("RAISECOM-POWERMONITOR-MIB", "raisecomPowerIndex"),
        ("RAISECOM-POWERMONITOR-MIB", "raisecomPowerStatus"))
)
if mibBuilder.loadTexts:
    raisecomPowerStatusTrap.setStatus(
        "current"
    )

raisecomDyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 24, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomDyingGaspTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-POWERMONITOR-MIB",
    **{"raisecomPowerMonitor": raisecomPowerMonitor,
       "raisecomPowerMonitorNotification": raisecomPowerMonitorNotification,
       "raisecomPowerVoltNormal": raisecomPowerVoltNormal,
       "raisecomPowerVoltAbnormal": raisecomPowerVoltAbnormal,
       "raisecomPowerStatusTrap": raisecomPowerStatusTrap,
       "raisecomDyingGaspTrap": raisecomDyingGaspTrap,
       "raisecomPowerMonitorMibObjects": raisecomPowerMonitorMibObjects,
       "raisecomPowerMonitorStateTable": raisecomPowerMonitorStateTable,
       "raisecomPowerMonitorStateEntry": raisecomPowerMonitorStateEntry,
       "raisecomPowerIndex": raisecomPowerIndex,
       "raisecomPowerSerialNumber": raisecomPowerSerialNumber,
       "raisecomPowerType": raisecomPowerType,
       "raisecomPowerVoltReference": raisecomPowerVoltReference,
       "raisecomPowerVoltValue": raisecomPowerVoltValue,
       "raisecomPowerStatus": raisecomPowerStatus}
)
