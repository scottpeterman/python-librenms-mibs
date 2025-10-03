# SNMP MIB module (WAYSTREAM-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\waystream\WAYSTREAM-COPY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:58 2025
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

(wsExperiment,) = mibBuilder.importSymbols(
    "WAYSTREAM-SMI",
    "wsExperiment")


# MODULE-IDENTITY

wsCopy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2)
)
if mibBuilder.loadTexts:
    wsCopy.setRevisions(
        ("2017-02-10 11:00",
         "2011-01-11 17:35",
         "2009-03-23 11:17",
         "2008-09-10 15:38")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsCopyNextState_Type = Unsigned32
_WsCopyNextState_Object = MibScalar
wsCopyNextState = _WsCopyNextState_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 1),
    _WsCopyNextState_Type()
)
wsCopyNextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCopyNextState.setStatus("current")
_WsCopyTable_Object = MibTable
wsCopyTable = _WsCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wsCopyTable.setStatus("current")
_WsCopyEntry_Object = MibTableRow
wsCopyEntry = _WsCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1)
)
wsCopyEntry.setIndexNames(
    (0, "WAYSTREAM-COPY-MIB", "wsCopyIndex"),
)
if mibBuilder.loadTexts:
    wsCopyEntry.setStatus("current")
_WsCopyIndex_Type = Unsigned32
_WsCopyIndex_Object = MibTableColumn
wsCopyIndex = _WsCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 1),
    _WsCopyIndex_Type()
)
wsCopyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCopyIndex.setStatus("current")


class _WsCopySource_Type(DisplayString):
    """Custom type wsCopySource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WsCopySource_Type.__name__ = "DisplayString"
_WsCopySource_Object = MibTableColumn
wsCopySource = _WsCopySource_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 2),
    _WsCopySource_Type()
)
wsCopySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsCopySource.setStatus("current")


class _WsCopyDestination_Type(DisplayString):
    """Custom type wsCopyDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WsCopyDestination_Type.__name__ = "DisplayString"
_WsCopyDestination_Object = MibTableColumn
wsCopyDestination = _WsCopyDestination_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 3),
    _WsCopyDestination_Type()
)
wsCopyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsCopyDestination.setStatus("current")


class _WsCopyStatus_Type(Integer32):
    """Custom type wsCopyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notused", 0),
          ("start", 1),
          ("stop", 2),
          ("destroy", 3),
          ("init", 4),
          ("inprogress", 5),
          ("failed", 6),
          ("finished", 7))
    )


_WsCopyStatus_Type.__name__ = "Integer32"
_WsCopyStatus_Object = MibTableColumn
wsCopyStatus = _WsCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 4),
    _WsCopyStatus_Type()
)
wsCopyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsCopyStatus.setStatus("current")


class _WsCopyError_Type(DisplayString):
    """Custom type wsCopyError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WsCopyError_Type.__name__ = "DisplayString"
_WsCopyError_Object = MibTableColumn
wsCopyError = _WsCopyError_Object(
    (1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 5),
    _WsCopyError_Type()
)
wsCopyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCopyError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAYSTREAM-COPY-MIB",
    **{"wsCopy": wsCopy,
       "wsCopyNextState": wsCopyNextState,
       "wsCopyTable": wsCopyTable,
       "wsCopyEntry": wsCopyEntry,
       "wsCopyIndex": wsCopyIndex,
       "wsCopySource": wsCopySource,
       "wsCopyDestination": wsCopyDestination,
       "wsCopyStatus": wsCopyStatus,
       "wsCopyError": wsCopyError}
)
