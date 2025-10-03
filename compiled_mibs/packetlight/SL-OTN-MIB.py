# SNMP MIB module (SL-OTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-OTN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:58 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slOTN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OTNTraceMessage(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class OTNTrafficRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sonetSdh10G", 1),
          ("gbe10GLan", 2),
          ("fc10G", 3),
          ("otu2", 4),
          ("otu2eLan", 5),
          ("otu2eLanStuff", 6),
          ("otu2eFc", 7),
          ("otu2FcStuff", 8))
    )



class OTNOperationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("sync", 2),
          ("bypass", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SlOTNConfig_ObjectIdentity = ObjectIdentity
slOTNConfig = _SlOTNConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1)
)
_SlOTNConfigTable_Object = MibTable
slOTNConfigTable = _SlOTNConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    slOTNConfigTable.setStatus("current")
_SlOTNConfigEntry_Object = MibTableRow
slOTNConfigEntry = _SlOTNConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1)
)
slOTNConfigEntry.setIndexNames(
    (0, "SL-OTN-MIB", "slOTNConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slOTNConfigEntry.setStatus("current")
_SlOTNConfigLineIndex_Type = InterfaceIndex
_SlOTNConfigLineIndex_Object = MibTableColumn
slOTNConfigLineIndex = _SlOTNConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 1),
    _SlOTNConfigLineIndex_Type()
)
slOTNConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNConfigLineIndex.setStatus("current")
_SlOTNConfigOperationMode_Type = OTNOperationMode
_SlOTNConfigOperationMode_Object = MibTableColumn
slOTNConfigOperationMode = _SlOTNConfigOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 2),
    _SlOTNConfigOperationMode_Type()
)
slOTNConfigOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigOperationMode.setStatus("current")
_SlOTNConfigFECEnabled_Type = Integer32
_SlOTNConfigFECEnabled_Object = MibTableColumn
slOTNConfigFECEnabled = _SlOTNConfigFECEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 3),
    _SlOTNConfigFECEnabled_Type()
)
slOTNConfigFECEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigFECEnabled.setStatus("current")
_SlOTNConfigStuffingEnabled_Type = TruthValue
_SlOTNConfigStuffingEnabled_Object = MibTableColumn
slOTNConfigStuffingEnabled = _SlOTNConfigStuffingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 4),
    _SlOTNConfigStuffingEnabled_Type()
)
slOTNConfigStuffingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigStuffingEnabled.setStatus("current")
_SlOTNConfigOTUkTIMDetEnabled_Type = TruthValue
_SlOTNConfigOTUkTIMDetEnabled_Object = MibTableColumn
slOTNConfigOTUkTIMDetEnabled = _SlOTNConfigOTUkTIMDetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 5),
    _SlOTNConfigOTUkTIMDetEnabled_Type()
)
slOTNConfigOTUkTIMDetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigOTUkTIMDetEnabled.setStatus("current")
_SlOTNConfigOTUkDAPIToTransmit_Type = OTNTraceMessage
_SlOTNConfigOTUkDAPIToTransmit_Object = MibTableColumn
slOTNConfigOTUkDAPIToTransmit = _SlOTNConfigOTUkDAPIToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 6),
    _SlOTNConfigOTUkDAPIToTransmit_Type()
)
slOTNConfigOTUkDAPIToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigOTUkDAPIToTransmit.setStatus("current")
_SlOTNConfigOTUkSAPIToTransmit_Type = OTNTraceMessage
_SlOTNConfigOTUkSAPIToTransmit_Object = MibTableColumn
slOTNConfigOTUkSAPIToTransmit = _SlOTNConfigOTUkSAPIToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 7),
    _SlOTNConfigOTUkSAPIToTransmit_Type()
)
slOTNConfigOTUkSAPIToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigOTUkSAPIToTransmit.setStatus("current")
_SlOTNConfigOTUkDAPIToExpect_Type = OTNTraceMessage
_SlOTNConfigOTUkDAPIToExpect_Object = MibTableColumn
slOTNConfigOTUkDAPIToExpect = _SlOTNConfigOTUkDAPIToExpect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 8),
    _SlOTNConfigOTUkDAPIToExpect_Type()
)
slOTNConfigOTUkDAPIToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigOTUkDAPIToExpect.setStatus("current")
_SlOTNConfigOTUkSAPIToExpect_Type = OTNTraceMessage
_SlOTNConfigOTUkSAPIToExpect_Object = MibTableColumn
slOTNConfigOTUkSAPIToExpect = _SlOTNConfigOTUkSAPIToExpect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 9),
    _SlOTNConfigOTUkSAPIToExpect_Type()
)
slOTNConfigOTUkSAPIToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigOTUkSAPIToExpect.setStatus("current")
_SlOTNConfigOTUkDAPIReceived_Type = OTNTraceMessage
_SlOTNConfigOTUkDAPIReceived_Object = MibTableColumn
slOTNConfigOTUkDAPIReceived = _SlOTNConfigOTUkDAPIReceived_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 10),
    _SlOTNConfigOTUkDAPIReceived_Type()
)
slOTNConfigOTUkDAPIReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNConfigOTUkDAPIReceived.setStatus("current")
_SlOTNConfigOTUkSAPIReceived_Type = OTNTraceMessage
_SlOTNConfigOTUkSAPIReceived_Object = MibTableColumn
slOTNConfigOTUkSAPIReceived = _SlOTNConfigOTUkSAPIReceived_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 11),
    _SlOTNConfigOTUkSAPIReceived_Type()
)
slOTNConfigOTUkSAPIReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNConfigOTUkSAPIReceived.setStatus("current")
_SlOTNConfigODUkTIMDetEnabled_Type = TruthValue
_SlOTNConfigODUkTIMDetEnabled_Object = MibTableColumn
slOTNConfigODUkTIMDetEnabled = _SlOTNConfigODUkTIMDetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 12),
    _SlOTNConfigODUkTIMDetEnabled_Type()
)
slOTNConfigODUkTIMDetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigODUkTIMDetEnabled.setStatus("current")
_SlOTNConfigODUkDAPIToTransmit_Type = OTNTraceMessage
_SlOTNConfigODUkDAPIToTransmit_Object = MibTableColumn
slOTNConfigODUkDAPIToTransmit = _SlOTNConfigODUkDAPIToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 13),
    _SlOTNConfigODUkDAPIToTransmit_Type()
)
slOTNConfigODUkDAPIToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigODUkDAPIToTransmit.setStatus("current")
_SlOTNConfigODUkSAPIToTransmit_Type = OTNTraceMessage
_SlOTNConfigODUkSAPIToTransmit_Object = MibTableColumn
slOTNConfigODUkSAPIToTransmit = _SlOTNConfigODUkSAPIToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 14),
    _SlOTNConfigODUkSAPIToTransmit_Type()
)
slOTNConfigODUkSAPIToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigODUkSAPIToTransmit.setStatus("current")
_SlOTNConfigODUkDAPIToExpect_Type = OTNTraceMessage
_SlOTNConfigODUkDAPIToExpect_Object = MibTableColumn
slOTNConfigODUkDAPIToExpect = _SlOTNConfigODUkDAPIToExpect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 15),
    _SlOTNConfigODUkDAPIToExpect_Type()
)
slOTNConfigODUkDAPIToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigODUkDAPIToExpect.setStatus("current")
_SlOTNConfigODUkSAPIToExpect_Type = OTNTraceMessage
_SlOTNConfigODUkSAPIToExpect_Object = MibTableColumn
slOTNConfigODUkSAPIToExpect = _SlOTNConfigODUkSAPIToExpect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 16),
    _SlOTNConfigODUkSAPIToExpect_Type()
)
slOTNConfigODUkSAPIToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigODUkSAPIToExpect.setStatus("current")
_SlOTNConfigODUkDAPIReceived_Type = OTNTraceMessage
_SlOTNConfigODUkDAPIReceived_Object = MibTableColumn
slOTNConfigODUkDAPIReceived = _SlOTNConfigODUkDAPIReceived_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 17),
    _SlOTNConfigODUkDAPIReceived_Type()
)
slOTNConfigODUkDAPIReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNConfigODUkDAPIReceived.setStatus("current")
_SlOTNConfigODUkSAPIReceived_Type = OTNTraceMessage
_SlOTNConfigODUkSAPIReceived_Object = MibTableColumn
slOTNConfigODUkSAPIReceived = _SlOTNConfigODUkSAPIReceived_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 18),
    _SlOTNConfigODUkSAPIReceived_Type()
)
slOTNConfigODUkSAPIReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNConfigODUkSAPIReceived.setStatus("current")
_SlOTNConfigOTUkTIMKillEnabled_Type = TruthValue
_SlOTNConfigOTUkTIMKillEnabled_Object = MibTableColumn
slOTNConfigOTUkTIMKillEnabled = _SlOTNConfigOTUkTIMKillEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 19),
    _SlOTNConfigOTUkTIMKillEnabled_Type()
)
slOTNConfigOTUkTIMKillEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigOTUkTIMKillEnabled.setStatus("current")
_SlOTNConfigODUkTIMKillEnabled_Type = TruthValue
_SlOTNConfigODUkTIMKillEnabled_Object = MibTableColumn
slOTNConfigODUkTIMKillEnabled = _SlOTNConfigODUkTIMKillEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 20),
    _SlOTNConfigODUkTIMKillEnabled_Type()
)
slOTNConfigODUkTIMKillEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigODUkTIMKillEnabled.setStatus("current")
_SlOTNConfigInbandGCC_Type = Integer32
_SlOTNConfigInbandGCC_Object = MibTableColumn
slOTNConfigInbandGCC = _SlOTNConfigInbandGCC_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 21),
    _SlOTNConfigInbandGCC_Type()
)
slOTNConfigInbandGCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNConfigInbandGCC.setStatus("current")
_SlOTNPm_ObjectIdentity = ObjectIdentity
slOTNPm = _SlOTNPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2)
)
_SlOTNCurrentPmTable_Object = MibTable
slOTNCurrentPmTable = _SlOTNCurrentPmTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    slOTNCurrentPmTable.setStatus("current")
_SlOTNCurrentPmEntry_Object = MibTableRow
slOTNCurrentPmEntry = _SlOTNCurrentPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1)
)
slOTNCurrentPmEntry.setIndexNames(
    (0, "SL-OTN-MIB", "slOTNCurrentPmIndex"),
)
if mibBuilder.loadTexts:
    slOTNCurrentPmEntry.setStatus("current")
_SlOTNCurrentPmIndex_Type = InterfaceIndex
_SlOTNCurrentPmIndex_Object = MibTableColumn
slOTNCurrentPmIndex = _SlOTNCurrentPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 1),
    _SlOTNCurrentPmIndex_Type()
)
slOTNCurrentPmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmIndex.setStatus("current")
_SlOTNCurrentPmFecCe_Type = Integer32
_SlOTNCurrentPmFecCe_Object = MibTableColumn
slOTNCurrentPmFecCe = _SlOTNCurrentPmFecCe_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 2),
    _SlOTNCurrentPmFecCe_Type()
)
slOTNCurrentPmFecCe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmFecCe.setStatus("current")
_SlOTNCurrentPmFecCerMant_Type = Integer32
_SlOTNCurrentPmFecCerMant_Object = MibTableColumn
slOTNCurrentPmFecCerMant = _SlOTNCurrentPmFecCerMant_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 3),
    _SlOTNCurrentPmFecCerMant_Type()
)
slOTNCurrentPmFecCerMant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmFecCerMant.setStatus("current")
_SlOTNCurrentPmFecCerExp_Type = Integer32
_SlOTNCurrentPmFecCerExp_Object = MibTableColumn
slOTNCurrentPmFecCerExp = _SlOTNCurrentPmFecCerExp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 4),
    _SlOTNCurrentPmFecCerExp_Type()
)
slOTNCurrentPmFecCerExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmFecCerExp.setStatus("current")
_SlOTNCurrentPmFecCerValid_Type = TruthValue
_SlOTNCurrentPmFecCerValid_Object = MibTableColumn
slOTNCurrentPmFecCerValid = _SlOTNCurrentPmFecCerValid_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 5),
    _SlOTNCurrentPmFecCerValid_Type()
)
slOTNCurrentPmFecCerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmFecCerValid.setStatus("current")
_SlOTNCurrentPmFecCerMantFE_Type = Integer32
_SlOTNCurrentPmFecCerMantFE_Object = MibTableColumn
slOTNCurrentPmFecCerMantFE = _SlOTNCurrentPmFecCerMantFE_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 6),
    _SlOTNCurrentPmFecCerMantFE_Type()
)
slOTNCurrentPmFecCerMantFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmFecCerMantFE.setStatus("current")
_SlOTNCurrentPmFecCerExpFE_Type = Integer32
_SlOTNCurrentPmFecCerExpFE_Object = MibTableColumn
slOTNCurrentPmFecCerExpFE = _SlOTNCurrentPmFecCerExpFE_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 7),
    _SlOTNCurrentPmFecCerExpFE_Type()
)
slOTNCurrentPmFecCerExpFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmFecCerExpFE.setStatus("current")
_SlOTNCurrentPmFecCerValidFE_Type = TruthValue
_SlOTNCurrentPmFecCerValidFE_Object = MibTableColumn
slOTNCurrentPmFecCerValidFE = _SlOTNCurrentPmFecCerValidFE_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 8),
    _SlOTNCurrentPmFecCerValidFE_Type()
)
slOTNCurrentPmFecCerValidFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTNCurrentPmFecCerValidFE.setStatus("current")
_SlOTNCurrentPmReset_Type = Integer32
_SlOTNCurrentPmReset_Object = MibTableColumn
slOTNCurrentPmReset = _SlOTNCurrentPmReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 9),
    _SlOTNCurrentPmReset_Type()
)
slOTNCurrentPmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTNCurrentPmReset.setStatus("current")
_SlOTNTraps_ObjectIdentity = ObjectIdentity
slOTNTraps = _SlOTNTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-OTN-MIB",
    **{"OTNTraceMessage": OTNTraceMessage,
       "OTNTrafficRate": OTNTrafficRate,
       "OTNOperationMode": OTNOperationMode,
       "slOTN": slOTN,
       "slOTNConfig": slOTNConfig,
       "slOTNConfigTable": slOTNConfigTable,
       "slOTNConfigEntry": slOTNConfigEntry,
       "slOTNConfigLineIndex": slOTNConfigLineIndex,
       "slOTNConfigOperationMode": slOTNConfigOperationMode,
       "slOTNConfigFECEnabled": slOTNConfigFECEnabled,
       "slOTNConfigStuffingEnabled": slOTNConfigStuffingEnabled,
       "slOTNConfigOTUkTIMDetEnabled": slOTNConfigOTUkTIMDetEnabled,
       "slOTNConfigOTUkDAPIToTransmit": slOTNConfigOTUkDAPIToTransmit,
       "slOTNConfigOTUkSAPIToTransmit": slOTNConfigOTUkSAPIToTransmit,
       "slOTNConfigOTUkDAPIToExpect": slOTNConfigOTUkDAPIToExpect,
       "slOTNConfigOTUkSAPIToExpect": slOTNConfigOTUkSAPIToExpect,
       "slOTNConfigOTUkDAPIReceived": slOTNConfigOTUkDAPIReceived,
       "slOTNConfigOTUkSAPIReceived": slOTNConfigOTUkSAPIReceived,
       "slOTNConfigODUkTIMDetEnabled": slOTNConfigODUkTIMDetEnabled,
       "slOTNConfigODUkDAPIToTransmit": slOTNConfigODUkDAPIToTransmit,
       "slOTNConfigODUkSAPIToTransmit": slOTNConfigODUkSAPIToTransmit,
       "slOTNConfigODUkDAPIToExpect": slOTNConfigODUkDAPIToExpect,
       "slOTNConfigODUkSAPIToExpect": slOTNConfigODUkSAPIToExpect,
       "slOTNConfigODUkDAPIReceived": slOTNConfigODUkDAPIReceived,
       "slOTNConfigODUkSAPIReceived": slOTNConfigODUkSAPIReceived,
       "slOTNConfigOTUkTIMKillEnabled": slOTNConfigOTUkTIMKillEnabled,
       "slOTNConfigODUkTIMKillEnabled": slOTNConfigODUkTIMKillEnabled,
       "slOTNConfigInbandGCC": slOTNConfigInbandGCC,
       "slOTNPm": slOTNPm,
       "slOTNCurrentPmTable": slOTNCurrentPmTable,
       "slOTNCurrentPmEntry": slOTNCurrentPmEntry,
       "slOTNCurrentPmIndex": slOTNCurrentPmIndex,
       "slOTNCurrentPmFecCe": slOTNCurrentPmFecCe,
       "slOTNCurrentPmFecCerMant": slOTNCurrentPmFecCerMant,
       "slOTNCurrentPmFecCerExp": slOTNCurrentPmFecCerExp,
       "slOTNCurrentPmFecCerValid": slOTNCurrentPmFecCerValid,
       "slOTNCurrentPmFecCerMantFE": slOTNCurrentPmFecCerMantFE,
       "slOTNCurrentPmFecCerExpFE": slOTNCurrentPmFecCerExpFE,
       "slOTNCurrentPmFecCerValidFE": slOTNCurrentPmFecCerValidFE,
       "slOTNCurrentPmReset": slOTNCurrentPmReset,
       "slOTNTraps": slOTNTraps}
)
