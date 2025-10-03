# SNMP MIB module (ALCATEL-IND1-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-HEALTH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:25 2025
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

(healthMonTraps,
 softentIND1Health) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "healthMonTraps",
    "softentIND1Health")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1HealthMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions



class HealthPortUpDownStatus(Integer32):
    """Custom type HealthPortUpDownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("healthPortDn", 1),
          ("healthPortUp", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1HealthMonitorMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBObjects = _AlcatelIND1HealthMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBObjects.setStatus("current")
_HealthDeviceInfo_ObjectIdentity = ObjectIdentity
healthDeviceInfo = _HealthDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1)
)


class _HealthDeviceRxLatest_Type(Integer32):
    """Custom type healthDeviceRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRxLatest_Type.__name__ = "Integer32"
_HealthDeviceRxLatest_Object = MibScalar
healthDeviceRxLatest = _HealthDeviceRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 1),
    _HealthDeviceRxLatest_Type()
)
healthDeviceRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxLatest.setStatus("current")


class _HealthDeviceRx1MinAvg_Type(Integer32):
    """Custom type healthDeviceRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRx1MinAvg_Type.__name__ = "Integer32"
_HealthDeviceRx1MinAvg_Object = MibScalar
healthDeviceRx1MinAvg = _HealthDeviceRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 2),
    _HealthDeviceRx1MinAvg_Type()
)
healthDeviceRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRx1MinAvg.setStatus("current")


class _HealthDeviceRx1HrAvg_Type(Integer32):
    """Custom type healthDeviceRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRx1HrAvg_Type.__name__ = "Integer32"
_HealthDeviceRx1HrAvg_Object = MibScalar
healthDeviceRx1HrAvg = _HealthDeviceRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 3),
    _HealthDeviceRx1HrAvg_Type()
)
healthDeviceRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRx1HrAvg.setStatus("current")


class _HealthDeviceRx1HrMax_Type(Integer32):
    """Custom type healthDeviceRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRx1HrMax_Type.__name__ = "Integer32"
_HealthDeviceRx1HrMax_Object = MibScalar
healthDeviceRx1HrMax = _HealthDeviceRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 4),
    _HealthDeviceRx1HrMax_Type()
)
healthDeviceRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRx1HrMax.setStatus("current")


class _HealthDeviceRxTxLatest_Type(Integer32):
    """Custom type healthDeviceRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRxTxLatest_Type.__name__ = "Integer32"
_HealthDeviceRxTxLatest_Object = MibScalar
healthDeviceRxTxLatest = _HealthDeviceRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 5),
    _HealthDeviceRxTxLatest_Type()
)
healthDeviceRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxTxLatest.setStatus("current")


class _HealthDeviceRxTx1MinAvg_Type(Integer32):
    """Custom type healthDeviceRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRxTx1MinAvg_Type.__name__ = "Integer32"
_HealthDeviceRxTx1MinAvg_Object = MibScalar
healthDeviceRxTx1MinAvg = _HealthDeviceRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 6),
    _HealthDeviceRxTx1MinAvg_Type()
)
healthDeviceRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxTx1MinAvg.setStatus("current")


class _HealthDeviceRxTx1HrAvg_Type(Integer32):
    """Custom type healthDeviceRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRxTx1HrAvg_Type.__name__ = "Integer32"
_HealthDeviceRxTx1HrAvg_Object = MibScalar
healthDeviceRxTx1HrAvg = _HealthDeviceRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 7),
    _HealthDeviceRxTx1HrAvg_Type()
)
healthDeviceRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxTx1HrAvg.setStatus("current")


class _HealthDeviceRxTx1HrMax_Type(Integer32):
    """Custom type healthDeviceRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceRxTx1HrMax_Type.__name__ = "Integer32"
_HealthDeviceRxTx1HrMax_Object = MibScalar
healthDeviceRxTx1HrMax = _HealthDeviceRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 8),
    _HealthDeviceRxTx1HrMax_Type()
)
healthDeviceRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxTx1HrMax.setStatus("current")


class _HealthDeviceMemoryLatest_Type(Integer32):
    """Custom type healthDeviceMemoryLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceMemoryLatest_Type.__name__ = "Integer32"
_HealthDeviceMemoryLatest_Object = MibScalar
healthDeviceMemoryLatest = _HealthDeviceMemoryLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 9),
    _HealthDeviceMemoryLatest_Type()
)
healthDeviceMemoryLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemoryLatest.setStatus("current")


class _HealthDeviceMemory1MinAvg_Type(Integer32):
    """Custom type healthDeviceMemory1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceMemory1MinAvg_Type.__name__ = "Integer32"
_HealthDeviceMemory1MinAvg_Object = MibScalar
healthDeviceMemory1MinAvg = _HealthDeviceMemory1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 10),
    _HealthDeviceMemory1MinAvg_Type()
)
healthDeviceMemory1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemory1MinAvg.setStatus("current")


class _HealthDeviceMemory1HrAvg_Type(Integer32):
    """Custom type healthDeviceMemory1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceMemory1HrAvg_Type.__name__ = "Integer32"
_HealthDeviceMemory1HrAvg_Object = MibScalar
healthDeviceMemory1HrAvg = _HealthDeviceMemory1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 11),
    _HealthDeviceMemory1HrAvg_Type()
)
healthDeviceMemory1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemory1HrAvg.setStatus("current")


class _HealthDeviceMemory1HrMax_Type(Integer32):
    """Custom type healthDeviceMemory1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceMemory1HrMax_Type.__name__ = "Integer32"
_HealthDeviceMemory1HrMax_Object = MibScalar
healthDeviceMemory1HrMax = _HealthDeviceMemory1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 12),
    _HealthDeviceMemory1HrMax_Type()
)
healthDeviceMemory1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemory1HrMax.setStatus("current")


class _HealthDeviceCpuLatest_Type(Integer32):
    """Custom type healthDeviceCpuLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceCpuLatest_Type.__name__ = "Integer32"
_HealthDeviceCpuLatest_Object = MibScalar
healthDeviceCpuLatest = _HealthDeviceCpuLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 13),
    _HealthDeviceCpuLatest_Type()
)
healthDeviceCpuLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCpuLatest.setStatus("current")


class _HealthDeviceCpu1MinAvg_Type(Integer32):
    """Custom type healthDeviceCpu1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceCpu1MinAvg_Type.__name__ = "Integer32"
_HealthDeviceCpu1MinAvg_Object = MibScalar
healthDeviceCpu1MinAvg = _HealthDeviceCpu1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 14),
    _HealthDeviceCpu1MinAvg_Type()
)
healthDeviceCpu1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCpu1MinAvg.setStatus("current")


class _HealthDeviceCpu1HrAvg_Type(Integer32):
    """Custom type healthDeviceCpu1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceCpu1HrAvg_Type.__name__ = "Integer32"
_HealthDeviceCpu1HrAvg_Object = MibScalar
healthDeviceCpu1HrAvg = _HealthDeviceCpu1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 15),
    _HealthDeviceCpu1HrAvg_Type()
)
healthDeviceCpu1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCpu1HrAvg.setStatus("current")


class _HealthDeviceCpu1HrMax_Type(Integer32):
    """Custom type healthDeviceCpu1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceCpu1HrMax_Type.__name__ = "Integer32"
_HealthDeviceCpu1HrMax_Object = MibScalar
healthDeviceCpu1HrMax = _HealthDeviceCpu1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 16),
    _HealthDeviceCpu1HrMax_Type()
)
healthDeviceCpu1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCpu1HrMax.setStatus("current")


class _HealthDeviceTemperatureChasLatest_Type(Integer32):
    """Custom type healthDeviceTemperatureChasLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureChasLatest_Type.__name__ = "Integer32"
_HealthDeviceTemperatureChasLatest_Object = MibScalar
healthDeviceTemperatureChasLatest = _HealthDeviceTemperatureChasLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 17),
    _HealthDeviceTemperatureChasLatest_Type()
)
healthDeviceTemperatureChasLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureChasLatest.setStatus("current")


class _HealthDeviceTemperatureChas1MinAvg_Type(Integer32):
    """Custom type healthDeviceTemperatureChas1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureChas1MinAvg_Type.__name__ = "Integer32"
_HealthDeviceTemperatureChas1MinAvg_Object = MibScalar
healthDeviceTemperatureChas1MinAvg = _HealthDeviceTemperatureChas1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 18),
    _HealthDeviceTemperatureChas1MinAvg_Type()
)
healthDeviceTemperatureChas1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureChas1MinAvg.setStatus("current")


class _HealthDeviceTemperatureChas1HrAvg_Type(Integer32):
    """Custom type healthDeviceTemperatureChas1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureChas1HrAvg_Type.__name__ = "Integer32"
_HealthDeviceTemperatureChas1HrAvg_Object = MibScalar
healthDeviceTemperatureChas1HrAvg = _HealthDeviceTemperatureChas1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 19),
    _HealthDeviceTemperatureChas1HrAvg_Type()
)
healthDeviceTemperatureChas1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureChas1HrAvg.setStatus("current")


class _HealthDeviceTemperatureChas1HrMax_Type(Integer32):
    """Custom type healthDeviceTemperatureChas1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureChas1HrMax_Type.__name__ = "Integer32"
_HealthDeviceTemperatureChas1HrMax_Object = MibScalar
healthDeviceTemperatureChas1HrMax = _HealthDeviceTemperatureChas1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 20),
    _HealthDeviceTemperatureChas1HrMax_Type()
)
healthDeviceTemperatureChas1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureChas1HrMax.setStatus("current")


class _HealthDeviceTemperatureCmmCpuLatest_Type(Integer32):
    """Custom type healthDeviceTemperatureCmmCpuLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureCmmCpuLatest_Type.__name__ = "Integer32"
_HealthDeviceTemperatureCmmCpuLatest_Object = MibScalar
healthDeviceTemperatureCmmCpuLatest = _HealthDeviceTemperatureCmmCpuLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 21),
    _HealthDeviceTemperatureCmmCpuLatest_Type()
)
healthDeviceTemperatureCmmCpuLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureCmmCpuLatest.setStatus("obsolete")


class _HealthDeviceTemperatureCmmCpu1MinAvg_Type(Integer32):
    """Custom type healthDeviceTemperatureCmmCpu1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureCmmCpu1MinAvg_Type.__name__ = "Integer32"
_HealthDeviceTemperatureCmmCpu1MinAvg_Object = MibScalar
healthDeviceTemperatureCmmCpu1MinAvg = _HealthDeviceTemperatureCmmCpu1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 22),
    _HealthDeviceTemperatureCmmCpu1MinAvg_Type()
)
healthDeviceTemperatureCmmCpu1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureCmmCpu1MinAvg.setStatus("obsolete")


class _HealthDeviceTemperatureCmmCpu1HrAvg_Type(Integer32):
    """Custom type healthDeviceTemperatureCmmCpu1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureCmmCpu1HrAvg_Type.__name__ = "Integer32"
_HealthDeviceTemperatureCmmCpu1HrAvg_Object = MibScalar
healthDeviceTemperatureCmmCpu1HrAvg = _HealthDeviceTemperatureCmmCpu1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 23),
    _HealthDeviceTemperatureCmmCpu1HrAvg_Type()
)
healthDeviceTemperatureCmmCpu1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureCmmCpu1HrAvg.setStatus("obsolete")


class _HealthDeviceTemperatureCmmCpu1HrMax_Type(Integer32):
    """Custom type healthDeviceTemperatureCmmCpu1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthDeviceTemperatureCmmCpu1HrMax_Type.__name__ = "Integer32"
_HealthDeviceTemperatureCmmCpu1HrMax_Object = MibScalar
healthDeviceTemperatureCmmCpu1HrMax = _HealthDeviceTemperatureCmmCpu1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 1, 24),
    _HealthDeviceTemperatureCmmCpu1HrMax_Type()
)
healthDeviceTemperatureCmmCpu1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureCmmCpu1HrMax.setStatus("obsolete")
_HealthModuleInfo_ObjectIdentity = ObjectIdentity
healthModuleInfo = _HealthModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2)
)
_HealthModuleTable_Object = MibTable
healthModuleTable = _HealthModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    healthModuleTable.setStatus("current")
_HealthModuleEntry_Object = MibTableRow
healthModuleEntry = _HealthModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1)
)
healthModuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthModuleSlot"),
)
if mibBuilder.loadTexts:
    healthModuleEntry.setStatus("current")


class _HealthModuleSlot_Type(Integer32):
    """Custom type healthModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HealthModuleSlot_Type.__name__ = "Integer32"
_HealthModuleSlot_Object = MibTableColumn
healthModuleSlot = _HealthModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 1),
    _HealthModuleSlot_Type()
)
healthModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleSlot.setStatus("current")


class _HealthModuleRxLatest_Type(Integer32):
    """Custom type healthModuleRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxLatest_Type.__name__ = "Integer32"
_HealthModuleRxLatest_Object = MibTableColumn
healthModuleRxLatest = _HealthModuleRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 2),
    _HealthModuleRxLatest_Type()
)
healthModuleRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxLatest.setStatus("current")


class _HealthModuleRx1MinAvg_Type(Integer32):
    """Custom type healthModuleRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRx1MinAvg_Type.__name__ = "Integer32"
_HealthModuleRx1MinAvg_Object = MibTableColumn
healthModuleRx1MinAvg = _HealthModuleRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 3),
    _HealthModuleRx1MinAvg_Type()
)
healthModuleRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRx1MinAvg.setStatus("current")


class _HealthModuleRx1HrAvg_Type(Integer32):
    """Custom type healthModuleRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRx1HrAvg_Type.__name__ = "Integer32"
_HealthModuleRx1HrAvg_Object = MibTableColumn
healthModuleRx1HrAvg = _HealthModuleRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 4),
    _HealthModuleRx1HrAvg_Type()
)
healthModuleRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRx1HrAvg.setStatus("current")


class _HealthModuleRx1HrMax_Type(Integer32):
    """Custom type healthModuleRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRx1HrMax_Type.__name__ = "Integer32"
_HealthModuleRx1HrMax_Object = MibTableColumn
healthModuleRx1HrMax = _HealthModuleRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 5),
    _HealthModuleRx1HrMax_Type()
)
healthModuleRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRx1HrMax.setStatus("current")


class _HealthModuleRxTxLatest_Type(Integer32):
    """Custom type healthModuleRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxTxLatest_Type.__name__ = "Integer32"
_HealthModuleRxTxLatest_Object = MibTableColumn
healthModuleRxTxLatest = _HealthModuleRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 6),
    _HealthModuleRxTxLatest_Type()
)
healthModuleRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTxLatest.setStatus("current")


class _HealthModuleRxTx1MinAvg_Type(Integer32):
    """Custom type healthModuleRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxTx1MinAvg_Type.__name__ = "Integer32"
_HealthModuleRxTx1MinAvg_Object = MibTableColumn
healthModuleRxTx1MinAvg = _HealthModuleRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 7),
    _HealthModuleRxTx1MinAvg_Type()
)
healthModuleRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTx1MinAvg.setStatus("current")


class _HealthModuleRxTx1HrAvg_Type(Integer32):
    """Custom type healthModuleRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxTx1HrAvg_Type.__name__ = "Integer32"
_HealthModuleRxTx1HrAvg_Object = MibTableColumn
healthModuleRxTx1HrAvg = _HealthModuleRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 8),
    _HealthModuleRxTx1HrAvg_Type()
)
healthModuleRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTx1HrAvg.setStatus("current")


class _HealthModuleRxTx1HrMax_Type(Integer32):
    """Custom type healthModuleRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxTx1HrMax_Type.__name__ = "Integer32"
_HealthModuleRxTx1HrMax_Object = MibTableColumn
healthModuleRxTx1HrMax = _HealthModuleRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 9),
    _HealthModuleRxTx1HrMax_Type()
)
healthModuleRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTx1HrMax.setStatus("current")


class _HealthModuleMemoryLatest_Type(Integer32):
    """Custom type healthModuleMemoryLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleMemoryLatest_Type.__name__ = "Integer32"
_HealthModuleMemoryLatest_Object = MibTableColumn
healthModuleMemoryLatest = _HealthModuleMemoryLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 10),
    _HealthModuleMemoryLatest_Type()
)
healthModuleMemoryLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleMemoryLatest.setStatus("current")


class _HealthModuleMemory1MinAvg_Type(Integer32):
    """Custom type healthModuleMemory1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleMemory1MinAvg_Type.__name__ = "Integer32"
_HealthModuleMemory1MinAvg_Object = MibTableColumn
healthModuleMemory1MinAvg = _HealthModuleMemory1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 11),
    _HealthModuleMemory1MinAvg_Type()
)
healthModuleMemory1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleMemory1MinAvg.setStatus("current")


class _HealthModuleMemory1HrAvg_Type(Integer32):
    """Custom type healthModuleMemory1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleMemory1HrAvg_Type.__name__ = "Integer32"
_HealthModuleMemory1HrAvg_Object = MibTableColumn
healthModuleMemory1HrAvg = _HealthModuleMemory1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 12),
    _HealthModuleMemory1HrAvg_Type()
)
healthModuleMemory1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleMemory1HrAvg.setStatus("current")


class _HealthModuleMemory1HrMax_Type(Integer32):
    """Custom type healthModuleMemory1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleMemory1HrMax_Type.__name__ = "Integer32"
_HealthModuleMemory1HrMax_Object = MibTableColumn
healthModuleMemory1HrMax = _HealthModuleMemory1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 13),
    _HealthModuleMemory1HrMax_Type()
)
healthModuleMemory1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleMemory1HrMax.setStatus("current")


class _HealthModuleCpuLatest_Type(Integer32):
    """Custom type healthModuleCpuLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleCpuLatest_Type.__name__ = "Integer32"
_HealthModuleCpuLatest_Object = MibTableColumn
healthModuleCpuLatest = _HealthModuleCpuLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 14),
    _HealthModuleCpuLatest_Type()
)
healthModuleCpuLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCpuLatest.setStatus("current")


class _HealthModuleCpu1MinAvg_Type(Integer32):
    """Custom type healthModuleCpu1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleCpu1MinAvg_Type.__name__ = "Integer32"
_HealthModuleCpu1MinAvg_Object = MibTableColumn
healthModuleCpu1MinAvg = _HealthModuleCpu1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 15),
    _HealthModuleCpu1MinAvg_Type()
)
healthModuleCpu1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCpu1MinAvg.setStatus("current")


class _HealthModuleCpu1HrAvg_Type(Integer32):
    """Custom type healthModuleCpu1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleCpu1HrAvg_Type.__name__ = "Integer32"
_HealthModuleCpu1HrAvg_Object = MibTableColumn
healthModuleCpu1HrAvg = _HealthModuleCpu1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 16),
    _HealthModuleCpu1HrAvg_Type()
)
healthModuleCpu1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCpu1HrAvg.setStatus("current")


class _HealthModuleCpu1HrMax_Type(Integer32):
    """Custom type healthModuleCpu1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleCpu1HrMax_Type.__name__ = "Integer32"
_HealthModuleCpu1HrMax_Object = MibTableColumn
healthModuleCpu1HrMax = _HealthModuleCpu1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 2, 1, 1, 17),
    _HealthModuleCpu1HrMax_Type()
)
healthModuleCpu1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCpu1HrMax.setStatus("current")
_HealthPortInfo_ObjectIdentity = ObjectIdentity
healthPortInfo = _HealthPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3)
)
_HealthPortTable_Object = MibTable
healthPortTable = _HealthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    healthPortTable.setStatus("current")
_HealthPortEntry_Object = MibTableRow
healthPortEntry = _HealthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1)
)
healthPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthPortSlot"),
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthPortIF"),
)
if mibBuilder.loadTexts:
    healthPortEntry.setStatus("current")


class _HealthPortSlot_Type(Integer32):
    """Custom type healthPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HealthPortSlot_Type.__name__ = "Integer32"
_HealthPortSlot_Object = MibTableColumn
healthPortSlot = _HealthPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 1),
    _HealthPortSlot_Type()
)
healthPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortSlot.setStatus("current")


class _HealthPortIF_Type(Integer32):
    """Custom type healthPortIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HealthPortIF_Type.__name__ = "Integer32"
_HealthPortIF_Object = MibTableColumn
healthPortIF = _HealthPortIF_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 2),
    _HealthPortIF_Type()
)
healthPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortIF.setStatus("current")
_HealthPortUpDn_Type = HealthPortUpDownStatus
_HealthPortUpDn_Object = MibTableColumn
healthPortUpDn = _HealthPortUpDn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 3),
    _HealthPortUpDn_Type()
)
healthPortUpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortUpDn.setStatus("current")


class _HealthPortRxLatest_Type(Integer32):
    """Custom type healthPortRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxLatest_Type.__name__ = "Integer32"
_HealthPortRxLatest_Object = MibTableColumn
healthPortRxLatest = _HealthPortRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 4),
    _HealthPortRxLatest_Type()
)
healthPortRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxLatest.setStatus("current")


class _HealthPortRx1MinAvg_Type(Integer32):
    """Custom type healthPortRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRx1MinAvg_Type.__name__ = "Integer32"
_HealthPortRx1MinAvg_Object = MibTableColumn
healthPortRx1MinAvg = _HealthPortRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 5),
    _HealthPortRx1MinAvg_Type()
)
healthPortRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRx1MinAvg.setStatus("current")


class _HealthPortRx1HrAvg_Type(Integer32):
    """Custom type healthPortRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRx1HrAvg_Type.__name__ = "Integer32"
_HealthPortRx1HrAvg_Object = MibTableColumn
healthPortRx1HrAvg = _HealthPortRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 6),
    _HealthPortRx1HrAvg_Type()
)
healthPortRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRx1HrAvg.setStatus("current")


class _HealthPortRx1HrMax_Type(Integer32):
    """Custom type healthPortRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRx1HrMax_Type.__name__ = "Integer32"
_HealthPortRx1HrMax_Object = MibTableColumn
healthPortRx1HrMax = _HealthPortRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 7),
    _HealthPortRx1HrMax_Type()
)
healthPortRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRx1HrMax.setStatus("current")


class _HealthPortRxTxLatest_Type(Integer32):
    """Custom type healthPortRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxTxLatest_Type.__name__ = "Integer32"
_HealthPortRxTxLatest_Object = MibTableColumn
healthPortRxTxLatest = _HealthPortRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 8),
    _HealthPortRxTxLatest_Type()
)
healthPortRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTxLatest.setStatus("current")


class _HealthPortRxTx1MinAvg_Type(Integer32):
    """Custom type healthPortRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxTx1MinAvg_Type.__name__ = "Integer32"
_HealthPortRxTx1MinAvg_Object = MibTableColumn
healthPortRxTx1MinAvg = _HealthPortRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 9),
    _HealthPortRxTx1MinAvg_Type()
)
healthPortRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTx1MinAvg.setStatus("current")


class _HealthPortRxTx1HrAvg_Type(Integer32):
    """Custom type healthPortRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxTx1HrAvg_Type.__name__ = "Integer32"
_HealthPortRxTx1HrAvg_Object = MibTableColumn
healthPortRxTx1HrAvg = _HealthPortRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 10),
    _HealthPortRxTx1HrAvg_Type()
)
healthPortRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTx1HrAvg.setStatus("current")


class _HealthPortRxTx1HrMax_Type(Integer32):
    """Custom type healthPortRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxTx1HrMax_Type.__name__ = "Integer32"
_HealthPortRxTx1HrMax_Object = MibTableColumn
healthPortRxTx1HrMax = _HealthPortRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 3, 1, 1, 11),
    _HealthPortRxTx1HrMax_Type()
)
healthPortRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTx1HrMax.setStatus("current")
_HealthControlInfo_ObjectIdentity = ObjectIdentity
healthControlInfo = _HealthControlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 4)
)


class _HealthSamplingInterval_Type(Integer32):
    """Custom type healthSamplingInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HealthSamplingInterval_Type.__name__ = "Integer32"
_HealthSamplingInterval_Object = MibScalar
healthSamplingInterval = _HealthSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 4, 1),
    _HealthSamplingInterval_Type()
)
healthSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthSamplingInterval.setStatus("current")


class _HealthSamplingReset_Type(Integer32):
    """Custom type healthSamplingReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HealthSamplingReset_Type.__name__ = "Integer32"
_HealthSamplingReset_Object = MibScalar
healthSamplingReset = _HealthSamplingReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 4, 2),
    _HealthSamplingReset_Type()
)
healthSamplingReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthSamplingReset.setStatus("current")
_HealthThreshInfo_ObjectIdentity = ObjectIdentity
healthThreshInfo = _HealthThreshInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5)
)


class _HealthThreshDeviceRxLimit_Type(Integer32):
    """Custom type healthThreshDeviceRxLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceRxLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceRxLimit_Object = MibScalar
healthThreshDeviceRxLimit = _HealthThreshDeviceRxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 1),
    _HealthThreshDeviceRxLimit_Type()
)
healthThreshDeviceRxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceRxLimit.setStatus("current")


class _HealthThreshDeviceRxTxLimit_Type(Integer32):
    """Custom type healthThreshDeviceRxTxLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceRxTxLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceRxTxLimit_Object = MibScalar
healthThreshDeviceRxTxLimit = _HealthThreshDeviceRxTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 2),
    _HealthThreshDeviceRxTxLimit_Type()
)
healthThreshDeviceRxTxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceRxTxLimit.setStatus("current")


class _HealthThreshDeviceMemoryLimit_Type(Integer32):
    """Custom type healthThreshDeviceMemoryLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceMemoryLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceMemoryLimit_Object = MibScalar
healthThreshDeviceMemoryLimit = _HealthThreshDeviceMemoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 3),
    _HealthThreshDeviceMemoryLimit_Type()
)
healthThreshDeviceMemoryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceMemoryLimit.setStatus("current")


class _HealthThreshDeviceCpuLimit_Type(Integer32):
    """Custom type healthThreshDeviceCpuLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceCpuLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceCpuLimit_Object = MibScalar
healthThreshDeviceCpuLimit = _HealthThreshDeviceCpuLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 4),
    _HealthThreshDeviceCpuLimit_Type()
)
healthThreshDeviceCpuLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceCpuLimit.setStatus("current")


class _HealthThreshDeviceRxSecondaryLimit_Type(Integer32):
    """Custom type healthThreshDeviceRxSecondaryLimit based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceRxSecondaryLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceRxSecondaryLimit_Object = MibScalar
healthThreshDeviceRxSecondaryLimit = _HealthThreshDeviceRxSecondaryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 5),
    _HealthThreshDeviceRxSecondaryLimit_Type()
)
healthThreshDeviceRxSecondaryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceRxSecondaryLimit.setStatus("current")


class _HealthThreshDeviceRxTxSecondaryLimit_Type(Integer32):
    """Custom type healthThreshDeviceRxTxSecondaryLimit based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceRxTxSecondaryLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceRxTxSecondaryLimit_Object = MibScalar
healthThreshDeviceRxTxSecondaryLimit = _HealthThreshDeviceRxTxSecondaryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 6),
    _HealthThreshDeviceRxTxSecondaryLimit_Type()
)
healthThreshDeviceRxTxSecondaryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceRxTxSecondaryLimit.setStatus("current")


class _HealthThreshDeviceMemorySecondaryLimit_Type(Integer32):
    """Custom type healthThreshDeviceMemorySecondaryLimit based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceMemorySecondaryLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceMemorySecondaryLimit_Object = MibScalar
healthThreshDeviceMemorySecondaryLimit = _HealthThreshDeviceMemorySecondaryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 7),
    _HealthThreshDeviceMemorySecondaryLimit_Type()
)
healthThreshDeviceMemorySecondaryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceMemorySecondaryLimit.setStatus("current")


class _HealthThreshDeviceCpuSecondaryLimit_Type(Integer32):
    """Custom type healthThreshDeviceCpuSecondaryLimit based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceCpuSecondaryLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceCpuSecondaryLimit_Object = MibScalar
healthThreshDeviceCpuSecondaryLimit = _HealthThreshDeviceCpuSecondaryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 8),
    _HealthThreshDeviceCpuSecondaryLimit_Type()
)
healthThreshDeviceCpuSecondaryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceCpuSecondaryLimit.setStatus("current")


class _HealthThreshDeviceTempLimit_Type(Integer32):
    """Custom type healthThreshDeviceTempLimit based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceTempLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceTempLimit_Object = MibScalar
healthThreshDeviceTempLimit = _HealthThreshDeviceTempLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 9),
    _HealthThreshDeviceTempLimit_Type()
)
healthThreshDeviceTempLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceTempLimit.setStatus("current")


class _HealthThreshDeviceTempSecondaryLimit_Type(Integer32):
    """Custom type healthThreshDeviceTempSecondaryLimit based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceTempSecondaryLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceTempSecondaryLimit_Object = MibScalar
healthThreshDeviceTempSecondaryLimit = _HealthThreshDeviceTempSecondaryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 5, 10),
    _HealthThreshDeviceTempSecondaryLimit_Type()
)
healthThreshDeviceTempSecondaryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceTempSecondaryLimit.setStatus("current")
_HealthTrapInfo_ObjectIdentity = ObjectIdentity
healthTrapInfo = _HealthTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6)
)


class _HealthMonRxStatus_Type(Integer32):
    """Custom type healthMonRxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonRxStatus_Type.__name__ = "Integer32"
_HealthMonRxStatus_Object = MibScalar
healthMonRxStatus = _HealthMonRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 1),
    _HealthMonRxStatus_Type()
)
healthMonRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonRxStatus.setStatus("current")


class _HealthMonRxTxStatus_Type(Integer32):
    """Custom type healthMonRxTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonRxTxStatus_Type.__name__ = "Integer32"
_HealthMonRxTxStatus_Object = MibScalar
healthMonRxTxStatus = _HealthMonRxTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 2),
    _HealthMonRxTxStatus_Type()
)
healthMonRxTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonRxTxStatus.setStatus("current")


class _HealthMonMemoryStatus_Type(Integer32):
    """Custom type healthMonMemoryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonMemoryStatus_Type.__name__ = "Integer32"
_HealthMonMemoryStatus_Object = MibScalar
healthMonMemoryStatus = _HealthMonMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 3),
    _HealthMonMemoryStatus_Type()
)
healthMonMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonMemoryStatus.setStatus("current")


class _HealthMonCpuStatus_Type(Integer32):
    """Custom type healthMonCpuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonCpuStatus_Type.__name__ = "Integer32"
_HealthMonCpuStatus_Object = MibScalar
healthMonCpuStatus = _HealthMonCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 4),
    _HealthMonCpuStatus_Type()
)
healthMonCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonCpuStatus.setStatus("current")


class _HealthMonCmmTempStatus_Type(Integer32):
    """Custom type healthMonCmmTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonCmmTempStatus_Type.__name__ = "Integer32"
_HealthMonCmmTempStatus_Object = MibScalar
healthMonCmmTempStatus = _HealthMonCmmTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 5),
    _HealthMonCmmTempStatus_Type()
)
healthMonCmmTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonCmmTempStatus.setStatus("current")


class _HealthMonCmmCpuTempStatus_Type(Integer32):
    """Custom type healthMonCmmCpuTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonCmmCpuTempStatus_Type.__name__ = "Integer32"
_HealthMonCmmCpuTempStatus_Object = MibScalar
healthMonCmmCpuTempStatus = _HealthMonCmmCpuTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 6),
    _HealthMonCmmCpuTempStatus_Type()
)
healthMonCmmCpuTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonCmmCpuTempStatus.setStatus("current")


class _HealthMonPrimaryFabricRxStatus_Type(Integer32):
    """Custom type healthMonPrimaryFabricRxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonPrimaryFabricRxStatus_Type.__name__ = "Integer32"
_HealthMonPrimaryFabricRxStatus_Object = MibScalar
healthMonPrimaryFabricRxStatus = _HealthMonPrimaryFabricRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 7),
    _HealthMonPrimaryFabricRxStatus_Type()
)
healthMonPrimaryFabricRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonPrimaryFabricRxStatus.setStatus("current")


class _HealthMonPrimaryFabricRxTxStatus_Type(Integer32):
    """Custom type healthMonPrimaryFabricRxTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonPrimaryFabricRxTxStatus_Type.__name__ = "Integer32"
_HealthMonPrimaryFabricRxTxStatus_Object = MibScalar
healthMonPrimaryFabricRxTxStatus = _HealthMonPrimaryFabricRxTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 8),
    _HealthMonPrimaryFabricRxTxStatus_Type()
)
healthMonPrimaryFabricRxTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonPrimaryFabricRxTxStatus.setStatus("current")


class _HealthMonSecondaryFabricRxStatus_Type(Integer32):
    """Custom type healthMonSecondaryFabricRxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonSecondaryFabricRxStatus_Type.__name__ = "Integer32"
_HealthMonSecondaryFabricRxStatus_Object = MibScalar
healthMonSecondaryFabricRxStatus = _HealthMonSecondaryFabricRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 9),
    _HealthMonSecondaryFabricRxStatus_Type()
)
healthMonSecondaryFabricRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonSecondaryFabricRxStatus.setStatus("current")


class _HealthMonSecondaryFabricRxTxStatus_Type(Integer32):
    """Custom type healthMonSecondaryFabricRxTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelowThreshold", 1),
          ("noChange", 2),
          ("crossedAboveThreshold", 3))
    )


_HealthMonSecondaryFabricRxTxStatus_Type.__name__ = "Integer32"
_HealthMonSecondaryFabricRxTxStatus_Object = MibScalar
healthMonSecondaryFabricRxTxStatus = _HealthMonSecondaryFabricRxTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 10),
    _HealthMonSecondaryFabricRxTxStatus_Type()
)
healthMonSecondaryFabricRxTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonSecondaryFabricRxTxStatus.setStatus("current")


class _HealthMonIpcPoolStatus_Type(DisplayString):
    """Custom type healthMonIpcPoolStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HealthMonIpcPoolStatus_Type.__name__ = "DisplayString"
_HealthMonIpcPoolStatus_Object = MibScalar
healthMonIpcPoolStatus = _HealthMonIpcPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 6, 11),
    _HealthMonIpcPoolStatus_Type()
)
healthMonIpcPoolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonIpcPoolStatus.setStatus("current")
_HealthSliceInfo_ObjectIdentity = ObjectIdentity
healthSliceInfo = _HealthSliceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 7)
)
_HealthSliceTable_Object = MibTable
healthSliceTable = _HealthSliceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    healthSliceTable.setStatus("current")
_HealthSliceEntry_Object = MibTableRow
healthSliceEntry = _HealthSliceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 7, 1, 1)
)
healthSliceEntry.setIndexNames(
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthSliceSlot"),
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthSliceSlice"),
)
if mibBuilder.loadTexts:
    healthSliceEntry.setStatus("current")


class _HealthSliceSlot_Type(Integer32):
    """Custom type healthSliceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HealthSliceSlot_Type.__name__ = "Integer32"
_HealthSliceSlot_Object = MibTableColumn
healthSliceSlot = _HealthSliceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 7, 1, 1, 1),
    _HealthSliceSlot_Type()
)
healthSliceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthSliceSlot.setStatus("current")


class _HealthSliceSlice_Type(Integer32):
    """Custom type healthSliceSlice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HealthSliceSlice_Type.__name__ = "Integer32"
_HealthSliceSlice_Object = MibTableColumn
healthSliceSlice = _HealthSliceSlice_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 7, 1, 1, 2),
    _HealthSliceSlice_Type()
)
healthSliceSlice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthSliceSlice.setStatus("current")


class _HealthSliceMemoryLatest_Type(Integer32):
    """Custom type healthSliceMemoryLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthSliceMemoryLatest_Type.__name__ = "Integer32"
_HealthSliceMemoryLatest_Object = MibTableColumn
healthSliceMemoryLatest = _HealthSliceMemoryLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 7, 1, 1, 3),
    _HealthSliceMemoryLatest_Type()
)
healthSliceMemoryLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthSliceMemoryLatest.setStatus("current")


class _HealthSliceCpuLatest_Type(Integer32):
    """Custom type healthSliceCpuLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthSliceCpuLatest_Type.__name__ = "Integer32"
_HealthSliceCpuLatest_Object = MibTableColumn
healthSliceCpuLatest = _HealthSliceCpuLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 7, 1, 1, 4),
    _HealthSliceCpuLatest_Type()
)
healthSliceCpuLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthSliceCpuLatest.setStatus("current")
_HealthFabricInfo_ObjectIdentity = ObjectIdentity
healthFabricInfo = _HealthFabricInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8)
)
_HealthFabricTable_Object = MibTable
healthFabricTable = _HealthFabricTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    healthFabricTable.setStatus("current")
_HealthFabricEntry_Object = MibTableRow
healthFabricEntry = _HealthFabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1)
)
healthFabricEntry.setIndexNames(
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthFabricSlot"),
)
if mibBuilder.loadTexts:
    healthFabricEntry.setStatus("current")


class _HealthFabricSlot_Type(Integer32):
    """Custom type healthFabricSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HealthFabricSlot_Type.__name__ = "Integer32"
_HealthFabricSlot_Object = MibTableColumn
healthFabricSlot = _HealthFabricSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 1),
    _HealthFabricSlot_Type()
)
healthFabricSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSlot.setStatus("current")


class _HealthFabricPrimaryRxLatest_Type(Integer32):
    """Custom type healthFabricPrimaryRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRxLatest_Type.__name__ = "Integer32"
_HealthFabricPrimaryRxLatest_Object = MibTableColumn
healthFabricPrimaryRxLatest = _HealthFabricPrimaryRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 2),
    _HealthFabricPrimaryRxLatest_Type()
)
healthFabricPrimaryRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRxLatest.setStatus("current")


class _HealthFabricPrimaryRx1MinAvg_Type(Integer32):
    """Custom type healthFabricPrimaryRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryRx1MinAvg_Object = MibTableColumn
healthFabricPrimaryRx1MinAvg = _HealthFabricPrimaryRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 3),
    _HealthFabricPrimaryRx1MinAvg_Type()
)
healthFabricPrimaryRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRx1MinAvg.setStatus("current")


class _HealthFabricPrimaryRx1HrAvg_Type(Integer32):
    """Custom type healthFabricPrimaryRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryRx1HrAvg_Object = MibTableColumn
healthFabricPrimaryRx1HrAvg = _HealthFabricPrimaryRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 4),
    _HealthFabricPrimaryRx1HrAvg_Type()
)
healthFabricPrimaryRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRx1HrAvg.setStatus("current")


class _HealthFabricPrimaryRx1HrMax_Type(Integer32):
    """Custom type healthFabricPrimaryRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRx1HrMax_Type.__name__ = "Integer32"
_HealthFabricPrimaryRx1HrMax_Object = MibTableColumn
healthFabricPrimaryRx1HrMax = _HealthFabricPrimaryRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 5),
    _HealthFabricPrimaryRx1HrMax_Type()
)
healthFabricPrimaryRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRx1HrMax.setStatus("current")


class _HealthFabricPrimaryRxTxLatest_Type(Integer32):
    """Custom type healthFabricPrimaryRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRxTxLatest_Type.__name__ = "Integer32"
_HealthFabricPrimaryRxTxLatest_Object = MibTableColumn
healthFabricPrimaryRxTxLatest = _HealthFabricPrimaryRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 6),
    _HealthFabricPrimaryRxTxLatest_Type()
)
healthFabricPrimaryRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRxTxLatest.setStatus("current")


class _HealthFabricPrimaryRxTx1MinAvg_Type(Integer32):
    """Custom type healthFabricPrimaryRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRxTx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryRxTx1MinAvg_Object = MibTableColumn
healthFabricPrimaryRxTx1MinAvg = _HealthFabricPrimaryRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 7),
    _HealthFabricPrimaryRxTx1MinAvg_Type()
)
healthFabricPrimaryRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRxTx1MinAvg.setStatus("current")


class _HealthFabricPrimaryRxTx1HrAvg_Type(Integer32):
    """Custom type healthFabricPrimaryRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRxTx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryRxTx1HrAvg_Object = MibTableColumn
healthFabricPrimaryRxTx1HrAvg = _HealthFabricPrimaryRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 8),
    _HealthFabricPrimaryRxTx1HrAvg_Type()
)
healthFabricPrimaryRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRxTx1HrAvg.setStatus("current")


class _HealthFabricPrimaryRxTx1HrMax_Type(Integer32):
    """Custom type healthFabricPrimaryRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryRxTx1HrMax_Type.__name__ = "Integer32"
_HealthFabricPrimaryRxTx1HrMax_Object = MibTableColumn
healthFabricPrimaryRxTx1HrMax = _HealthFabricPrimaryRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 9),
    _HealthFabricPrimaryRxTx1HrMax_Type()
)
healthFabricPrimaryRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryRxTx1HrMax.setStatus("current")


class _HealthFabricSecondaryRxLatest_Type(Integer32):
    """Custom type healthFabricSecondaryRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRxLatest_Type.__name__ = "Integer32"
_HealthFabricSecondaryRxLatest_Object = MibTableColumn
healthFabricSecondaryRxLatest = _HealthFabricSecondaryRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 10),
    _HealthFabricSecondaryRxLatest_Type()
)
healthFabricSecondaryRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRxLatest.setStatus("current")


class _HealthFabricSecondaryRx1MinAvg_Type(Integer32):
    """Custom type healthFabricSecondaryRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryRx1MinAvg_Object = MibTableColumn
healthFabricSecondaryRx1MinAvg = _HealthFabricSecondaryRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 11),
    _HealthFabricSecondaryRx1MinAvg_Type()
)
healthFabricSecondaryRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRx1MinAvg.setStatus("current")


class _HealthFabricSecondaryRx1HrAvg_Type(Integer32):
    """Custom type healthFabricSecondaryRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryRx1HrAvg_Object = MibTableColumn
healthFabricSecondaryRx1HrAvg = _HealthFabricSecondaryRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 12),
    _HealthFabricSecondaryRx1HrAvg_Type()
)
healthFabricSecondaryRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRx1HrAvg.setStatus("current")


class _HealthFabricSecondaryRx1HrMax_Type(Integer32):
    """Custom type healthFabricSecondaryRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRx1HrMax_Type.__name__ = "Integer32"
_HealthFabricSecondaryRx1HrMax_Object = MibTableColumn
healthFabricSecondaryRx1HrMax = _HealthFabricSecondaryRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 13),
    _HealthFabricSecondaryRx1HrMax_Type()
)
healthFabricSecondaryRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRx1HrMax.setStatus("current")


class _HealthFabricSecondaryRxTxLatest_Type(Integer32):
    """Custom type healthFabricSecondaryRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRxTxLatest_Type.__name__ = "Integer32"
_HealthFabricSecondaryRxTxLatest_Object = MibTableColumn
healthFabricSecondaryRxTxLatest = _HealthFabricSecondaryRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 14),
    _HealthFabricSecondaryRxTxLatest_Type()
)
healthFabricSecondaryRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRxTxLatest.setStatus("current")


class _HealthFabricSecondaryRxTx1MinAvg_Type(Integer32):
    """Custom type healthFabricSecondaryRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRxTx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryRxTx1MinAvg_Object = MibTableColumn
healthFabricSecondaryRxTx1MinAvg = _HealthFabricSecondaryRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 15),
    _HealthFabricSecondaryRxTx1MinAvg_Type()
)
healthFabricSecondaryRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRxTx1MinAvg.setStatus("current")


class _HealthFabricSecondaryRxTx1HrAvg_Type(Integer32):
    """Custom type healthFabricSecondaryRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRxTx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryRxTx1HrAvg_Object = MibTableColumn
healthFabricSecondaryRxTx1HrAvg = _HealthFabricSecondaryRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 16),
    _HealthFabricSecondaryRxTx1HrAvg_Type()
)
healthFabricSecondaryRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRxTx1HrAvg.setStatus("current")


class _HealthFabricSecondaryRxTx1HrMax_Type(Integer32):
    """Custom type healthFabricSecondaryRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryRxTx1HrMax_Type.__name__ = "Integer32"
_HealthFabricSecondaryRxTx1HrMax_Object = MibTableColumn
healthFabricSecondaryRxTx1HrMax = _HealthFabricSecondaryRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 17),
    _HealthFabricSecondaryRxTx1HrMax_Type()
)
healthFabricSecondaryRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryRxTx1HrMax.setStatus("current")


class _HealthFabricPrimaryLink1RxLatest_Type(Integer32):
    """Custom type healthFabricPrimaryLink1RxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1RxLatest_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1RxLatest_Object = MibTableColumn
healthFabricPrimaryLink1RxLatest = _HealthFabricPrimaryLink1RxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 18),
    _HealthFabricPrimaryLink1RxLatest_Type()
)
healthFabricPrimaryLink1RxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1RxLatest.setStatus("current")


class _HealthFabricPrimaryLink1Rx1MinAvg_Type(Integer32):
    """Custom type healthFabricPrimaryLink1Rx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1Rx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1Rx1MinAvg_Object = MibTableColumn
healthFabricPrimaryLink1Rx1MinAvg = _HealthFabricPrimaryLink1Rx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 19),
    _HealthFabricPrimaryLink1Rx1MinAvg_Type()
)
healthFabricPrimaryLink1Rx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1Rx1MinAvg.setStatus("current")


class _HealthFabricPrimaryLink1Rx1HrAvg_Type(Integer32):
    """Custom type healthFabricPrimaryLink1Rx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1Rx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1Rx1HrAvg_Object = MibTableColumn
healthFabricPrimaryLink1Rx1HrAvg = _HealthFabricPrimaryLink1Rx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 20),
    _HealthFabricPrimaryLink1Rx1HrAvg_Type()
)
healthFabricPrimaryLink1Rx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1Rx1HrAvg.setStatus("current")


class _HealthFabricPrimaryLink1Rx1HrMax_Type(Integer32):
    """Custom type healthFabricPrimaryLink1Rx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1Rx1HrMax_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1Rx1HrMax_Object = MibTableColumn
healthFabricPrimaryLink1Rx1HrMax = _HealthFabricPrimaryLink1Rx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 21),
    _HealthFabricPrimaryLink1Rx1HrMax_Type()
)
healthFabricPrimaryLink1Rx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1Rx1HrMax.setStatus("current")


class _HealthFabricPrimaryLink1RxTxLatest_Type(Integer32):
    """Custom type healthFabricPrimaryLink1RxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1RxTxLatest_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1RxTxLatest_Object = MibTableColumn
healthFabricPrimaryLink1RxTxLatest = _HealthFabricPrimaryLink1RxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 22),
    _HealthFabricPrimaryLink1RxTxLatest_Type()
)
healthFabricPrimaryLink1RxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1RxTxLatest.setStatus("current")


class _HealthFabricPrimaryLink1RxTx1MinAvg_Type(Integer32):
    """Custom type healthFabricPrimaryLink1RxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1RxTx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1RxTx1MinAvg_Object = MibTableColumn
healthFabricPrimaryLink1RxTx1MinAvg = _HealthFabricPrimaryLink1RxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 23),
    _HealthFabricPrimaryLink1RxTx1MinAvg_Type()
)
healthFabricPrimaryLink1RxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1RxTx1MinAvg.setStatus("current")


class _HealthFabricPrimaryLink1RxTx1HrAvg_Type(Integer32):
    """Custom type healthFabricPrimaryLink1RxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1RxTx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1RxTx1HrAvg_Object = MibTableColumn
healthFabricPrimaryLink1RxTx1HrAvg = _HealthFabricPrimaryLink1RxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 24),
    _HealthFabricPrimaryLink1RxTx1HrAvg_Type()
)
healthFabricPrimaryLink1RxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1RxTx1HrAvg.setStatus("current")


class _HealthFabricPrimaryLink1RxTx1HrMax_Type(Integer32):
    """Custom type healthFabricPrimaryLink1RxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricPrimaryLink1RxTx1HrMax_Type.__name__ = "Integer32"
_HealthFabricPrimaryLink1RxTx1HrMax_Object = MibTableColumn
healthFabricPrimaryLink1RxTx1HrMax = _HealthFabricPrimaryLink1RxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 25),
    _HealthFabricPrimaryLink1RxTx1HrMax_Type()
)
healthFabricPrimaryLink1RxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricPrimaryLink1RxTx1HrMax.setStatus("current")


class _HealthFabricSecondaryLink1RxLatest_Type(Integer32):
    """Custom type healthFabricSecondaryLink1RxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1RxLatest_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1RxLatest_Object = MibTableColumn
healthFabricSecondaryLink1RxLatest = _HealthFabricSecondaryLink1RxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 26),
    _HealthFabricSecondaryLink1RxLatest_Type()
)
healthFabricSecondaryLink1RxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1RxLatest.setStatus("current")


class _HealthFabricSecondaryLink1Rx1MinAvg_Type(Integer32):
    """Custom type healthFabricSecondaryLink1Rx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1Rx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1Rx1MinAvg_Object = MibTableColumn
healthFabricSecondaryLink1Rx1MinAvg = _HealthFabricSecondaryLink1Rx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 27),
    _HealthFabricSecondaryLink1Rx1MinAvg_Type()
)
healthFabricSecondaryLink1Rx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1Rx1MinAvg.setStatus("current")


class _HealthFabricSecondaryLink1Rx1HrAvg_Type(Integer32):
    """Custom type healthFabricSecondaryLink1Rx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1Rx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1Rx1HrAvg_Object = MibTableColumn
healthFabricSecondaryLink1Rx1HrAvg = _HealthFabricSecondaryLink1Rx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 28),
    _HealthFabricSecondaryLink1Rx1HrAvg_Type()
)
healthFabricSecondaryLink1Rx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1Rx1HrAvg.setStatus("current")


class _HealthFabricSecondaryLink1Rx1HrMax_Type(Integer32):
    """Custom type healthFabricSecondaryLink1Rx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1Rx1HrMax_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1Rx1HrMax_Object = MibTableColumn
healthFabricSecondaryLink1Rx1HrMax = _HealthFabricSecondaryLink1Rx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 29),
    _HealthFabricSecondaryLink1Rx1HrMax_Type()
)
healthFabricSecondaryLink1Rx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1Rx1HrMax.setStatus("current")


class _HealthFabricSecondaryLink1RxTxLatest_Type(Integer32):
    """Custom type healthFabricSecondaryLink1RxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1RxTxLatest_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1RxTxLatest_Object = MibTableColumn
healthFabricSecondaryLink1RxTxLatest = _HealthFabricSecondaryLink1RxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 30),
    _HealthFabricSecondaryLink1RxTxLatest_Type()
)
healthFabricSecondaryLink1RxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1RxTxLatest.setStatus("current")


class _HealthFabricSecondaryLink1RxTx1MinAvg_Type(Integer32):
    """Custom type healthFabricSecondaryLink1RxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1RxTx1MinAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1RxTx1MinAvg_Object = MibTableColumn
healthFabricSecondaryLink1RxTx1MinAvg = _HealthFabricSecondaryLink1RxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 31),
    _HealthFabricSecondaryLink1RxTx1MinAvg_Type()
)
healthFabricSecondaryLink1RxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1RxTx1MinAvg.setStatus("current")


class _HealthFabricSecondaryLink1RxTx1HrAvg_Type(Integer32):
    """Custom type healthFabricSecondaryLink1RxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1RxTx1HrAvg_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1RxTx1HrAvg_Object = MibTableColumn
healthFabricSecondaryLink1RxTx1HrAvg = _HealthFabricSecondaryLink1RxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 32),
    _HealthFabricSecondaryLink1RxTx1HrAvg_Type()
)
healthFabricSecondaryLink1RxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1RxTx1HrAvg.setStatus("current")


class _HealthFabricSecondaryLink1RxTx1HrMax_Type(Integer32):
    """Custom type healthFabricSecondaryLink1RxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthFabricSecondaryLink1RxTx1HrMax_Type.__name__ = "Integer32"
_HealthFabricSecondaryLink1RxTx1HrMax_Object = MibTableColumn
healthFabricSecondaryLink1RxTx1HrMax = _HealthFabricSecondaryLink1RxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 1, 8, 1, 1, 33),
    _HealthFabricSecondaryLink1RxTx1HrMax_Type()
)
healthFabricSecondaryLink1RxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthFabricSecondaryLink1RxTx1HrMax.setStatus("current")
_AlcatelIND1HealthMonitorMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBConformance = _AlcatelIND1HealthMonitorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBConformance.setStatus("current")
_AlcatelIND1HealthMonitorMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBGroups = _AlcatelIND1HealthMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBGroups.setStatus("current")
_AlcatelIND1HealthMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBCompliances = _AlcatelIND1HealthMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBCompliances.setStatus("current")

# Managed Objects groups

healthDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 1)
)
healthDeviceGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRxTxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceRxTx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceMemoryLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceMemory1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceMemory1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceMemory1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceCpuLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceCpu1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceCpu1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceCpu1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureChas1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureChasLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureChas1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureChas1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureChas1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureCmmCpuLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureCmmCpu1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureCmmCpu1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthDeviceTemperatureCmmCpu1HrMax"))
)
if mibBuilder.loadTexts:
    healthDeviceGroup.setStatus("current")

healthModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 2)
)
healthModuleGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthModuleSlot"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleMemoryLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleMemory1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleMemory1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleMemory1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpuLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpu1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpu1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpu1HrMax"))
)
if mibBuilder.loadTexts:
    healthModuleGroup.setStatus("current")

healthPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 3)
)
healthPortGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthPortSlot"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortIF"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTx1HrMax"))
)
if mibBuilder.loadTexts:
    healthPortGroup.setStatus("current")

healthControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 4)
)
healthControlGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthSamplingInterval"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthSamplingReset"))
)
if mibBuilder.loadTexts:
    healthControlGroup.setStatus("current")

healthThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 5)
)
healthThreshGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceRxLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceRxTxLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceMemoryLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceCpuLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceRxSecondaryLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceRxTxSecondaryLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceMemorySecondaryLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceCpuSecondaryLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceTempLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshDeviceTempSecondaryLimit"))
)
if mibBuilder.loadTexts:
    healthThreshGroup.setStatus("current")

healthTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 6)
)
healthTrapObjectsGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthMonRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxTxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonMemoryStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCpuStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCmmTempStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCmmCpuTempStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonPrimaryFabricRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonPrimaryFabricRxTxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonSecondaryFabricRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonSecondaryFabricRxTxStatus"))
)
if mibBuilder.loadTexts:
    healthTrapObjectsGroup.setStatus("current")

healthSliceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 8)
)
healthSliceGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthSliceSlot"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthSliceSlice"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthSliceMemoryLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthSliceCpuLatest"))
)
if mibBuilder.loadTexts:
    healthSliceGroup.setStatus("current")

healthFabricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 9)
)
healthFabricGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRxTxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryRxTx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRxTxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryRxTx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1RxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1Rx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1Rx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1Rx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1RxTxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1RxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1RxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricPrimaryLink1RxTx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1RxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1Rx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1Rx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1Rx1HrMax"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1RxTxLatest"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1RxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1RxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthFabricSecondaryLink1RxTx1HrMax"))
)
if mibBuilder.loadTexts:
    healthFabricGroup.setStatus("current")


# Notification objects

healthMonDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 5, 0, 1)
)
healthMonDeviceTrap.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthMonRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxTxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonMemoryStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCpuStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCmmTempStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCmmCpuTempStatus"))
)
if mibBuilder.loadTexts:
    healthMonDeviceTrap.setStatus(
        "current"
    )

healthMonModuleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 5, 0, 2)
)
healthMonModuleTrap.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthModuleSlot"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxTxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonMemoryStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCpuStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonPrimaryFabricRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonPrimaryFabricRxTxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonSecondaryFabricRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonSecondaryFabricRxTxStatus"))
)
if mibBuilder.loadTexts:
    healthMonModuleTrap.setStatus(
        "current"
    )

healthMonPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 5, 0, 3)
)
healthMonPortTrap.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthPortSlot"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortIF"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxTxStatus"))
)
if mibBuilder.loadTexts:
    healthMonPortTrap.setStatus(
        "current"
    )

healthMonIpcTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 5, 0, 4)
)
healthMonIpcTrap.setObjects(
    ("ALCATEL-IND1-HEALTH-MIB", "healthMonIpcPoolStatus")
)
if mibBuilder.loadTexts:
    healthMonIpcTrap.setStatus(
        "current"
    )

healthMonCpuShutPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 5, 0, 5)
)
healthMonCpuShutPortTrap.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthModuleSlot"),
        ("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpuLatest"))
)
if mibBuilder.loadTexts:
    healthMonCpuShutPortTrap.setStatus(
        "current"
    )


# Notifications groups

healthTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 1, 7)
)
healthTrapsGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthMonDeviceTrap"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonModuleTrap"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonPortTrap"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonIpcTrap"))
)
if mibBuilder.loadTexts:
    healthTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1HealthMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 16, 1, 2, 2, 1)
)
alcatelIND1HealthMonitorMIBCompliance.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthDeviceGroup"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleGroup"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortGroup"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthControlGroup"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshGroup"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthSliceGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-HEALTH-MIB",
    **{"HealthPortUpDownStatus": HealthPortUpDownStatus,
       "alcatelIND1HealthMonitorMIB": alcatelIND1HealthMonitorMIB,
       "alcatelIND1HealthMonitorMIBObjects": alcatelIND1HealthMonitorMIBObjects,
       "healthDeviceInfo": healthDeviceInfo,
       "healthDeviceRxLatest": healthDeviceRxLatest,
       "healthDeviceRx1MinAvg": healthDeviceRx1MinAvg,
       "healthDeviceRx1HrAvg": healthDeviceRx1HrAvg,
       "healthDeviceRx1HrMax": healthDeviceRx1HrMax,
       "healthDeviceRxTxLatest": healthDeviceRxTxLatest,
       "healthDeviceRxTx1MinAvg": healthDeviceRxTx1MinAvg,
       "healthDeviceRxTx1HrAvg": healthDeviceRxTx1HrAvg,
       "healthDeviceRxTx1HrMax": healthDeviceRxTx1HrMax,
       "healthDeviceMemoryLatest": healthDeviceMemoryLatest,
       "healthDeviceMemory1MinAvg": healthDeviceMemory1MinAvg,
       "healthDeviceMemory1HrAvg": healthDeviceMemory1HrAvg,
       "healthDeviceMemory1HrMax": healthDeviceMemory1HrMax,
       "healthDeviceCpuLatest": healthDeviceCpuLatest,
       "healthDeviceCpu1MinAvg": healthDeviceCpu1MinAvg,
       "healthDeviceCpu1HrAvg": healthDeviceCpu1HrAvg,
       "healthDeviceCpu1HrMax": healthDeviceCpu1HrMax,
       "healthDeviceTemperatureChasLatest": healthDeviceTemperatureChasLatest,
       "healthDeviceTemperatureChas1MinAvg": healthDeviceTemperatureChas1MinAvg,
       "healthDeviceTemperatureChas1HrAvg": healthDeviceTemperatureChas1HrAvg,
       "healthDeviceTemperatureChas1HrMax": healthDeviceTemperatureChas1HrMax,
       "healthDeviceTemperatureCmmCpuLatest": healthDeviceTemperatureCmmCpuLatest,
       "healthDeviceTemperatureCmmCpu1MinAvg": healthDeviceTemperatureCmmCpu1MinAvg,
       "healthDeviceTemperatureCmmCpu1HrAvg": healthDeviceTemperatureCmmCpu1HrAvg,
       "healthDeviceTemperatureCmmCpu1HrMax": healthDeviceTemperatureCmmCpu1HrMax,
       "healthModuleInfo": healthModuleInfo,
       "healthModuleTable": healthModuleTable,
       "healthModuleEntry": healthModuleEntry,
       "healthModuleSlot": healthModuleSlot,
       "healthModuleRxLatest": healthModuleRxLatest,
       "healthModuleRx1MinAvg": healthModuleRx1MinAvg,
       "healthModuleRx1HrAvg": healthModuleRx1HrAvg,
       "healthModuleRx1HrMax": healthModuleRx1HrMax,
       "healthModuleRxTxLatest": healthModuleRxTxLatest,
       "healthModuleRxTx1MinAvg": healthModuleRxTx1MinAvg,
       "healthModuleRxTx1HrAvg": healthModuleRxTx1HrAvg,
       "healthModuleRxTx1HrMax": healthModuleRxTx1HrMax,
       "healthModuleMemoryLatest": healthModuleMemoryLatest,
       "healthModuleMemory1MinAvg": healthModuleMemory1MinAvg,
       "healthModuleMemory1HrAvg": healthModuleMemory1HrAvg,
       "healthModuleMemory1HrMax": healthModuleMemory1HrMax,
       "healthModuleCpuLatest": healthModuleCpuLatest,
       "healthModuleCpu1MinAvg": healthModuleCpu1MinAvg,
       "healthModuleCpu1HrAvg": healthModuleCpu1HrAvg,
       "healthModuleCpu1HrMax": healthModuleCpu1HrMax,
       "healthPortInfo": healthPortInfo,
       "healthPortTable": healthPortTable,
       "healthPortEntry": healthPortEntry,
       "healthPortSlot": healthPortSlot,
       "healthPortIF": healthPortIF,
       "healthPortUpDn": healthPortUpDn,
       "healthPortRxLatest": healthPortRxLatest,
       "healthPortRx1MinAvg": healthPortRx1MinAvg,
       "healthPortRx1HrAvg": healthPortRx1HrAvg,
       "healthPortRx1HrMax": healthPortRx1HrMax,
       "healthPortRxTxLatest": healthPortRxTxLatest,
       "healthPortRxTx1MinAvg": healthPortRxTx1MinAvg,
       "healthPortRxTx1HrAvg": healthPortRxTx1HrAvg,
       "healthPortRxTx1HrMax": healthPortRxTx1HrMax,
       "healthControlInfo": healthControlInfo,
       "healthSamplingInterval": healthSamplingInterval,
       "healthSamplingReset": healthSamplingReset,
       "healthThreshInfo": healthThreshInfo,
       "healthThreshDeviceRxLimit": healthThreshDeviceRxLimit,
       "healthThreshDeviceRxTxLimit": healthThreshDeviceRxTxLimit,
       "healthThreshDeviceMemoryLimit": healthThreshDeviceMemoryLimit,
       "healthThreshDeviceCpuLimit": healthThreshDeviceCpuLimit,
       "healthThreshDeviceRxSecondaryLimit": healthThreshDeviceRxSecondaryLimit,
       "healthThreshDeviceRxTxSecondaryLimit": healthThreshDeviceRxTxSecondaryLimit,
       "healthThreshDeviceMemorySecondaryLimit": healthThreshDeviceMemorySecondaryLimit,
       "healthThreshDeviceCpuSecondaryLimit": healthThreshDeviceCpuSecondaryLimit,
       "healthThreshDeviceTempLimit": healthThreshDeviceTempLimit,
       "healthThreshDeviceTempSecondaryLimit": healthThreshDeviceTempSecondaryLimit,
       "healthTrapInfo": healthTrapInfo,
       "healthMonRxStatus": healthMonRxStatus,
       "healthMonRxTxStatus": healthMonRxTxStatus,
       "healthMonMemoryStatus": healthMonMemoryStatus,
       "healthMonCpuStatus": healthMonCpuStatus,
       "healthMonCmmTempStatus": healthMonCmmTempStatus,
       "healthMonCmmCpuTempStatus": healthMonCmmCpuTempStatus,
       "healthMonPrimaryFabricRxStatus": healthMonPrimaryFabricRxStatus,
       "healthMonPrimaryFabricRxTxStatus": healthMonPrimaryFabricRxTxStatus,
       "healthMonSecondaryFabricRxStatus": healthMonSecondaryFabricRxStatus,
       "healthMonSecondaryFabricRxTxStatus": healthMonSecondaryFabricRxTxStatus,
       "healthMonIpcPoolStatus": healthMonIpcPoolStatus,
       "healthSliceInfo": healthSliceInfo,
       "healthSliceTable": healthSliceTable,
       "healthSliceEntry": healthSliceEntry,
       "healthSliceSlot": healthSliceSlot,
       "healthSliceSlice": healthSliceSlice,
       "healthSliceMemoryLatest": healthSliceMemoryLatest,
       "healthSliceCpuLatest": healthSliceCpuLatest,
       "healthFabricInfo": healthFabricInfo,
       "healthFabricTable": healthFabricTable,
       "healthFabricEntry": healthFabricEntry,
       "healthFabricSlot": healthFabricSlot,
       "healthFabricPrimaryRxLatest": healthFabricPrimaryRxLatest,
       "healthFabricPrimaryRx1MinAvg": healthFabricPrimaryRx1MinAvg,
       "healthFabricPrimaryRx1HrAvg": healthFabricPrimaryRx1HrAvg,
       "healthFabricPrimaryRx1HrMax": healthFabricPrimaryRx1HrMax,
       "healthFabricPrimaryRxTxLatest": healthFabricPrimaryRxTxLatest,
       "healthFabricPrimaryRxTx1MinAvg": healthFabricPrimaryRxTx1MinAvg,
       "healthFabricPrimaryRxTx1HrAvg": healthFabricPrimaryRxTx1HrAvg,
       "healthFabricPrimaryRxTx1HrMax": healthFabricPrimaryRxTx1HrMax,
       "healthFabricSecondaryRxLatest": healthFabricSecondaryRxLatest,
       "healthFabricSecondaryRx1MinAvg": healthFabricSecondaryRx1MinAvg,
       "healthFabricSecondaryRx1HrAvg": healthFabricSecondaryRx1HrAvg,
       "healthFabricSecondaryRx1HrMax": healthFabricSecondaryRx1HrMax,
       "healthFabricSecondaryRxTxLatest": healthFabricSecondaryRxTxLatest,
       "healthFabricSecondaryRxTx1MinAvg": healthFabricSecondaryRxTx1MinAvg,
       "healthFabricSecondaryRxTx1HrAvg": healthFabricSecondaryRxTx1HrAvg,
       "healthFabricSecondaryRxTx1HrMax": healthFabricSecondaryRxTx1HrMax,
       "healthFabricPrimaryLink1RxLatest": healthFabricPrimaryLink1RxLatest,
       "healthFabricPrimaryLink1Rx1MinAvg": healthFabricPrimaryLink1Rx1MinAvg,
       "healthFabricPrimaryLink1Rx1HrAvg": healthFabricPrimaryLink1Rx1HrAvg,
       "healthFabricPrimaryLink1Rx1HrMax": healthFabricPrimaryLink1Rx1HrMax,
       "healthFabricPrimaryLink1RxTxLatest": healthFabricPrimaryLink1RxTxLatest,
       "healthFabricPrimaryLink1RxTx1MinAvg": healthFabricPrimaryLink1RxTx1MinAvg,
       "healthFabricPrimaryLink1RxTx1HrAvg": healthFabricPrimaryLink1RxTx1HrAvg,
       "healthFabricPrimaryLink1RxTx1HrMax": healthFabricPrimaryLink1RxTx1HrMax,
       "healthFabricSecondaryLink1RxLatest": healthFabricSecondaryLink1RxLatest,
       "healthFabricSecondaryLink1Rx1MinAvg": healthFabricSecondaryLink1Rx1MinAvg,
       "healthFabricSecondaryLink1Rx1HrAvg": healthFabricSecondaryLink1Rx1HrAvg,
       "healthFabricSecondaryLink1Rx1HrMax": healthFabricSecondaryLink1Rx1HrMax,
       "healthFabricSecondaryLink1RxTxLatest": healthFabricSecondaryLink1RxTxLatest,
       "healthFabricSecondaryLink1RxTx1MinAvg": healthFabricSecondaryLink1RxTx1MinAvg,
       "healthFabricSecondaryLink1RxTx1HrAvg": healthFabricSecondaryLink1RxTx1HrAvg,
       "healthFabricSecondaryLink1RxTx1HrMax": healthFabricSecondaryLink1RxTx1HrMax,
       "alcatelIND1HealthMonitorMIBConformance": alcatelIND1HealthMonitorMIBConformance,
       "alcatelIND1HealthMonitorMIBGroups": alcatelIND1HealthMonitorMIBGroups,
       "healthDeviceGroup": healthDeviceGroup,
       "healthModuleGroup": healthModuleGroup,
       "healthPortGroup": healthPortGroup,
       "healthControlGroup": healthControlGroup,
       "healthThreshGroup": healthThreshGroup,
       "healthTrapObjectsGroup": healthTrapObjectsGroup,
       "healthTrapsGroup": healthTrapsGroup,
       "healthSliceGroup": healthSliceGroup,
       "healthFabricGroup": healthFabricGroup,
       "alcatelIND1HealthMonitorMIBCompliances": alcatelIND1HealthMonitorMIBCompliances,
       "alcatelIND1HealthMonitorMIBCompliance": alcatelIND1HealthMonitorMIBCompliance,
       "healthMonDeviceTrap": healthMonDeviceTrap,
       "healthMonModuleTrap": healthMonModuleTrap,
       "healthMonPortTrap": healthMonPortTrap,
       "healthMonIpcTrap": healthMonIpcTrap,
       "healthMonCpuShutPortTrap": healthMonCpuShutPortTrap}
)
