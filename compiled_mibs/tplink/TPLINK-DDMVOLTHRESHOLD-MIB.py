# SNMP MIB module (TPLINK-DDMVOLTHRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-DDMVOLTHRESHOLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:28 2025
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

ddmVolThreshold = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3)
)
if mibBuilder.loadTexts:
    ddmVolThreshold.setRevisions(
        ("2009-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DdmVolThresholdTable_Object = MibTable
ddmVolThresholdTable = _DdmVolThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ddmVolThresholdTable.setStatus("current")
_DdmVolThresholdEntry_Object = MibTableRow
ddmVolThresholdEntry = _DdmVolThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1, 1)
)
ddmVolThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmVolThresholdEntry.setStatus("current")


class _DdmVolThresholdPort_Type(DisplayString):
    """Custom type ddmVolThresholdPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DdmVolThresholdPort_Type.__name__ = "DisplayString"
_DdmVolThresholdPort_Object = MibTableColumn
ddmVolThresholdPort = _DdmVolThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1, 1, 1),
    _DdmVolThresholdPort_Type()
)
ddmVolThresholdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmVolThresholdPort.setStatus("current")


class _DdmVolThresholdHighAlarm_Type(OctetString):
    """Custom type ddmVolThresholdHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmVolThresholdHighAlarm_Type.__name__ = "OctetString"
_DdmVolThresholdHighAlarm_Object = MibTableColumn
ddmVolThresholdHighAlarm = _DdmVolThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1, 1, 2),
    _DdmVolThresholdHighAlarm_Type()
)
ddmVolThresholdHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmVolThresholdHighAlarm.setStatus("current")


class _DdmVolThresholdLowAlarm_Type(OctetString):
    """Custom type ddmVolThresholdLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmVolThresholdLowAlarm_Type.__name__ = "OctetString"
_DdmVolThresholdLowAlarm_Object = MibTableColumn
ddmVolThresholdLowAlarm = _DdmVolThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1, 1, 3),
    _DdmVolThresholdLowAlarm_Type()
)
ddmVolThresholdLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmVolThresholdLowAlarm.setStatus("current")


class _DdmVolThresholdHighWarn_Type(OctetString):
    """Custom type ddmVolThresholdHighWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmVolThresholdHighWarn_Type.__name__ = "OctetString"
_DdmVolThresholdHighWarn_Object = MibTableColumn
ddmVolThresholdHighWarn = _DdmVolThresholdHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1, 1, 4),
    _DdmVolThresholdHighWarn_Type()
)
ddmVolThresholdHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmVolThresholdHighWarn.setStatus("current")


class _DdmVolThresholdLowWarn_Type(OctetString):
    """Custom type ddmVolThresholdLowWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmVolThresholdLowWarn_Type.__name__ = "OctetString"
_DdmVolThresholdLowWarn_Object = MibTableColumn
ddmVolThresholdLowWarn = _DdmVolThresholdLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1, 1, 5),
    _DdmVolThresholdLowWarn_Type()
)
ddmVolThresholdLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmVolThresholdLowWarn.setStatus("current")


class _DdmVolThresholdPortLAG_Type(OctetString):
    """Custom type ddmVolThresholdPortLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmVolThresholdPortLAG_Type.__name__ = "OctetString"
_DdmVolThresholdPortLAG_Object = MibTableColumn
ddmVolThresholdPortLAG = _DdmVolThresholdPortLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 3, 1, 1, 6),
    _DdmVolThresholdPortLAG_Type()
)
ddmVolThresholdPortLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmVolThresholdPortLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DDMVOLTHRESHOLD-MIB",
    **{"ddmVolThreshold": ddmVolThreshold,
       "ddmVolThresholdTable": ddmVolThresholdTable,
       "ddmVolThresholdEntry": ddmVolThresholdEntry,
       "ddmVolThresholdPort": ddmVolThresholdPort,
       "ddmVolThresholdHighAlarm": ddmVolThresholdHighAlarm,
       "ddmVolThresholdLowAlarm": ddmVolThresholdLowAlarm,
       "ddmVolThresholdHighWarn": ddmVolThresholdHighWarn,
       "ddmVolThresholdLowWarn": ddmVolThresholdLowWarn,
       "ddmVolThresholdPortLAG": ddmVolThresholdPortLAG}
)
