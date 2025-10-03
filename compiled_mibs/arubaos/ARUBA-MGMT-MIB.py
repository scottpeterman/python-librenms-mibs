# SNMP MIB module (ARUBA-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\ARUBA-MGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:42 2025
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

(arubaMgmt,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "arubaMgmt")

(ArubaEnableValue,) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaEnableValue")

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
 ObjectName,
 TimeTicks,
 Unsigned32,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arubaMgmtExtensions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaMgmtGroup_ObjectIdentity = ObjectIdentity
arubaMgmtGroup = _ArubaMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3, 1)
)
_ArubaGetTable_Type = ObjectIdentifier
_ArubaGetTable_Object = MibScalar
arubaGetTable = _ArubaGetTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 1),
    _ArubaGetTable_Type()
)
arubaGetTable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaGetTable.setStatus("current")
_ArubaNumberOfRows_Type = Integer32
_ArubaNumberOfRows_Object = MibScalar
arubaNumberOfRows = _ArubaNumberOfRows_Object(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 2),
    _ArubaNumberOfRows_Type()
)
arubaNumberOfRows.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaNumberOfRows.setStatus("current")
_ArubaRowInstance_Type = ObjectIdentifier
_ArubaRowInstance_Object = MibScalar
arubaRowInstance = _ArubaRowInstance_Object(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 3),
    _ArubaRowInstance_Type()
)
arubaRowInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaRowInstance.setStatus("current")


class _ArubaGetTableStatus_Type(Integer32):
    """Custom type arubaGetTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("endTable", 1),
          ("moreTable", 2),
          ("retrieveError", 3),
          ("noAmpSupport", 4),
          ("invalidColumnID", 5),
          ("resourceAllocationFailure", 6))
    )


_ArubaGetTableStatus_Type.__name__ = "Integer32"
_ArubaGetTableStatus_Object = MibScalar
arubaGetTableStatus = _ArubaGetTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 4),
    _ArubaGetTableStatus_Type()
)
arubaGetTableStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaGetTableStatus.setStatus("current")
_ArubaNumberOfColumns_Type = Integer32
_ArubaNumberOfColumns_Object = MibScalar
arubaNumberOfColumns = _ArubaNumberOfColumns_Object(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 5),
    _ArubaNumberOfColumns_Type()
)
arubaNumberOfColumns.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaNumberOfColumns.setStatus("current")
_ArubaSwitchAMPSupport_Type = ArubaEnableValue
_ArubaSwitchAMPSupport_Object = MibScalar
arubaSwitchAMPSupport = _ArubaSwitchAMPSupport_Object(
    (1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 6),
    _ArubaSwitchAMPSupport_Type()
)
arubaSwitchAMPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaSwitchAMPSupport.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBA-MGMT-MIB",
    **{"arubaMgmtExtensions": arubaMgmtExtensions,
       "arubaMgmtGroup": arubaMgmtGroup,
       "arubaGetTable": arubaGetTable,
       "arubaNumberOfRows": arubaNumberOfRows,
       "arubaRowInstance": arubaRowInstance,
       "arubaGetTableStatus": arubaGetTableStatus,
       "arubaNumberOfColumns": arubaNumberOfColumns,
       "arubaSwitchAMPSupport": arubaSwitchAMPSupport}
)
