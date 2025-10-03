# SNMP MIB module (SL-ALS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-ALS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:43 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slAlsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlAlsConfig_ObjectIdentity = ObjectIdentity
slAlsConfig = _SlAlsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1)
)
_SlAlsConfigTable_Object = MibTable
slAlsConfigTable = _SlAlsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    slAlsConfigTable.setStatus("current")
_SlAlsConfigEntry_Object = MibTableRow
slAlsConfigEntry = _SlAlsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1)
)
slAlsConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slAlsConfigEntry.setStatus("current")


class _SlAlsMode_Type(Integer32):
    """Custom type slAlsMode based on Integer32"""
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


_SlAlsMode_Type.__name__ = "Integer32"
_SlAlsMode_Object = MibTableColumn
slAlsMode = _SlAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 1),
    _SlAlsMode_Type()
)
slAlsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsMode.setStatus("current")


class _SlAlsLosDeclareTime_Type(Integer32):
    """Custom type slAlsLosDeclareTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms500", 1),
          ("ms550", 2),
          ("ms600", 3))
    )


_SlAlsLosDeclareTime_Type.__name__ = "Integer32"
_SlAlsLosDeclareTime_Object = MibTableColumn
slAlsLosDeclareTime = _SlAlsLosDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 2),
    _SlAlsLosDeclareTime_Type()
)
slAlsLosDeclareTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsLosDeclareTime.setStatus("current")


class _SlAlsTestPulseTime_Type(Integer32):
    """Custom type slAlsTestPulseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s80", 1),
          ("s90", 2),
          ("s100", 3))
    )


_SlAlsTestPulseTime_Type.__name__ = "Integer32"
_SlAlsTestPulseTime_Object = MibTableColumn
slAlsTestPulseTime = _SlAlsTestPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 3),
    _SlAlsTestPulseTime_Type()
)
slAlsTestPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsTestPulseTime.setStatus("current")


class _SlAlsManualPulseTime_Type(Integer32):
    """Custom type slAlsManualPulseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1750", 1),
          ("ms2000", 2),
          ("ms2250", 3))
    )


_SlAlsManualPulseTime_Type.__name__ = "Integer32"
_SlAlsManualPulseTime_Object = MibTableColumn
slAlsManualPulseTime = _SlAlsManualPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 4),
    _SlAlsManualPulseTime_Type()
)
slAlsManualPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsManualPulseTime.setStatus("current")


class _SlAlsAutomaticPulseTime_Type(Integer32):
    """Custom type slAlsAutomaticPulseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1750", 1),
          ("ms2000", 2),
          ("ms2250", 3))
    )


_SlAlsAutomaticPulseTime_Type.__name__ = "Integer32"
_SlAlsAutomaticPulseTime_Object = MibTableColumn
slAlsAutomaticPulseTime = _SlAlsAutomaticPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 5),
    _SlAlsAutomaticPulseTime_Type()
)
slAlsAutomaticPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsAutomaticPulseTime.setStatus("current")


class _SlAlsAutomaticDelayTime_Type(Integer32):
    """Custom type slAlsAutomaticDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_SlAlsAutomaticDelayTime_Type.__name__ = "Integer32"
_SlAlsAutomaticDelayTime_Object = MibTableColumn
slAlsAutomaticDelayTime = _SlAlsAutomaticDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 6),
    _SlAlsAutomaticDelayTime_Type()
)
slAlsAutomaticDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsAutomaticDelayTime.setStatus("current")


class _SlAlsLaserTestActivate_Type(Integer32):
    """Custom type slAlsLaserTestActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_SlAlsLaserTestActivate_Type.__name__ = "Integer32"
_SlAlsLaserTestActivate_Object = MibTableColumn
slAlsLaserTestActivate = _SlAlsLaserTestActivate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 7),
    _SlAlsLaserTestActivate_Type()
)
slAlsLaserTestActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsLaserTestActivate.setStatus("current")


class _SlAlsLaserManualActivate_Type(Integer32):
    """Custom type slAlsLaserManualActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_SlAlsLaserManualActivate_Type.__name__ = "Integer32"
_SlAlsLaserManualActivate_Object = MibTableColumn
slAlsLaserManualActivate = _SlAlsLaserManualActivate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 8),
    _SlAlsLaserManualActivate_Type()
)
slAlsLaserManualActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsLaserManualActivate.setStatus("current")


class _SlAlsOperStatus_Type(Integer32):
    """Custom type slAlsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SlAlsOperStatus_Type.__name__ = "Integer32"
_SlAlsOperStatus_Object = MibTableColumn
slAlsOperStatus = _SlAlsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 9),
    _SlAlsOperStatus_Type()
)
slAlsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlsOperStatus.setStatus("current")


class _SlAlsResetParams_Type(Integer32):
    """Custom type slAlsResetParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounters", 1)
    )


_SlAlsResetParams_Type.__name__ = "Integer32"
_SlAlsResetParams_Object = MibTableColumn
slAlsResetParams = _SlAlsResetParams_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 10),
    _SlAlsResetParams_Type()
)
slAlsResetParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlsResetParams.setStatus("current")
_SlAlsTraps_ObjectIdentity = ObjectIdentity
slAlsTraps = _SlAlsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 2)
)

# Managed Objects groups


# Notification objects

slAlsStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 12, 2, 1)
)
slAlsStatusChangeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SL-ALS-MIB", "slAlsOperStatus"))
)
if mibBuilder.loadTexts:
    slAlsStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-ALS-MIB",
    **{"slAlsMib": slAlsMib,
       "slAlsConfig": slAlsConfig,
       "slAlsConfigTable": slAlsConfigTable,
       "slAlsConfigEntry": slAlsConfigEntry,
       "slAlsMode": slAlsMode,
       "slAlsLosDeclareTime": slAlsLosDeclareTime,
       "slAlsTestPulseTime": slAlsTestPulseTime,
       "slAlsManualPulseTime": slAlsManualPulseTime,
       "slAlsAutomaticPulseTime": slAlsAutomaticPulseTime,
       "slAlsAutomaticDelayTime": slAlsAutomaticDelayTime,
       "slAlsLaserTestActivate": slAlsLaserTestActivate,
       "slAlsLaserManualActivate": slAlsLaserManualActivate,
       "slAlsOperStatus": slAlsOperStatus,
       "slAlsResetParams": slAlsResetParams,
       "slAlsTraps": slAlsTraps,
       "slAlsStatusChangeTrap": slAlsStatusChangeTrap}
)
