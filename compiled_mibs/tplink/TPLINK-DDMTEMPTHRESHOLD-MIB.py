# SNMP MIB module (TPLINK-DDMTEMPTHRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-DDMTEMPTHRESHOLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:25 2025
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

ddmTempThreshold = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2)
)
if mibBuilder.loadTexts:
    ddmTempThreshold.setRevisions(
        ("2009-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DdmTempThresholdTable_Object = MibTable
ddmTempThresholdTable = _DdmTempThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ddmTempThresholdTable.setStatus("current")
_DdmTempThresholdEntry_Object = MibTableRow
ddmTempThresholdEntry = _DdmTempThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1, 1)
)
ddmTempThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmTempThresholdEntry.setStatus("current")


class _DdmTempThresholdPort_Type(DisplayString):
    """Custom type ddmTempThresholdPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DdmTempThresholdPort_Type.__name__ = "DisplayString"
_DdmTempThresholdPort_Object = MibTableColumn
ddmTempThresholdPort = _DdmTempThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1, 1, 1),
    _DdmTempThresholdPort_Type()
)
ddmTempThresholdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempThresholdPort.setStatus("current")


class _DdmTempThresholdHighAlarm_Type(OctetString):
    """Custom type ddmTempThresholdHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTempThresholdHighAlarm_Type.__name__ = "OctetString"
_DdmTempThresholdHighAlarm_Object = MibTableColumn
ddmTempThresholdHighAlarm = _DdmTempThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1, 1, 2),
    _DdmTempThresholdHighAlarm_Type()
)
ddmTempThresholdHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTempThresholdHighAlarm.setStatus("current")


class _DdmTempThresholdLowAlarm_Type(OctetString):
    """Custom type ddmTempThresholdLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTempThresholdLowAlarm_Type.__name__ = "OctetString"
_DdmTempThresholdLowAlarm_Object = MibTableColumn
ddmTempThresholdLowAlarm = _DdmTempThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1, 1, 3),
    _DdmTempThresholdLowAlarm_Type()
)
ddmTempThresholdLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTempThresholdLowAlarm.setStatus("current")


class _DdmTempThresholdHighWarn_Type(OctetString):
    """Custom type ddmTempThresholdHighWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTempThresholdHighWarn_Type.__name__ = "OctetString"
_DdmTempThresholdHighWarn_Object = MibTableColumn
ddmTempThresholdHighWarn = _DdmTempThresholdHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1, 1, 4),
    _DdmTempThresholdHighWarn_Type()
)
ddmTempThresholdHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTempThresholdHighWarn.setStatus("current")


class _DdmTempThresholdLowWarn_Type(OctetString):
    """Custom type ddmTempThresholdLowWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTempThresholdLowWarn_Type.__name__ = "OctetString"
_DdmTempThresholdLowWarn_Object = MibTableColumn
ddmTempThresholdLowWarn = _DdmTempThresholdLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1, 1, 5),
    _DdmTempThresholdLowWarn_Type()
)
ddmTempThresholdLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTempThresholdLowWarn.setStatus("current")


class _DdmTempThresholdPortLAG_Type(OctetString):
    """Custom type ddmTempThresholdPortLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmTempThresholdPortLAG_Type.__name__ = "OctetString"
_DdmTempThresholdPortLAG_Object = MibTableColumn
ddmTempThresholdPortLAG = _DdmTempThresholdPortLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 2, 1, 1, 6),
    _DdmTempThresholdPortLAG_Type()
)
ddmTempThresholdPortLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempThresholdPortLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DDMTEMPTHRESHOLD-MIB",
    **{"ddmTempThreshold": ddmTempThreshold,
       "ddmTempThresholdTable": ddmTempThresholdTable,
       "ddmTempThresholdEntry": ddmTempThresholdEntry,
       "ddmTempThresholdPort": ddmTempThresholdPort,
       "ddmTempThresholdHighAlarm": ddmTempThresholdHighAlarm,
       "ddmTempThresholdLowAlarm": ddmTempThresholdLowAlarm,
       "ddmTempThresholdHighWarn": ddmTempThresholdHighWarn,
       "ddmTempThresholdLowWarn": ddmTempThresholdLowWarn,
       "ddmTempThresholdPortLAG": ddmTempThresholdPortLAG}
)
