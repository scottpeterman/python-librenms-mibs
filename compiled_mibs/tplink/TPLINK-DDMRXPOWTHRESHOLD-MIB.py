# SNMP MIB module (TPLINK-DDMRXPOWTHRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-DDMRXPOWTHRESHOLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:22 2025
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

ddmRxPowThreshold = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6)
)
if mibBuilder.loadTexts:
    ddmRxPowThreshold.setRevisions(
        ("2009-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DdmRxPowThresholdTable_Object = MibTable
ddmRxPowThresholdTable = _DdmRxPowThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ddmRxPowThresholdTable.setStatus("current")
_DdmRxPowThresholdEntry_Object = MibTableRow
ddmRxPowThresholdEntry = _DdmRxPowThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1, 1)
)
ddmRxPowThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmRxPowThresholdEntry.setStatus("current")


class _DdmRxPowThresholdPort_Type(DisplayString):
    """Custom type ddmRxPowThresholdPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DdmRxPowThresholdPort_Type.__name__ = "DisplayString"
_DdmRxPowThresholdPort_Object = MibTableColumn
ddmRxPowThresholdPort = _DdmRxPowThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1, 1, 1),
    _DdmRxPowThresholdPort_Type()
)
ddmRxPowThresholdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxPowThresholdPort.setStatus("current")


class _DdmRxPowThresholdHighAlarm_Type(OctetString):
    """Custom type ddmRxPowThresholdHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmRxPowThresholdHighAlarm_Type.__name__ = "OctetString"
_DdmRxPowThresholdHighAlarm_Object = MibTableColumn
ddmRxPowThresholdHighAlarm = _DdmRxPowThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1, 1, 2),
    _DdmRxPowThresholdHighAlarm_Type()
)
ddmRxPowThresholdHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmRxPowThresholdHighAlarm.setStatus("current")


class _DdmRxPowThresholdLowAlarm_Type(OctetString):
    """Custom type ddmRxPowThresholdLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmRxPowThresholdLowAlarm_Type.__name__ = "OctetString"
_DdmRxPowThresholdLowAlarm_Object = MibTableColumn
ddmRxPowThresholdLowAlarm = _DdmRxPowThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1, 1, 3),
    _DdmRxPowThresholdLowAlarm_Type()
)
ddmRxPowThresholdLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmRxPowThresholdLowAlarm.setStatus("current")


class _DdmRxPowThresholdHighWarn_Type(OctetString):
    """Custom type ddmRxPowThresholdHighWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmRxPowThresholdHighWarn_Type.__name__ = "OctetString"
_DdmRxPowThresholdHighWarn_Object = MibTableColumn
ddmRxPowThresholdHighWarn = _DdmRxPowThresholdHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1, 1, 4),
    _DdmRxPowThresholdHighWarn_Type()
)
ddmRxPowThresholdHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmRxPowThresholdHighWarn.setStatus("current")


class _DdmRxPowThresholdLowWarn_Type(OctetString):
    """Custom type ddmRxPowThresholdLowWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmRxPowThresholdLowWarn_Type.__name__ = "OctetString"
_DdmRxPowThresholdLowWarn_Object = MibTableColumn
ddmRxPowThresholdLowWarn = _DdmRxPowThresholdLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1, 1, 5),
    _DdmRxPowThresholdLowWarn_Type()
)
ddmRxPowThresholdLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmRxPowThresholdLowWarn.setStatus("current")


class _DdmRxPowThresholdPortLAG_Type(OctetString):
    """Custom type ddmRxPowThresholdPortLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmRxPowThresholdPortLAG_Type.__name__ = "OctetString"
_DdmRxPowThresholdPortLAG_Object = MibTableColumn
ddmRxPowThresholdPortLAG = _DdmRxPowThresholdPortLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 6, 1, 1, 6),
    _DdmRxPowThresholdPortLAG_Type()
)
ddmRxPowThresholdPortLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxPowThresholdPortLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DDMRXPOWTHRESHOLD-MIB",
    **{"ddmRxPowThreshold": ddmRxPowThreshold,
       "ddmRxPowThresholdTable": ddmRxPowThresholdTable,
       "ddmRxPowThresholdEntry": ddmRxPowThresholdEntry,
       "ddmRxPowThresholdPort": ddmRxPowThresholdPort,
       "ddmRxPowThresholdHighAlarm": ddmRxPowThresholdHighAlarm,
       "ddmRxPowThresholdLowAlarm": ddmRxPowThresholdLowAlarm,
       "ddmRxPowThresholdHighWarn": ddmRxPowThresholdHighWarn,
       "ddmRxPowThresholdLowWarn": ddmRxPowThresholdLowWarn,
       "ddmRxPowThresholdPortLAG": ddmRxPowThresholdPortLAG}
)
