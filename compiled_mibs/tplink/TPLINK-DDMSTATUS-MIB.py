# SNMP MIB module (TPLINK-DDMSTATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-DDMSTATUS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:24 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkDdmManageMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-DDMMANAGE-MIB",
    "tplinkDdmManageMIBObjects")


# MODULE-IDENTITY

ddmStatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7)
)
if mibBuilder.loadTexts:
    ddmStatus.setRevisions(
        ("2009-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DdmStatusTable_Object = MibTable
ddmStatusTable = _DdmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ddmStatusTable.setStatus("current")
_DdmStatusEntry_Object = MibTableRow
ddmStatusEntry = _DdmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1)
)
ddmStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmStatusEntry.setStatus("current")


class _DdmStatusPort_Type(DisplayString):
    """Custom type ddmStatusPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DdmStatusPort_Type.__name__ = "DisplayString"
_DdmStatusPort_Object = MibTableColumn
ddmStatusPort = _DdmStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 1),
    _DdmStatusPort_Type()
)
ddmStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusPort.setStatus("current")


class _DdmStatusTemperature_Type(DisplayString):
    """Custom type ddmStatusTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusTemperature_Type.__name__ = "DisplayString"
_DdmStatusTemperature_Object = MibTableColumn
ddmStatusTemperature = _DdmStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 2),
    _DdmStatusTemperature_Type()
)
ddmStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusTemperature.setStatus("current")


class _DdmStatusVoltage_Type(DisplayString):
    """Custom type ddmStatusVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusVoltage_Type.__name__ = "DisplayString"
_DdmStatusVoltage_Object = MibTableColumn
ddmStatusVoltage = _DdmStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 3),
    _DdmStatusVoltage_Type()
)
ddmStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusVoltage.setStatus("current")


class _DdmStatusBiasCurrent_Type(DisplayString):
    """Custom type ddmStatusBiasCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusBiasCurrent_Type.__name__ = "DisplayString"
_DdmStatusBiasCurrent_Object = MibTableColumn
ddmStatusBiasCurrent = _DdmStatusBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 4),
    _DdmStatusBiasCurrent_Type()
)
ddmStatusBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusBiasCurrent.setStatus("current")


class _DdmStatusTxPow_Type(DisplayString):
    """Custom type ddmStatusTxPow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusTxPow_Type.__name__ = "DisplayString"
_DdmStatusTxPow_Object = MibTableColumn
ddmStatusTxPow = _DdmStatusTxPow_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 5),
    _DdmStatusTxPow_Type()
)
ddmStatusTxPow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusTxPow.setStatus("current")


class _DdmStatusRxPow_Type(DisplayString):
    """Custom type ddmStatusRxPow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusRxPow_Type.__name__ = "DisplayString"
_DdmStatusRxPow_Object = MibTableColumn
ddmStatusRxPow = _DdmStatusRxPow_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 6),
    _DdmStatusRxPow_Type()
)
ddmStatusRxPow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusRxPow.setStatus("current")


class _DdmStatusDataReady_Type(DisplayString):
    """Custom type ddmStatusDataReady based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusDataReady_Type.__name__ = "DisplayString"
_DdmStatusDataReady_Object = MibTableColumn
ddmStatusDataReady = _DdmStatusDataReady_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 7),
    _DdmStatusDataReady_Type()
)
ddmStatusDataReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusDataReady.setStatus("current")


class _DdmStatusLossSignal_Type(DisplayString):
    """Custom type ddmStatusLossSignal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusLossSignal_Type.__name__ = "DisplayString"
_DdmStatusLossSignal_Object = MibTableColumn
ddmStatusLossSignal = _DdmStatusLossSignal_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 8),
    _DdmStatusLossSignal_Type()
)
ddmStatusLossSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusLossSignal.setStatus("current")


class _DdmStatusTxFault_Type(DisplayString):
    """Custom type ddmStatusTxFault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmStatusTxFault_Type.__name__ = "DisplayString"
_DdmStatusTxFault_Object = MibTableColumn
ddmStatusTxFault = _DdmStatusTxFault_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 7, 1, 1, 9),
    _DdmStatusTxFault_Type()
)
ddmStatusTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmStatusTxFault.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DDMSTATUS-MIB",
    **{"ddmStatus": ddmStatus,
       "ddmStatusTable": ddmStatusTable,
       "ddmStatusEntry": ddmStatusEntry,
       "ddmStatusPort": ddmStatusPort,
       "ddmStatusTemperature": ddmStatusTemperature,
       "ddmStatusVoltage": ddmStatusVoltage,
       "ddmStatusBiasCurrent": ddmStatusBiasCurrent,
       "ddmStatusTxPow": ddmStatusTxPow,
       "ddmStatusRxPow": ddmStatusRxPow,
       "ddmStatusDataReady": ddmStatusDataReady,
       "ddmStatusLossSignal": ddmStatusLossSignal,
       "ddmStatusTxFault": ddmStatusTxFault}
)
