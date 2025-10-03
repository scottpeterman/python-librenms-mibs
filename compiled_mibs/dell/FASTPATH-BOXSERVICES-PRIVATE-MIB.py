# SNMP MIB module (FASTPATH-BOXSERVICES-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\FASTPATH-BOXSERVICES-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:09 2025
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

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

fastPathBoxServices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43)
)
if mibBuilder.loadTexts:
    fastPathBoxServices.setRevisions(
        ("2008-02-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FastPathBoxServicesTraps_ObjectIdentity = ObjectIdentity
fastPathBoxServicesTraps = _FastPathBoxServicesTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0)
)
_BoxServicesGroup_ObjectIdentity = ObjectIdentity
boxServicesGroup = _BoxServicesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1)
)


class _BoxServicesNormalTempRangeMin_Type(Integer32):
    """Custom type boxServicesNormalTempRangeMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_BoxServicesNormalTempRangeMin_Type.__name__ = "Integer32"
_BoxServicesNormalTempRangeMin_Object = MibScalar
boxServicesNormalTempRangeMin = _BoxServicesNormalTempRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 1),
    _BoxServicesNormalTempRangeMin_Type()
)
boxServicesNormalTempRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesNormalTempRangeMin.setStatus("current")


class _BoxServicesNormalTempRangeMax_Type(Integer32):
    """Custom type boxServicesNormalTempRangeMax based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_BoxServicesNormalTempRangeMax_Type.__name__ = "Integer32"
_BoxServicesNormalTempRangeMax_Object = MibScalar
boxServicesNormalTempRangeMax = _BoxServicesNormalTempRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 2),
    _BoxServicesNormalTempRangeMax_Type()
)
boxServicesNormalTempRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesNormalTempRangeMax.setStatus("current")


class _BoxServicesTemperatureTrapEnable_Type(Integer32):
    """Custom type boxServicesTemperatureTrapEnable based on Integer32"""
    defaultValue = 1

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


_BoxServicesTemperatureTrapEnable_Type.__name__ = "Integer32"
_BoxServicesTemperatureTrapEnable_Object = MibScalar
boxServicesTemperatureTrapEnable = _BoxServicesTemperatureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 3),
    _BoxServicesTemperatureTrapEnable_Type()
)
boxServicesTemperatureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesTemperatureTrapEnable.setStatus("current")


class _BoxServicesPSMStateTrapEnable_Type(Integer32):
    """Custom type boxServicesPSMStateTrapEnable based on Integer32"""
    defaultValue = 1

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


_BoxServicesPSMStateTrapEnable_Type.__name__ = "Integer32"
_BoxServicesPSMStateTrapEnable_Object = MibScalar
boxServicesPSMStateTrapEnable = _BoxServicesPSMStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 4),
    _BoxServicesPSMStateTrapEnable_Type()
)
boxServicesPSMStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesPSMStateTrapEnable.setStatus("current")


class _BoxServicesFanStateTrapEnable_Type(Integer32):
    """Custom type boxServicesFanStateTrapEnable based on Integer32"""
    defaultValue = 1

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


_BoxServicesFanStateTrapEnable_Type.__name__ = "Integer32"
_BoxServicesFanStateTrapEnable_Object = MibScalar
boxServicesFanStateTrapEnable = _BoxServicesFanStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 5),
    _BoxServicesFanStateTrapEnable_Type()
)
boxServicesFanStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesFanStateTrapEnable.setStatus("current")
_BoxServicesFansTable_Object = MibTable
boxServicesFansTable = _BoxServicesFansTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6)
)
if mibBuilder.loadTexts:
    boxServicesFansTable.setStatus("current")
_BoxServicesFansEntry_Object = MibTableRow
boxServicesFansEntry = _BoxServicesFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1)
)
boxServicesFansEntry.setIndexNames(
    (0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"),
)
if mibBuilder.loadTexts:
    boxServicesFansEntry.setStatus("current")


class _BoxServicesFansIndex_Type(Integer32):
    """Custom type boxServicesFansIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoxServicesFansIndex_Type.__name__ = "Integer32"
_BoxServicesFansIndex_Object = MibTableColumn
boxServicesFansIndex = _BoxServicesFansIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 1),
    _BoxServicesFansIndex_Type()
)
boxServicesFansIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFansIndex.setStatus("current")


class _BoxServicesFanItemType_Type(Integer32):
    """Custom type boxServicesFanItemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("removable", 2))
    )


_BoxServicesFanItemType_Type.__name__ = "Integer32"
_BoxServicesFanItemType_Object = MibTableColumn
boxServicesFanItemType = _BoxServicesFanItemType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 2),
    _BoxServicesFanItemType_Type()
)
boxServicesFanItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanItemType.setStatus("current")


class _BoxServicesFanItemState_Type(Integer32):
    """Custom type boxServicesFanItemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("operational", 2),
          ("failed", 3))
    )


_BoxServicesFanItemState_Type.__name__ = "Integer32"
_BoxServicesFanItemState_Object = MibTableColumn
boxServicesFanItemState = _BoxServicesFanItemState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 3),
    _BoxServicesFanItemState_Type()
)
boxServicesFanItemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanItemState.setStatus("current")
_BoxServicesFanSpeed_Type = Integer32
_BoxServicesFanSpeed_Object = MibTableColumn
boxServicesFanSpeed = _BoxServicesFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 4),
    _BoxServicesFanSpeed_Type()
)
boxServicesFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanSpeed.setStatus("current")
_BoxServicesFanDutyLevel_Type = Integer32
_BoxServicesFanDutyLevel_Object = MibTableColumn
boxServicesFanDutyLevel = _BoxServicesFanDutyLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 5),
    _BoxServicesFanDutyLevel_Type()
)
boxServicesFanDutyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanDutyLevel.setStatus("current")
_BoxServicesPowSuppliesTable_Object = MibTable
boxServicesPowSuppliesTable = _BoxServicesPowSuppliesTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7)
)
if mibBuilder.loadTexts:
    boxServicesPowSuppliesTable.setStatus("current")
_BoxServicesPowSuppliesEntry_Object = MibTableRow
boxServicesPowSuppliesEntry = _BoxServicesPowSuppliesEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1)
)
boxServicesPowSuppliesEntry.setIndexNames(
    (0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"),
)
if mibBuilder.loadTexts:
    boxServicesPowSuppliesEntry.setStatus("current")


class _BoxServicesPowSupplyIndex_Type(Integer32):
    """Custom type boxServicesPowSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoxServicesPowSupplyIndex_Type.__name__ = "Integer32"
_BoxServicesPowSupplyIndex_Object = MibTableColumn
boxServicesPowSupplyIndex = _BoxServicesPowSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 1),
    _BoxServicesPowSupplyIndex_Type()
)
boxServicesPowSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesPowSupplyIndex.setStatus("current")


class _BoxServicesPowSupplyItemType_Type(Integer32):
    """Custom type boxServicesPowSupplyItemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("removable", 2))
    )


_BoxServicesPowSupplyItemType_Type.__name__ = "Integer32"
_BoxServicesPowSupplyItemType_Object = MibTableColumn
boxServicesPowSupplyItemType = _BoxServicesPowSupplyItemType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 2),
    _BoxServicesPowSupplyItemType_Type()
)
boxServicesPowSupplyItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesPowSupplyItemType.setStatus("current")


class _BoxServicesPowSupplyItemState_Type(Integer32):
    """Custom type boxServicesPowSupplyItemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("operational", 2),
          ("failed", 3))
    )


_BoxServicesPowSupplyItemState_Type.__name__ = "Integer32"
_BoxServicesPowSupplyItemState_Object = MibTableColumn
boxServicesPowSupplyItemState = _BoxServicesPowSupplyItemState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 3),
    _BoxServicesPowSupplyItemState_Type()
)
boxServicesPowSupplyItemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesPowSupplyItemState.setStatus("current")
_BoxServicesTempSensorsTable_Object = MibTable
boxServicesTempSensorsTable = _BoxServicesTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8)
)
if mibBuilder.loadTexts:
    boxServicesTempSensorsTable.setStatus("current")
_BoxServicesTempSensorsEntry_Object = MibTableRow
boxServicesTempSensorsEntry = _BoxServicesTempSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1)
)
boxServicesTempSensorsEntry.setIndexNames(
    (0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"),
)
if mibBuilder.loadTexts:
    boxServicesTempSensorsEntry.setStatus("current")


class _BoxServicesTempSensorIndex_Type(Integer32):
    """Custom type boxServicesTempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoxServicesTempSensorIndex_Type.__name__ = "Integer32"
_BoxServicesTempSensorIndex_Object = MibTableColumn
boxServicesTempSensorIndex = _BoxServicesTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 1),
    _BoxServicesTempSensorIndex_Type()
)
boxServicesTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorIndex.setStatus("current")


class _BoxServicesTempSensorType_Type(Integer32):
    """Custom type boxServicesTempSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("removable", 2))
    )


_BoxServicesTempSensorType_Type.__name__ = "Integer32"
_BoxServicesTempSensorType_Object = MibTableColumn
boxServicesTempSensorType = _BoxServicesTempSensorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 2),
    _BoxServicesTempSensorType_Type()
)
boxServicesTempSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorType.setStatus("current")


class _BoxServicesTempSensorState_Type(Integer32):
    """Custom type boxServicesTempSensorState based on Integer32"""
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("shutdown", 4),
          ("notpresent", 5),
          ("notoperational", 6))
    )


_BoxServicesTempSensorState_Type.__name__ = "Integer32"
_BoxServicesTempSensorState_Object = MibTableColumn
boxServicesTempSensorState = _BoxServicesTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 3),
    _BoxServicesTempSensorState_Type()
)
boxServicesTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorState.setStatus("current")
_BoxServicesTempSensorTemperature_Type = Integer32
_BoxServicesTempSensorTemperature_Object = MibTableColumn
boxServicesTempSensorTemperature = _BoxServicesTempSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 4),
    _BoxServicesTempSensorTemperature_Type()
)
boxServicesTempSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorTemperature.setStatus("current")
_BoxServicesNotificationsGroup_ObjectIdentity = ObjectIdentity
boxServicesNotificationsGroup = _BoxServicesNotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2)
)


class _BoxsItemStateChangeEvent_Type(Integer32):
    """Custom type boxsItemStateChangeEvent based on Integer32"""
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
        *(("insertion", 1),
          ("removal", 2),
          ("becomeoperational", 3),
          ("failure", 4))
    )


_BoxsItemStateChangeEvent_Type.__name__ = "Integer32"
_BoxsItemStateChangeEvent_Object = MibScalar
boxsItemStateChangeEvent = _BoxsItemStateChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 1),
    _BoxsItemStateChangeEvent_Type()
)
boxsItemStateChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxsItemStateChangeEvent.setStatus("current")


class _BoxsTemperatureChangeEvent_Type(Integer32):
    """Custom type boxsTemperatureChangeEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abovethreshold", 1),
          ("belowthreshold", 2),
          ("withinnormalrange", 3))
    )


_BoxsTemperatureChangeEvent_Type.__name__ = "Integer32"
_BoxsTemperatureChangeEvent_Object = MibScalar
boxsTemperatureChangeEvent = _BoxsTemperatureChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 2),
    _BoxsTemperatureChangeEvent_Type()
)
boxsTemperatureChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxsTemperatureChangeEvent.setStatus("current")

# Managed Objects groups


# Notification objects

boxsFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 1)
)
boxsFanStateChange.setObjects(
      *(("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"),
        ("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
)
if mibBuilder.loadTexts:
    boxsFanStateChange.setStatus(
        "current"
    )

boxsPowSupplyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 2)
)
boxsPowSupplyStateChange.setObjects(
      *(("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"),
        ("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
)
if mibBuilder.loadTexts:
    boxsPowSupplyStateChange.setStatus(
        "current"
    )

boxsTemperatureChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 3)
)
boxsTemperatureChange.setObjects(
      *(("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"),
        ("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureChangeEvent"))
)
if mibBuilder.loadTexts:
    boxsTemperatureChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-BOXSERVICES-PRIVATE-MIB",
    **{"fastPathBoxServices": fastPathBoxServices,
       "fastPathBoxServicesTraps": fastPathBoxServicesTraps,
       "boxsFanStateChange": boxsFanStateChange,
       "boxsPowSupplyStateChange": boxsPowSupplyStateChange,
       "boxsTemperatureChange": boxsTemperatureChange,
       "boxServicesGroup": boxServicesGroup,
       "boxServicesNormalTempRangeMin": boxServicesNormalTempRangeMin,
       "boxServicesNormalTempRangeMax": boxServicesNormalTempRangeMax,
       "boxServicesTemperatureTrapEnable": boxServicesTemperatureTrapEnable,
       "boxServicesPSMStateTrapEnable": boxServicesPSMStateTrapEnable,
       "boxServicesFanStateTrapEnable": boxServicesFanStateTrapEnable,
       "boxServicesFansTable": boxServicesFansTable,
       "boxServicesFansEntry": boxServicesFansEntry,
       "boxServicesFansIndex": boxServicesFansIndex,
       "boxServicesFanItemType": boxServicesFanItemType,
       "boxServicesFanItemState": boxServicesFanItemState,
       "boxServicesFanSpeed": boxServicesFanSpeed,
       "boxServicesFanDutyLevel": boxServicesFanDutyLevel,
       "boxServicesPowSuppliesTable": boxServicesPowSuppliesTable,
       "boxServicesPowSuppliesEntry": boxServicesPowSuppliesEntry,
       "boxServicesPowSupplyIndex": boxServicesPowSupplyIndex,
       "boxServicesPowSupplyItemType": boxServicesPowSupplyItemType,
       "boxServicesPowSupplyItemState": boxServicesPowSupplyItemState,
       "boxServicesTempSensorsTable": boxServicesTempSensorsTable,
       "boxServicesTempSensorsEntry": boxServicesTempSensorsEntry,
       "boxServicesTempSensorIndex": boxServicesTempSensorIndex,
       "boxServicesTempSensorType": boxServicesTempSensorType,
       "boxServicesTempSensorState": boxServicesTempSensorState,
       "boxServicesTempSensorTemperature": boxServicesTempSensorTemperature,
       "boxServicesNotificationsGroup": boxServicesNotificationsGroup,
       "boxsItemStateChangeEvent": boxsItemStateChangeEvent,
       "boxsTemperatureChangeEvent": boxsTemperatureChangeEvent}
)
