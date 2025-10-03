# SNMP MIB module (TPLINK-DDMBIASCURTHRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-DDMBIASCURTHRESHOLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:19 2025
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

ddmBiasCurThreshold = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4)
)
if mibBuilder.loadTexts:
    ddmBiasCurThreshold.setRevisions(
        ("2009-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DdmBiasCurThresholdTable_Object = MibTable
ddmBiasCurThresholdTable = _DdmBiasCurThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ddmBiasCurThresholdTable.setStatus("current")
_DdmBiasCurThresholdEntry_Object = MibTableRow
ddmBiasCurThresholdEntry = _DdmBiasCurThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1, 1)
)
ddmBiasCurThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmBiasCurThresholdEntry.setStatus("current")


class _DdmBiasCurThresholdPort_Type(DisplayString):
    """Custom type ddmBiasCurThresholdPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DdmBiasCurThresholdPort_Type.__name__ = "DisplayString"
_DdmBiasCurThresholdPort_Object = MibTableColumn
ddmBiasCurThresholdPort = _DdmBiasCurThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1, 1, 1),
    _DdmBiasCurThresholdPort_Type()
)
ddmBiasCurThresholdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmBiasCurThresholdPort.setStatus("current")


class _DdmBiasCurThresholdHighAlarm_Type(OctetString):
    """Custom type ddmBiasCurThresholdHighAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmBiasCurThresholdHighAlarm_Type.__name__ = "OctetString"
_DdmBiasCurThresholdHighAlarm_Object = MibTableColumn
ddmBiasCurThresholdHighAlarm = _DdmBiasCurThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1, 1, 2),
    _DdmBiasCurThresholdHighAlarm_Type()
)
ddmBiasCurThresholdHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmBiasCurThresholdHighAlarm.setStatus("current")


class _DdmBiasCurThresholdLowAlarm_Type(OctetString):
    """Custom type ddmBiasCurThresholdLowAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmBiasCurThresholdLowAlarm_Type.__name__ = "OctetString"
_DdmBiasCurThresholdLowAlarm_Object = MibTableColumn
ddmBiasCurThresholdLowAlarm = _DdmBiasCurThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1, 1, 3),
    _DdmBiasCurThresholdLowAlarm_Type()
)
ddmBiasCurThresholdLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmBiasCurThresholdLowAlarm.setStatus("current")


class _DdmBiasCurThresholdHighWarn_Type(OctetString):
    """Custom type ddmBiasCurThresholdHighWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmBiasCurThresholdHighWarn_Type.__name__ = "OctetString"
_DdmBiasCurThresholdHighWarn_Object = MibTableColumn
ddmBiasCurThresholdHighWarn = _DdmBiasCurThresholdHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1, 1, 4),
    _DdmBiasCurThresholdHighWarn_Type()
)
ddmBiasCurThresholdHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmBiasCurThresholdHighWarn.setStatus("current")


class _DdmBiasCurThresholdLowWarn_Type(OctetString):
    """Custom type ddmBiasCurThresholdLowWarn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmBiasCurThresholdLowWarn_Type.__name__ = "OctetString"
_DdmBiasCurThresholdLowWarn_Object = MibTableColumn
ddmBiasCurThresholdLowWarn = _DdmBiasCurThresholdLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1, 1, 5),
    _DdmBiasCurThresholdLowWarn_Type()
)
ddmBiasCurThresholdLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmBiasCurThresholdLowWarn.setStatus("current")


class _DdmBiasCurThresholdPortLAG_Type(OctetString):
    """Custom type ddmBiasCurThresholdPortLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DdmBiasCurThresholdPortLAG_Type.__name__ = "OctetString"
_DdmBiasCurThresholdPortLAG_Object = MibTableColumn
ddmBiasCurThresholdPortLAG = _DdmBiasCurThresholdPortLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 4, 1, 1, 6),
    _DdmBiasCurThresholdPortLAG_Type()
)
ddmBiasCurThresholdPortLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmBiasCurThresholdPortLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DDMBIASCURTHRESHOLD-MIB",
    **{"ddmBiasCurThreshold": ddmBiasCurThreshold,
       "ddmBiasCurThresholdTable": ddmBiasCurThresholdTable,
       "ddmBiasCurThresholdEntry": ddmBiasCurThresholdEntry,
       "ddmBiasCurThresholdPort": ddmBiasCurThresholdPort,
       "ddmBiasCurThresholdHighAlarm": ddmBiasCurThresholdHighAlarm,
       "ddmBiasCurThresholdLowAlarm": ddmBiasCurThresholdLowAlarm,
       "ddmBiasCurThresholdHighWarn": ddmBiasCurThresholdHighWarn,
       "ddmBiasCurThresholdLowWarn": ddmBiasCurThresholdLowWarn,
       "ddmBiasCurThresholdPortLAG": ddmBiasCurThresholdPortLAG}
)
