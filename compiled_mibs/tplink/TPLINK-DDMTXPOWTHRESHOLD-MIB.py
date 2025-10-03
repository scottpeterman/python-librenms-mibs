# SNMP MIB module (TPLINK-DDMTXPOWTHRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-DDMTXPOWTHRESHOLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:27 2025
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

ddmTxPowThreshold = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5)
)
if mibBuilder.loadTexts:
    ddmTxPowThreshold.setRevisions(
        ("2009-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DdmTxPowThresholdTable_Object = MibTable
ddmTxPowThresholdTable = _DdmTxPowThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ddmTxPowThresholdTable.setStatus("current")
_DdmTxPowThresholdEntry_Object = MibTableRow
ddmTxPowThresholdEntry = _DdmTxPowThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1, 1)
)
ddmTxPowThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmTxPowThresholdEntry.setStatus("current")


class _DdmTxPowThresholdPort_Type(DisplayString):
    """Custom type ddmTxPowThresholdPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DdmTxPowThresholdPort_Type.__name__ = "DisplayString"
_DdmTxPowThresholdPort_Object = MibTableColumn
ddmTxPowThresholdPort = _DdmTxPowThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1, 1, 1),
    _DdmTxPowThresholdPort_Type()
)
ddmTxPowThresholdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxPowThresholdPort.setStatus("current")


class _DdmTxPowThresholdHighAlarm_Type(OctetString):
    """Custom type ddmTxPowThresholdHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTxPowThresholdHighAlarm_Type.__name__ = "OctetString"
_DdmTxPowThresholdHighAlarm_Object = MibTableColumn
ddmTxPowThresholdHighAlarm = _DdmTxPowThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1, 1, 2),
    _DdmTxPowThresholdHighAlarm_Type()
)
ddmTxPowThresholdHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTxPowThresholdHighAlarm.setStatus("current")


class _DdmTxPowThresholdLowAlarm_Type(OctetString):
    """Custom type ddmTxPowThresholdLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTxPowThresholdLowAlarm_Type.__name__ = "OctetString"
_DdmTxPowThresholdLowAlarm_Object = MibTableColumn
ddmTxPowThresholdLowAlarm = _DdmTxPowThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1, 1, 3),
    _DdmTxPowThresholdLowAlarm_Type()
)
ddmTxPowThresholdLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTxPowThresholdLowAlarm.setStatus("current")


class _DdmTxPowThresholdHighWarn_Type(OctetString):
    """Custom type ddmTxPowThresholdHighWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTxPowThresholdHighWarn_Type.__name__ = "OctetString"
_DdmTxPowThresholdHighWarn_Object = MibTableColumn
ddmTxPowThresholdHighWarn = _DdmTxPowThresholdHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1, 1, 4),
    _DdmTxPowThresholdHighWarn_Type()
)
ddmTxPowThresholdHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTxPowThresholdHighWarn.setStatus("current")


class _DdmTxPowThresholdLowWarn_Type(OctetString):
    """Custom type ddmTxPowThresholdLowWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTxPowThresholdLowWarn_Type.__name__ = "OctetString"
_DdmTxPowThresholdLowWarn_Object = MibTableColumn
ddmTxPowThresholdLowWarn = _DdmTxPowThresholdLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1, 1, 5),
    _DdmTxPowThresholdLowWarn_Type()
)
ddmTxPowThresholdLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTxPowThresholdLowWarn.setStatus("current")


class _DdmTxPowThresholdPortLAG_Type(OctetString):
    """Custom type ddmTxPowThresholdPortLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTxPowThresholdPortLAG_Type.__name__ = "OctetString"
_DdmTxPowThresholdPortLAG_Object = MibTableColumn
ddmTxPowThresholdPortLAG = _DdmTxPowThresholdPortLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 5, 1, 1, 6),
    _DdmTxPowThresholdPortLAG_Type()
)
ddmTxPowThresholdPortLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxPowThresholdPortLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DDMTXPOWTHRESHOLD-MIB",
    **{"ddmTxPowThreshold": ddmTxPowThreshold,
       "ddmTxPowThresholdTable": ddmTxPowThresholdTable,
       "ddmTxPowThresholdEntry": ddmTxPowThresholdEntry,
       "ddmTxPowThresholdPort": ddmTxPowThresholdPort,
       "ddmTxPowThresholdHighAlarm": ddmTxPowThresholdHighAlarm,
       "ddmTxPowThresholdLowAlarm": ddmTxPowThresholdLowAlarm,
       "ddmTxPowThresholdHighWarn": ddmTxPowThresholdHighWarn,
       "ddmTxPowThresholdLowWarn": ddmTxPowThresholdLowWarn,
       "ddmTxPowThresholdPortLAG": ddmTxPowThresholdPortLAG}
)
