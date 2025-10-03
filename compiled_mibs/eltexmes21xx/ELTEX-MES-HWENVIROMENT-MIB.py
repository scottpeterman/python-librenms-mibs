# SNMP MIB module (ELTEX-MES-HWENVIROMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltexmes21xx\ELTEX-MES-HWENVIROMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:26 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(RlEnvMonState,) = mibBuilder.importSymbols(
    "RADLAN-HWENVIROMENT",
    "RlEnvMonState")

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

eltMesEnv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 11)
)
if mibBuilder.loadTexts:
    eltMesEnv.setRevisions(
        ("2016-03-04 00:00",
         "2015-06-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltEnvMonBatteryStatusTable_Object = MibTable
eltEnvMonBatteryStatusTable = _EltEnvMonBatteryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 11, 1)
)
if mibBuilder.loadTexts:
    eltEnvMonBatteryStatusTable.setStatus("current")
_EltEnvMonBatteryStatusEntry_Object = MibTableRow
eltEnvMonBatteryStatusEntry = _EltEnvMonBatteryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 11, 1, 1)
)
eltEnvMonBatteryStatusEntry.setIndexNames(
    (0, "ELTEX-MES-HWENVIROMENT-MIB", "eltEnvMonBatteryStatusIndex"),
)
if mibBuilder.loadTexts:
    eltEnvMonBatteryStatusEntry.setStatus("current")
_EltEnvMonBatteryStatusIndex_Type = Integer32
_EltEnvMonBatteryStatusIndex_Object = MibTableColumn
eltEnvMonBatteryStatusIndex = _EltEnvMonBatteryStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 11, 1, 1, 1),
    _EltEnvMonBatteryStatusIndex_Type()
)
eltEnvMonBatteryStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltEnvMonBatteryStatusIndex.setStatus("current")
_EltEnvMonBatteryState_Type = RlEnvMonState
_EltEnvMonBatteryState_Object = MibTableColumn
eltEnvMonBatteryState = _EltEnvMonBatteryState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 11, 1, 1, 2),
    _EltEnvMonBatteryState_Type()
)
eltEnvMonBatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltEnvMonBatteryState.setStatus("current")


class _EltEnvMonBatteryStatusCharge_Type(Integer32):
    """Custom type eltEnvMonBatteryStatusCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(255, 255),
    )


_EltEnvMonBatteryStatusCharge_Type.__name__ = "Integer32"
_EltEnvMonBatteryStatusCharge_Object = MibTableColumn
eltEnvMonBatteryStatusCharge = _EltEnvMonBatteryStatusCharge_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 11, 1, 1, 3),
    _EltEnvMonBatteryStatusCharge_Type()
)
eltEnvMonBatteryStatusCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltEnvMonBatteryStatusCharge.setStatus("current")


class _EltEnvResetButtonMode_Type(Integer32):
    """Custom type eltEnvResetButtonMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1),
          ("reset-only", 2))
    )


_EltEnvResetButtonMode_Type.__name__ = "Integer32"
_EltEnvResetButtonMode_Object = MibScalar
eltEnvResetButtonMode = _EltEnvResetButtonMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 11, 2),
    _EltEnvResetButtonMode_Type()
)
eltEnvResetButtonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltEnvResetButtonMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-HWENVIROMENT-MIB",
    **{"eltMesEnv": eltMesEnv,
       "eltEnvMonBatteryStatusTable": eltEnvMonBatteryStatusTable,
       "eltEnvMonBatteryStatusEntry": eltEnvMonBatteryStatusEntry,
       "eltEnvMonBatteryStatusIndex": eltEnvMonBatteryStatusIndex,
       "eltEnvMonBatteryState": eltEnvMonBatteryState,
       "eltEnvMonBatteryStatusCharge": eltEnvMonBatteryStatusCharge,
       "eltEnvResetButtonMode": eltEnvResetButtonMode}
)
